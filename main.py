from sqlite_db import Database
from gpt_connector import GPTConnector
from resources.sqlite_statements import CREATE_STATEMENTS, INSERT_STATEMENTS, DELETE_STATEMENTS
from resources.prompts import PROMPTS

DB_FILE = "db/sqlitedb.db"

def main():
    db = Database(DB_FILE)
    
    for prompt in PROMPTS:
        print("Prompt: " + prompt)
        
        # reset database
        db.create_tables(CREATE_STATEMENTS)
        db.execute_all(DELETE_STATEMENTS)
        db.execute_all(INSERT_STATEMENTS)
    
        # prompt GPT for a query
        gpt_connector = GPTConnector()
        gpt_query = gpt_connector.ask_gpt(prompt)
        print(gpt_query)
        
        # run the query on the database
        query_response = db.query(gpt_query)
        print("DB response:")
        print(query_response)
        
        # prompt GPT for a friendly response of the results
        request_friendly_response = "Here is the database query result: " + query_response + \
            " \nExplain the results in a single sentance Do not include the select statement or "\
            "anything other than a single sentence explaining the results. Here is the query that "\
            "produced the response for context: " + prompt
        query_response = gpt_connector.ask_gpt(request_friendly_response)
        print("Friendly response:")
        print(query_response)
        print()
    


if __name__ == "__main__":
    main()
