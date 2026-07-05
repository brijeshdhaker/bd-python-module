#!/bin/bash

#
# Setup User & Databases
#

# wait-for-mysql.sh
# until nc -z -w5 mysqlserver.sandbox.net 3306; do
#   echo "Waiting for MySQL to be ready..."
#   sleep 1
# done
# echo "MySQL is ready!"


#--user=root --password=paSSW0rd --host=mysqlserver.sandbox.net --database=SANDBOXDB
mysql --host=localhost --user=root --password=$MYSQL_ADMIN_PASSWORD <<EOF

CREATE DATABASE SANDBOXDB;

CREATE USER 'root'@'%' IDENTIFIED BY '$MYSQL_ADMIN_PASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

CREATE USER 'admin'@'%' IDENTIFIED BY '$MYSQL_ADMIN_PASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH GRANT OPTION;

CREATE USER 'operate'@'%' IDENTIFIED BY '$MYSQL_ADMIN_PASSWORD';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'operate'@'%' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON SANDBOXDB.* TO 'operate'@'%';

FLUSH PRIVILEGES;

EOF