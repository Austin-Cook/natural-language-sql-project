# Results

## Zero-Shot
### Results
#### ZERO_SHOT_INSTRUCTIONS
    Given the create table statements, create a sqlite select statement for the following prompt and return only the selected statement:
#### 1.
    - Statement:
        - ZERO_SHOT_INSTRUCTIONS + "Select the highest salaried baker. " + CREATE_TABLE_CONTEXT
    - Generated Query:
        - SELECT name, salary
          FROM baker
          ORDER BY salary DESC
          LIMIT 1;
    - DB Response:
        - ('Kevin', 54000)
    - Friendly Message:
        - The query result is the name 'Kevin' and his salary of 54000, indicating that Kevin is the highest salaried baker in the database.
#### 2.
    - Statement:
        - ZERO_SHOT_INSTRUCTIONS + "Select all bakers that work on Tuesdays. " + CREATE_TABLE_CONTEXT
    - Generated Query:
        - SELECT b.name
          FROM baker b
          JOIN schedule s ON b.id = s.baker_id
          WHERE s.day_of_week = 'T';
    - DB Response:
        - None
    - Result:
        - The query result is a list of bakers who work on Tuesdays.
#### 3.
    - Statement:
        - ZERO_SHOT_INSTRUCTIONS + "Select the names of all bakers who bake Alice's favorite item. " + CREATE_TABLE_CONTEXT
    - Generated Query:
        - SELECT b.name
          FROM baker b
          JOIN baker_item bi ON b.id = bi.baker_id
          JOIN item i ON bi.item_id = i.id
          WHERE i.name = (SELECT name FROM item WHERE id = (SELECT favorite_item FROM baker WHERE name = 'Alice'));
    - DB Response:
        - ('Alice',)('Bob',)('Charlie',)('Daisy',)('Edward',)('Fiona',)
    - Result:
        - The query result shows the names of all bakers who bake Alice's favorite item.

## Single-Shot
### Training Examples for Single-Shot
##### EXAMPLE1
        - Statement: Select the names of all bakers who bake Alice's favorite item.
        - Generated query: SELECT b.name FROM baker b JOIN baker_item bi ON b.id = bi.baker_id JOIN item i ON bi.item_id = i.id WHERE i.name = (SELECT name FROM item WHERE id = (SELECT favorite_item FROM baker WHERE name = 'Alice')); 
##### EXAMPLE2
        - Statement: Select the highest salaried baker.
        - Generated query: SELECT name, salary FROM baker ORDER BY salary DESC LIMIT 1;
##### EXAMPLE3
        - Statement: Select all bakers that work on Tuesdays
        - Generated query: SELECT b.name FROM baker b JOIN schedule s ON b.id = s.baker_id WHERE s.day_of_week = 't';
### Single-Shot Results
#### SINGLE_DOMAIN_INSTRUCTIONS
    Given the create table statements, and the example queries, create a sqlite select statement for the following prompt and return only the selected statement:
##### 1.
    - Statement:
        - SINGLE_DOMAIN_INSTRUCTIONS + "Select the day/days of the week where the most bakers are working. " + CREATE_TABLE_CONTEXT + EXAMPLE1 + EXAMPLE2 + EXAMPLE3
    - Generated Query:
        - SELECT s.day_of_week
          FROM schedule s
          GROUP BY s.day_of_week
          HAVING COUNT(s.baker_id) = (
              SELECT MAX(baker_count)
              FROM (
                  SELECT COUNT(s.baker_id) as baker_count
                  FROM schedule s
                  GROUP BY s.day_of_week
              )
          );
    - DB Response:
        - ('w',)
    - Result:
        - The query result ('w',) indicates that there is a baker who works on Wednesdays.
##### 2.
    - Statement:
        - SINGLE_DOMAIN_INSTRUCTIONS + "Select the name and salary of the oldest baker. " + CREATE_TABLE_CONTEXT + EXAMPLE1 + EXAMPLE2 + EXAMPLE3
    - Generated Query:
        - SELECT name, salary 
          FROM baker 
          ORDER BY birthdate ASC 
          LIMIT 1;
    - DB Response:
        - ('Ivan', 52000)
    - Result:
        - The result is the name and salary of the oldest baker, which is Ivan with a salary of 52000.
##### 3.
    - Statement:
        - SINGLE_DOMAIN_INSTRUCTIONS + "Select the item made by the most bakers. " + CREATE_TABLE_CONTEXT + EXAMPLE1 + EXAMPLE2 + EXAMPLE3
    - Generated Query:
        - SELECT i.name 
          FROM item i 
          JOIN baker_item bi ON i.id = bi.item_id 
          GROUP BY i.name 
          ORDER BY COUNT(bi.baker_id) DESC 
          LIMIT 1;
    - DB Response:
        - ('Baguette',)
    - Result:
        - The query result is the item "Baguette".