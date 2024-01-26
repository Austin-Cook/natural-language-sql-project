# Natural Language SQL

## Setup
1) Set the OpenAI API key
    - (Linux) 
        1) Temporary
            - Set env variable with `export OPENAI_API_KEY='your_actual_api_key_here'`
        2) Parmanent
            - `nano ~/.bashrc`
            - Add line to bottom of file `export OPENAI_API_KEY='key_here'`
            - Apply changes with `source ~/.bashrc` or by restarting terminal

## Instructions
1) In main.py, update `CURR_GPT_PROMPT` to the desired prompt
2) Run `python3 main.py`