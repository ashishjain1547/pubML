(base) ashish@ashish:~/Desktop$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.33-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
Query OK, 0 rows affected (0.00 sec)

mysql> exit
Bye
(base) ashish@ashish:~/Desktop$ sudo mysql
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)
(base) ashish@ashish:~/Desktop$ mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.33-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE USER 'ash'@'localhost' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.04 sec)

mysql> GRANT PRIVILEGE ON database.table TO 'ash'@'localhost';
ERROR 3619 (HY000): Illegal privilege level specified for table
mysql> GRANT CREATE, ALTER, DROP, INSERT, UPDATE, INDEX, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'ash'@'localhost' WITH GRANT OPTION;
Query OK, 0 rows affected (0.02 sec)

mysql> 
mysql> exit
Bye


$ mysql -u ash -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 8.0.33-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.



mysql> exit
Bye


(base) ashish@ashish:~/Desktop$ mysql -u ash -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 13
Server version: 8.0.33-0ubuntu0.22.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE TABLE leads (first_name varchar2(4000), last_name varchar2(4000), phone_work varchar2(4000);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'varchar2(4000), last_name varchar2(4000), phone_work varchar2(4000)' at line 1
mysql> CREATE TABLE leads (first_name varchar2(4000), last_name varchar2(4000), phone_work varchar2(4000));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'varchar2(4000), last_name varchar2(4000), phone_work varchar2(4000))' at line 1
mysql> 
mysql> 
mysql> CREATE TABLE leads (first_name varchar(4000), last_name varchar(4000), phone_work varchar(4000));
ERROR 1046 (3D000): No database selected
mysql> CREATE DATABASE `leadsdb`;
Query OK, 1 row affected (0.01 sec)

mysql> use leadsdb
Database changed
mysql> 
mysql> CREATE TABLE leads (first_name varchar(4000), last_name varchar(4000), phone_work varchar(4000));
Query OK, 0 rows affected (0.05 sec)

mysql> 





-------------------------



create table bitcoinprice(ticker_date varchar(4000), ticker_time varchar(4000), usd_btc real);


