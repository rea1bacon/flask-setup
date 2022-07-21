#!/bin/bash
echo "debug=true" >.env
read -r -p "[?] Enter app secret :" secret
echo "secret=$secret" >>.env
read -r -p "[?] Enter database name :" db
echo "db=$db" >>.env
read -r -p "[?] Enter database type (mysql/sqlite) :" dbt
echo "dbt=$dbt" >>.env
if [ "$dbt" == "mysql" ]; then
	read -r -p "[?] Enter connection settings, please % encode special chars (username:password@server) :" dbc
	echo "dbc='$dbc'" >>.env
fi
