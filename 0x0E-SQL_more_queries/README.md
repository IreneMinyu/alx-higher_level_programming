# SQL - More queries

## How To Create a New User and Grant Permissions in MySQL

### Creating a New User

`sudo mysql`

Note: If your root MySQL user is configured to authenticate with a password, you will need to use a different command to access the MySQL shell. The following will run your MySQL client with regular user privileges, and you will only gain administrator privileges within the database by authenticating with the correct password:

`mysql -u root -p`
Once you have access to the MySQL prompt, you can create a new user with a CREATE USER statement. These follow this general syntax:

``CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';`

Run the following command to create a user that authenticates with caching_sha2_password. Be sure to change sammy to your preferred username and password to a strong password of your choosing:

`CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';`

Note: There is a known issue with some versions of PHP that causes problems with caching_sha2_password. If you plan to use this database with a PHP application — phpMyAdmin, for example — you may want to create a user that will authenticate with the older, though still secure, mysql_native_password plugin instead:

`CREATE USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';`

If you aren’t sure, you can always create a user that authenticates with caching_sha2_plugin and then ALTER it later on with this command:

`ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';`

After creating your new user, you can grant them the appropriate privileges.

### Granting a User Permissions

The general syntax for granting user privileges is as follows:

`GRANT PRIVILEGE ON database.table TO 'username'@'host';`

Run this GRANT statement, replacing sammy with your own MySQL user’s name, to grant these privileges to your user:

`GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;`

Note that this statement also includes WITH GRANT OPTION. This will allow your MySQL user to grant any permissions that it has to other users on the system.

Warning: Some users may want to grant their MySQL user the ALL PRIVILEGES privilege, which will provide them with broad superuser privileges akin to the root user’s privileges, like so:

`GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;`

Such broad privileges should not be granted lightly, as anyone with access to this MySQL user will have complete control over every database on the server.
Many guides suggest running the FLUSH PRIVILEGES command immediately after a CREATE USER or GRANT statement in order to reload the grant tables to ensure that the new privileges are put into effect:

### FLUSH PRIVILEGES;

`REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';`

You can review a user’s current permissions by running the SHOW GRANTS command:

`SHOW GRANTS FOR 'username'@'host';`

Just as you can delete databases with DROP, you can use DROP to delete a user:

`DROP USER 'username'@'localhost';`

After creating your MySQL user and granting them privileges, you can exit the MySQL client:

`exit`

In the future, to log in as your new MySQL user, you’d use a command like the following:

`mysql -u sammy -p`
The -p flag will cause the MySQL client to prompt you for your MySQL user’s password in order to authenticate.

## MYSQL Grant statements

````GRANT privilege [,privilege],..
ON privilege_level
TO account_name;```

```GRANT SELECT
ON employees
TO bob@localhost;```

```GRANT INSERT, UPDATE, DELETE
ON employees
TO bob@localhost;```

Global privileges apply to all databases in a MySQL Server. To assign global privileges, you use the *.* syntax, for example:

```GRANT SELECT
ON *.*
TO bob@localhost;```

Database privileges apply to all objects in a database. To assign database-level privileges, you use the ON database_name.* syntax, for example:

```GRANT INSERT
ON classicmodels.*
TO bob@localhost;```

Table privileges apply to all columns in a table. To assign table-level privileges, you use the ON database_name.table_name syntax, for example:

```GRANT DELETE
ON classicmodels.employees
TO bob@localhsot;```

Column privileges apply to single columns in a table.  You must specify the column or columns for each privilege, for example:

```GRANT
   SELECT (employeeNumner,lastName, firstName,email),
   UPDATE(lastName)
ON employees
TO bob@localhost;```

Stored routine privileges apply to stored procedures and stored functions, for example:

```GRANT EXECUTE
ON PROCEDURE CheckCredit
TO bob@localhost;```

In this example, bob@localhost can execute the stored procedure CheckCredit in the current database.

Proxy user privileges allow one user to be a proxy for another. The proxy user gets all privileges of the proxied user. For example:

```GRANT PROXY
ON root
TO alice@localhost;```

## MySQL GRANT statement examples


First, create a new user called super@localhost by using the following CREATE USER statement:

```CREATE USER super@localhost
IDENTIFIED BY 'Secure1Pass!';```

Second, show the privileges assigned to super@localhost user by using the SHOW GRANTS statement.

```SHOW GRANTS FOR super@localhost;```

Third, grant all privileges in all databases in the current database server to super@localhost:

```GRANT ALL
ON classicmodels.*
TO super@localhost;```


Fourth, use the SHOW GRANTS statement again:

```SHOW GRANTS FOR super@localhost;```

# MYSQL Constraints

We have the following constraints:

- NOT NULL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY
- ENUM
- SET

### NOT NULL constraint

A column with a NOT NULL constraint, cannot have NULL values.

```CREATE TABLE People(Id INTEGER, LastName TEXT NOT NULL,
FirstName TEXT NOT NULL, City VARCHAR(55));```

```INSERT INTO People VALUES(1, 'Hanks', 'Robert', 'New York');```

### UNIQUE constraint

The UNIQUE constraint ensures that all data are unique in a column.

```CREATE TABLE Brands(Id INTEGER, BrandName VARCHAR(30) UNIQUE);```

```INSERT INTO Brands VALUES(1, 'Coca Cola');```

### Primary key

```CREATE TABLE Brands(Id INTEGER PRIMARY KEY, BrandName VARCHAR(30) UNIQUE);```

### Foreign key

```CREATE TABLE Authors(AuthorId INTEGER PRIMARY KEY, Name VARCHAR(70)) type=InnoDB;```

### ENUM constraint

```CREATE TABLE Shops(Id INTEGER, Name VARCHAR(55),Quality ENUM('High', 'Average', 'Low'));```

### SET constraint

```CREATE TABLE Students(Id INTEGER, Name VARCHAR(55),Certificates SET('A1', 'A2', 'B1', 'C1'));```

### 7 types of JOINs and how to use them

- INNER JOIN
```SELECT *
FROM table1
INNER JOIN table2
ON table1.col1 = table2.col2;```
- FULL [OUTER] JOIN
```SELECT *
FROM table1
FULL JOIN table2
ON table1.col1 = table2.col2;```
- FULL [OUTER] JOIN without the intersection
```SELECT *
FROM table1
FULL JOIN table2
ON table1.col1 = table2.col2
WHERE table1.col1 IS NULL
OR table2.col2 IS NULL;```
- LEFT [OUTER] JOIN
```SELECT *
FROM table1
LEFT JOIN table2
ON table1.col1 = table2.col2;```
- LEFT [OUTER] JOIN without the intersection
```SELECT *
FROM table1
LEFT JOIN table2
ON table1.col1 = table2.col2
WHERE table2.col2 IS NULL;```
- RIGHT [OUTER] JOIN
```SELECT *
FROM table1
RIGHT JOIN table2
ON table1.col1 = table2.col2;```
- RIGHT [OUTER] JOIN without the intersection
```SELECT *
FROM table1
RIGHT JOIN table2
ON table1.col1 = table2.col2
WHERE table1.col1 IS NULL;```

## MYSQL Cheat Sheet

https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf






````
