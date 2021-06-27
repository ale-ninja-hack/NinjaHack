#!/bin/bash
clear

rojo="\033[1;31m"
blanco="\033[1;37m"
amarillo="\033[1;33m"
negro="\033[1,30m"
cian="\033[1;36m"


read -p "Escribe la ip o el dominio: " ip

python3 hammer.py -s $ip
