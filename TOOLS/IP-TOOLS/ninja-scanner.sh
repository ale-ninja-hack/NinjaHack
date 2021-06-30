#!/bin/bash
# ninja ip info

banner() {
echo -e ""
echo ""
echo -e  "\e[1;32m  ▐ ▄  ▐ ▄  ▐▄▄▄ ▄▄▄· \e[0m"
echo -e  "\e[1;32m •█▌▐█•█▌▐█  ·██▐█ ▀█ \e[0m"
echo -e  "\e[1;32m ▐█▐▐▌▐█▐▐▌▪▄ ██▄█▀▀█ \e[0m"
echo -e  "\e[1;32m ██▐█▌██▐█▌▐▌▐█▌▐█ ▪▐▌\e[0m"
echo -e  "\e[1;32m ▀▀ █▪▀▀ █▪ ▀▀▀• ▀  ▀  \e[0m"
echo -e ""
}

restartprogram() {
echo "
Esa Opción es incorrecta, elije de nuevo !
Elige entre el 1 2 o 3"
sleep 2
clear
menuprincipal
}


miIP() {
	curl -s http://ip-api.com/
	echo ""
	exit
}

tarjetaip() {
	echo ""
	echo -e "\e[36m Escribe la dirección IP \e[0m"
	echo -e "\e[1;32m| NINJA@IP"
	read -p "|- $ " target
	curl -s http://ip-api.com/$target
	echo -e ""
	exit
}
    
menuprincipal() {
    clear
	banner
	echo -e "\e[1;34m[\e[1;37m1\e[1;34m]\e[0m" "\e[36minformación de mi IP\e[0m"
	echo -e "\e[1;34m[\e[1;37m2\e[1;34m]\e[0m" "\e[36mSacar informacion de una IP\e[0m"
	echo -e "\e[1;34m[\e[1;37m3\e[1;34m]\e[0m" "\e[1;31mSalir\e[0m"
    echo -e "\e[1;32m"
	echo -e "Elige entre el 1 2 o 3"
	echo -e ""
	read -p "~$ " opt
	if [ $opt -eq 1 ];
		then
			miIP
	elif [ $opt -eq 2 ];
		then
			tarjetaip                                            

	elif [ $opt -eq 3 ];
		then
			echo -e "\e[1;33mGracias por usar el script "
			exit
	else
		sleep 1
		restartprogram
	fi

}


menuprincipal
