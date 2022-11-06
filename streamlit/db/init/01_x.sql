use todos;

create table if not exists awesome_table (
    name text,
    age smallint unsigned,
    height float unsigned,
    date_birth date,
    balance double
)
;

insert into awesome_table (
    name, age, height, date_birth, balance
) values
( "pokemon", 33, 166.6, '1990-05-08', -0.9 ),
( "yuji", 1, 99.9, '1989-01-08', 100 ),
( "tanaka", 0, 165.5, '1989-03-08', 11 ),
( "taro", 99, 165.5, '1989-07-08', -1.1 ),
( "山田", 23, 180.5, '2000-09-08', 0 );
