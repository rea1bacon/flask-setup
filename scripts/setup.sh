#!/bin/bash
echo "debug=true" >.env
read -r -p "[?] Enter app secret :" secret
echo "secret=$secret" >>.env
read -r -p "[?] Enter database url :" dbu
echo "dbu=$dbu" >>.env
sudo echo "127.0.0.1       flaskezs.com" >>/etc/hosts
sudo echo "127.0.0.1       api.flaskezs.com" >>/etc/hosts
