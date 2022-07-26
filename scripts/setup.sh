#!/bin/bash
echo "debug=true" >.env
read -r -p "[?] Enter app secret :" secret
echo "secret=$secret" >>.env
read -r -p "[?] Enter database url :" dbu
echo "dbu=$dbu" >>.env
