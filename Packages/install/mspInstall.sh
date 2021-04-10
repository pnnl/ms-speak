#!/bin/sh
set -e

# dash(Debian Almquist shell) is a POSIX-compliant implementation of /bin/sh
# this script works under bash but not dash
# The problem is the unexpected operator. That is referring to the = which is non-POSIX. 
#	use = instead of = in comparison
#
#   -x runs in debug mode,
#		print everything as if it were executed, after substitution and expansion is applied
#		indicate the depth-level of the subshell (by default by prefixing a + (plus) sign to the displayed command)
# -e exits if any command fails
#
#  retrieve this file from the repository:
#		wget https://raw.githubusercontent.com/pnnl/ms-speak/Phase3/Multispeaker/mspInstall.sh
#
#	if ERROR: The certificate of ‘raw.githubusercontent.com’ is not trusted.
#	   ERROR: The certificate of ‘raw.githubusercontent.com’ hasn't got a known issuer.
#			If you are using Debian or Ubuntu operating system please install the package
#   			sudo apt-get install ca-certificates
# RUN:
#     cd ~
#     . mspInstall
#

ORIG_DIR=
NEW_DIR=

if [ $# -ne 0 ]; then
	echo "to run Squid use the following command:"
	echo "     sudo /usr/local/squid/sbin/squid -N -d 1"
	echo "  if you see this error:"
	echo "      logfileHandleWrite: daemon:/var/logs/access.log: error writing ((32) Broken pipe"
	echo "  do the following:"
	echo "      add your user to the staff group:"
	echo "         sudo usermod -a -G staff yourusername"
	echo "            (then shutdown, restart)"
	echo "      sudo chmod 777 /usr/local/squid -R"
	
	echo "\nto run c-icap use the following command:"
	echo "     sudo /usr/local/bin/c-icap -N -D -d 1"
	echo "  if you see this error:"
	echo "      /usr/local/bin/c-icap: error while loading shared libraries libicapapi.so.5:"
	echo "               cannot open shared object file: No such file or directory"
	echo "  do the following:"
	echo "      sudo ldconfig"
	echo "  then run c-icap again."
	return 0
fi

# required packages
echo "The Following required packages will now be installed:"
echo "    g++, libsqlite3-dev, libxml2-dev, libxml2, uuid-dev, git & libcurl4"
echo "\nPress just the [Enter] key to continue with this Installation, or"
echo "  else enter 'S' to skip this step, otherwise enter 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Installation of Required Packages Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		echo "Skipping this step."
	else
		echo "Installation Terminated.\n"
		return -1
	fi
else
	echo "Installing Required Packages..."
	if sudo apt-get install g++; then
		if sudo apt-get install libsqlite3-dev; then
			if sudo apt-get install libxml2; then
				if sudo apt-get install libxml2-dev; then
					if sudo apt-get install uuid-dev; then
						if sudo apt-get install git; then
							if sudo apt-get install libcurl4-openssl-dev; then
								echo "\n*** Successfully Installed required packages"
							else
								echo "Failed to Install libcurl4, can not continue"
								false
							fi
						else
							echo "Failed to Install git, can not continue"
							false
						fi
					else
						echo "Failed to Install uuid-dev, can not continue"
						false
					fi
				else
					echo "Failed to Install libxml2-dev, can not continue"
					false
				fi
			else
				echo "Failed to Install libxml2, can not continue"
				false
			fi
		else
			echo "Failed to Install libsqlite3-dev, can not continue"
			false
		fi
	else
		echo "Failed to Install g++, can not continue"
		false
	fi
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to Successfully Install all required packages, can not continue"
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
echo "Installing to $NEW_DIR"
cd $NEW_DIR
retval=$?
if [ $retval -ne 0 ]; then
	echo "Failed to change to $NEW_DIR"
	return -1
else
	cd ../
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to change to parent of $NEW_DIR"
		return -1
	fi
fi

#echo "Press [Enter] key to continue with the Installation, else 'N' to terminate:"
#read DO_INSTALL
#if [ -z "$DO_INSTALL" ]
#then
#	pwd
#	echo "Cloning repository to" $NEW_DIR
#else
#	echo "Installation Cancelled."
#	return -1
#fi

SKIP=0;
echo "\nThe MS-SPEAK source repository will now be cloned to" $NEW_DIR
echo "  *** WARNING: any existing files in this directory will be deleted. ***"
echo "Press [Enter] to clone, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Cloning of Repository Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		echo "Skipping this step."
		SKIP=1;
	else
		echo "Installation Terminated.\n"
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
		echo "Failed to clone Install repository, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	fi
fi

cd $NEW_DIR/Packages

#Extract Packages:
#echo "\nSquid & c-icap will now be extracted to $NEW_DIR/Packages"
#echo "Press [Enter] to extract, 'S' to skip this step, or 'N' to terminate completely:"
#read DO_INSTALL
#if [ ! -z "$DO_INSTALL" ]; then
#	echo "Extraction of Tarballs Cancelled."
#	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
#		echo "Skipping this step."
#	else
#		echo "Installation Terminated.\n"
#		cd $ORIG_DIR
#		return -1
#	fi
#else
if [ $SKIP -eq 0 ]; then
	if tar xzf install/squid/squid-4.7.tar.gz; then
		mv squid-4.7-20190507-r2e17b0261 squid-4.7
		if tar xzf install/c_icap/c_icap-0.5.5.tar.gz; then
			echo "Packages Extracted Successfully.."
		else
			echo "Failed to extract i-cap Package, can not continue"
			read -p "Press [Enter] to exit."
			cd $ORIG_DIR
			return -1
		fi
	else
		echo "Failed to extract Squid Package, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	fi
fi
#fi

#SQUID:
echo "\nSquid will now be installed to $NEW_DIR/Packages"
echo "     (this typically takes 20 to 30 minutes to complete)"
echo "Press [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Installation of Squid Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		echo "Skipping this step."
	else
		echo "Installation Terminated.\n"
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
					echo "Squid Installed Successfully."
				else
					echo "Failed to copy squid.conf to local directory."
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
		echo "Failed to Successfully Install Squid, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	fi
fi

#c-icap config:
echo "\nc-icap will now be installed to $NEW_DIR/Packages"
echo "Press [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Installation of c-icap Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		echo "Skipping this step."
	else
		echo "Installation Terminated.\n"
		cd $ORIG_DIR
		return -1
	fi
else
	if cd $NEW_DIR/Packages; then
		if cp install/c_icap/configure c_icap-0.5.5; then
			if cp install/c_icap/c-icap.conf.in c_icap-0.5.5; then
				if cp install/c_icap/configure.ac c_icap-0.5.5; then
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
	else
		retval=$?
	fi
	if [ $retval -ne 0 ]; then
		echo "Failed to successfully copy c-icap configuration files, can not continue"
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
								sudo cp install/BizRules.db $NEW_DIR
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
		echo "Failed to Successfully Install c-icap, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return -1
	else
		echo "c-icap Installed Successfully."
		sudo ldconfig
	fi
fi

echo "\n*** Installation Completed Successfully."
echo "to run squid use the following command:"
echo "     sudo /usr/local/squid/sbin/squid -N -d 1"
echo "to run c-icap use the following command:"
echo "     sudo /usr/local/bin/c-icap -N -D -d 1"
echo "\nFor help with these commands, run this script with the '-h' option:"
echo "   . mspInstall.sh -h\n"
cd $ORIG_DIR
return 0
# cd /usr/local/bin
# sudo ln -s /home/carl/mspInstall/msspeak /home/msspeak
# sudo ln -s $NEW_DIR /home/msspeak
