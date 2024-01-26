from sqlite_db import Database
from gpt_connector import GPTConnector
from resources.sqlite_statements import CREATE_STATEMENTS, INSERT_STATEMENTS, DELETE_STATEMENTS

DB_FILE = "db/sqlitedb.db"
CURR_GPT_PROMPT = \
    "Given this create table statement, create a sqlite select statement for the following prompt and return only the selected statement: " + \
    "Select the highest salaried baker. " + \
    "create table if not exists baker ( " + "id integer primary key, " + "name varchar (20), " + \
    "birthdate date, " + "salary integer, " + "favorite_item integer, " + \
    "foreign key (favorite_item) references item (id) " + "on delete set null " + "on update cascade"


def main():
    db = Database(DB_FILE)
    
    # reset database
    db.create_tables(CREATE_STATEMENTS)
    db.execute_all(DELETE_STATEMENTS)
    db.execute_all(INSERT_STATEMENTS)
    
    # prompt GPT for a query
    gpt_connector = GPTConnector()
    gpt_query = gpt_connector.ask_gpt(CURR_GPT_PROMPT)
    print(gpt_query)
    
    # run the query on the database
    query_response = db.query(gpt_query)
    print("Db response:")
    print(query_response)


if __name__ == "__main__":
    main()
