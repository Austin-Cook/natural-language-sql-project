# Results

## Statements
- "Given this create table statement, create a sqlite select statement for the following prompt and return only the selected statement: Select the highest salaried baker. " + \
    "create table if not exists baker ( " + "id integer primary key, " + "name varchar (20), " + \
    "birthdate date, " + "salary integer, " + "favorite_item integer, " + \
    "foreign key (favorite_item) references item (id) " + "on delete set null " + "on update cascade"