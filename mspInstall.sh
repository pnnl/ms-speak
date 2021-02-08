#!/bin/sh -e
#   -x runs in debug mode, -e exits if any command fails
#  retrieve this file from the repository:
#		wget https://raw.githubusercontent.com/pnnl/ms-speak/Phase2/Multispeaker/mspInstall.sh
#
#	if ERROR: The certificate of ‘raw.githubusercontent.com’ is not trusted.
#	   ERROR: The certificate of ‘raw.githubusercontent.com’ hasn't got a known issuer.
#			If you are using Debian or Ubuntu operating system please install the package
#   			sudo apt-get install ca-certificates
#
ORIG_DIR=
NEW_DIR=

if [ $# -ne 0 ]; then
	echo -e "to run Squid use the following command:"
	echo -e "     sudo /usr/local/squid/sbin/squid -N -d 1"
	echo -e "  if you see this error:"
	echo -e "      logfileHandleWrite: daemon:/var/logs/access.log: error writing ((32) Broken pipe"
	echo -e "  do the following:"
	echo -e "      add your user to the staff group:"
	echo -e "         sudo usermod -a -G staff yourusername"
	echo -e "            (then shutdown, restart)"
	echo -e "      sudo chmod 777 /usr/local/squid -R"
	
	echo -e "\nto run c-icap use the following command:"
	echo -e "     sudo /usr/local/bin/c-icap -N -D -d 1"
	echo -e "  if you see this error:"
	echo -e "      /usr/local/bin/c-icap: error while loading shared libraries libicapapi.so.5:"
	echo -e "               cannot open shared object file: No such file or directory"
	echo -e "  do the following:"
	echo -e "      sudo ldconfig"
	echo -e "  then run c-icap again."
	return 0
fi

# required packages
echo -e "The Following required packages will now be installed:"
echo -e "    g++, libglib2.0-dev, libxml2-dev, libxml2 & uuid-dev git"
echo -e "\nPress just the [Enter] key to continue with this Installation, or"
echo -e "  else enter 'S' to skip this step, otherwise enter 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo -e "Installation of Required Packages Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo -e "Skipping this step."
	else
		echo -e "Installation Terminated.\n"
		return -1
	fi
else
	echo -e "Installing Required Packages..."
	if sudo apt-get install g++; then
		if sudo apt-get install libglib2.0-dev; then
			if sudo apt-get install libxml2; then
				if sudo apt-get install libxml2-dev; then
					if sudo apt-get install uuid-dev; then
						if sudo apt-get install git; then
							echo -e "\n*** Successfully Installed required packages"
						else
							echo -e "Failed to Install git, can not continue"
							false
						fi
					else
						echo -e "Failed to Install uuid-dev, can not continue"
						false
					fi
				else
					echo -e "Failed to Install libxml2-dev, can not continue"
					false
				fi
			else
				echo -e "Failed to Install libxml2, can not continue"
				false
			fi
		else
			echo -e "Failed to Install libglib2.0-dev, can not continue"
			false
		fi
	else
		echo -e "Failed to Install g++, can not continue"
		false
	fi
	retval=$?
	if [ $retval -ne 0 ]; then
		echo -e "Failed to Successfully Install all required packages, can not continue"
		read -p "Press [Enter] to exit."
		return 1
	fi
fi

ORIG_DIR=$(pwd)
SUBDIR="msspeak"
echo "Enter the sub-directory name to install Squid & c-icap to [default: $SUBDIR]:"
echo "   NOTE: files will be installed as a sub-directory of the current folder: $(pwd)"
echo "  *** WARNING: any existing files in this directory will be deleted. ***"
read SUBDIR
if [ -z "$SUBDIR" ]; then
	SUBDIR="msspeak"
fi
NEW_DIR="$(pwd)/msspeak"
#NEW_DIR="/home/msspeak"

if [ ! -d "$NEW_DIR" ]; then
	mkdir -p $NEW_DIR
fi
#
echo -e "Installing to $NEW_DIR"
cd $NEW_DIR
retval=$?
if [ $retval -ne 0 ]; then
	echo -e "Failed to change to $NEW_DIR"
	return -1
else
	cd ../
	retval=$?
	if [ $retval -ne 0 ]; then
		echo -e "Failed to change to parent of $NEW_DIR"
		return -1
	fi
fi

#echo -e "Press [Enter] key to continue with the Installation, else 'N' to terminate:"
#read DO_INSTALL
#if [ -z "$DO_INSTALL" ]
#then
#	pwd
#	echo -e "Cloning repository to" $NEW_DIR
#else
#	echo -e "Installation Cancelled."
#	return -1
#fi

SKIP=0;
echo -e "\nThe MS-SPEAK source repository will now be cloned to" $NEW_DIR
echo "  *** WARNING: any existing files in this directory will be deleted. ***"
echo -e "Press [Enter] to clone, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo -e "Cloning of Repository Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo -e "Skipping this step."
		SKIP=1;
	else
		echo -e "Installation Terminated.\n"
		cd $ORIG_DIR
		return -1
	fi
else
	if [ ! -d "$NEW_DIR" ]; then
		mkdir -p $NEW_DIR
	else
		sudo rm -rf $NEW_DIR
		mkdir -p $NEW_DIR
	fi
	cd $NEW_DIR
	cd ../
	git clone --branch Install https://github.com/pnnl/ms-speak $NEW_DIR
	retval=$?
	if [ $retval -ne 0 ]; then
		echo -e "Failed to clone Install repository, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	fi
fi

cd $NEW_DIR/Packages

#Extract Packages:
#echo -e "\nSquid & c-icap will now be extracted to $NEW_DIR/Packages"
#echo -e "Press [Enter] to extract, 'S' to skip this step, or 'N' to terminate completely:"
#read DO_INSTALL
#if [ ! -z "$DO_INSTALL" ]; then
#	echo -e "Extraction of Tarballs Cancelled."
#	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
#		echo -e "Skipping this step."
#	else
#		echo -e "Installation Terminated.\n"
#		cd $ORIG_DIR
#		return -1
#	fi
#else
if [ $SKIP -eq 0 ]; then
	if tar xzf install/squid/squid-4.7.tar.gz; then
		mv squid-4.7-20190507-r2e17b0261 squid-4.7
		if tar xzf install/c_icap/c_icap-0.5.5.tar.gz; then
			echo -e "Packages Extracted Successfully.."
		else
			echo -e "Failed to extract i-cap Package, can not continue"
			read -p "Press [Enter] to exit."
			cd $ORIG_DIR
			return -1
		fi
	else
		echo -e "Failed to extract Squid Package, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	fi
fi
#fi

#SQUID:
echo -e "\nSquid will now be installed to $NEW_DIR/Packages"
echo -e "     (this typically takes 20 to 30 minutes to complete)"
echo -e "Press [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo -e "Installation of Squid Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo -e "Skipping this step."
	else
		echo -e "Installation Terminated.\n"
		cd $ORIG_DIR
		return -1
	fi
else
	cd squid-4.7
	if ./configure; then
		if make; then
			if sudo make install; then
				cd ../
				if sudo cp install/squid/squid.conf /usr/local/squid/etc/; then
					sudo chmod 777 /usr/local/squid -R
					echo -e "Squid Installed Successfully."
				else
					echo -e "Failed to copy squid.conf to local directory."
					false # this should set $? to 1
				fi
			else
				retval=$?
			fi
		else
			retval=$?
		fi
	else
		retval=1
	fi
	#retval=$?
	if [ $retval -ne 0 ]; then
		echo -e "Failed to Successfully Install Squid, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	fi
fi

#c-icap config:
echo -e "\nc-icap will now be installed to $NEW_DIR/Packages"
echo -e "Press [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo -e "Installation of c-icap Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo -e "Skipping this step."
	else
		echo -e "Installation Terminated.\n"
		cd $ORIG_DIR
		return -1
	fi
else
	if cd $NEW_DIR/Packages; then
		if cp install/c_icap/configure c_icap-0.5.5; then
			if cp install/c_icap/c-icap.conf.in c_icap-0.5.5; then
				mkdir -p c_icap-0.5.5/services/msp
				if cp -r install/c_icap/services/msp/* c_icap-0.5.5/services/msp; then
					if cp install/c_icap/services/Makefile.am c_icap-0.5.5/services/Makefile.am; then
						cp install/c_icap/services/Makefile.in c_icap-0.5.5/services/Makefile.in
						retval=$?
					else
						retval=$?
					fi
				else
					retval=$?
				fi
			else
				retval=$?
			fi
		else
			retval=$?
		fi
	else
		retval=$?
	fi
	if [ $retval -ne 0 ]; then
		echo -e "Failed to successfully copy c-icap configuration files, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	fi

	#c-icap make
	if cd c_icap-0.5.5; then
		if ./configure; then
			if make; then
				if sudo make install; then
					cd ../
					sudo mkdir -p /usr/local/share/c_icap
					sudo mkdir -p /usr/local/share/c_icap/templates
					if sudo mkdir -p /usr/local/share/c_icap/templates/msp; then
						if sudo mkdir -p /usr/local/share/c_icap/templates/msp/en	; then		
							if sudo cp install/c_icap/services/msp/MSP_RESPONSE /usr/local/share/c_icap/templates/msp/en; then
								sudo cp install/c_icap/c-icap.conf /usr/local/etc
								sudo cp install/BizRules.cfg $NEW_DIR
								sudo mkdir -p /var/run/c-icap
								sudo ln -s $NEW_DIR /home/msspeak
								retval=$?
							else
								retval=$?
							fi
						else
							retval=$?
						fi
					else
						retval=$?
					fi
				else
					retval=$?
				fi
			else
				retval=$?
			fi
		else
			retval=$?
		fi
	else
		retval=$?
	fi
	if [ $retval -ne 0 ]; then
		echo -e "Failed to Successfully Install c-icap, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	else
		echo -e "c-icap Installed Successfully."
		sudo ldconfig
	fi
fi

echo -e "\n*** Installation Completed Successfully."
echo -e "to run squid use the following command:"
echo -e "     sudo /usr/local/squid/sbin/squid -N -d 1"
echo -e "to run c-icap use the following command:"
echo -e "     sudo /usr/local/bin/c-icap -N -D -d 1"
echo -e "\nFor help with these commands, run this script with the '-h' option:"
echo -e "   . mspInstall.sh -h\n"
cd $ORIG_DIR
return 0
# cd /usr/local/bin
# sudo ln -s /home/carl/mspInstall/msspeak /home/msspeak
# sudo ln -s $NEW_DIR /home/msspeak

	
	
	
	
	
	
	
	
	