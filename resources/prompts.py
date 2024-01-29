CREATE_TABLE_CONTEXT = \
    "create table if not exists baker ( "\
    "id integer primary key, "\
    "name varchar (20), "\
    "birthdate date, "\
    "salary integer, "\
    "favorite_item integer, "\
    "foreign key (favorite_item) references item (id) "\
    "on delete set null "\
    "on update cascade"\
    "); "\
    "create table if not exists schedule ( "\
    "baker_id integer, "\
    "day_of_week char (1), "\
    "foreign key (baker_id) references baker (id) "\
    "on delete cascade "\
    "on update cascade"\
    "); "\
    "create table if not exists item ( "\
    "id integer primary key, "\
    "name varchar (20) unique, "\
    "price double "\
    "); "\
    "create table if not exists baker_item ( "\
    "baker_id integer, "\
    "item_id integer, "\
    "foreign key (baker_id) references baker (id) "\
    "on delete cascade "\
    "on update cascade, "\
    "foreign key (item_id) references item (id) "\
    "on delete cascade "\
    "on update cascade "\
    ");"

ZERO_SHOT_INSTRUCTIONS = "Given the create table statements, create a sqlite select statement for the following prompt and return only the selected statement: "
SINGLE_DOMAIN_INSTRUCTIONS = "Given the create table statements, and the example queries, create a sqlite select statement for the following prompt and return only the selected statement: "

EXAMPLE1 = "Example 1 statement: Select the names of all bakers who bake Alice's favorite item. Example 1 generated query: SELECT b.name FROM baker b JOIN baker_item bi ON b.id = bi.baker_id JOIN item i ON bi.item_id = i.id WHERE i.name = (SELECT name FROM item WHERE id = (SELECT favorite_item FROM baker WHERE name = 'Alice')); "
EXAMPLE2 = "Example 2 statement: Select the highest salaried baker. Example 2 generated query: SELECT name, salary FROM baker ORDER BY salary DESC LIMIT 1; "
EXAMPLE3 = "Example 3 statement: Select all bakers that work on Tuesdays Example 3 generated query: SELECT b.name FROM baker b JOIN schedule s ON b.id = s.baker_id WHERE s.day_of_week = 't'; "

PROMPTS = [
    ZERO_SHOT_INSTRUCTIONS + "Select the highest salaried baker. " + CREATE_TABLE_CONTEXT,
    ZERO_SHOT_INSTRUCTIONS + "Select all bakers that work on Tuesdays. " + CREATE_TABLE_CONTEXT,
    ZERO_SHOT_INSTRUCTIONS + "Select the names of all bakers who bake Alice's favorite item. " + CREATE_TABLE_CONTEXT,
    SINGLE_DOMAIN_INSTRUCTIONS + "Select the day/days of the week where the most bakers are working. " + CREATE_TABLE_CONTEXT + EXAMPLE1 + EXAMPLE2 + EXAMPLE3,
    SINGLE_DOMAIN_INSTRUCTIONS + "Select the name and salary of the oldest baker. " + CREATE_TABLE_CONTEXT + EXAMPLE1 + EXAMPLE2 + EXAMPLE3,
    SINGLE_DOMAIN_INSTRUCTIONS + "Select the item made by the most bakers. " + CREATE_TABLE_CONTEXT + EXAMPLE1 + EXAMPLE2 + EXAMPLE3
]
