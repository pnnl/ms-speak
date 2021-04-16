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
# NOTE:
#        Wayland is a display server protocol which was introduced as the default in GNOME.
#	It is said that Wayland will eventually replace X11 as the default display 
#	server on Linux and many distributions have begun implementation of Wayland. Wayland is enabled 
#	by default in the GNOME Desktop.
#
#        Gnome 3.22 uses wayland by default, To run the MS-SPEAK apps, set the Qt Platform Abstraction (QPA)
#				export QT_QPA_PLATFORM=wayland  (vs QT_QPA_PLATFORM=xcb)
#		set via /etc/profile.d/qt.qpa.sh
#       Files in /etc/profile.d/ are run when a user logs in (unless you've 
#			modified /etc/profile to not do this) 
#		to see what display server you are using:
#			printf $XDG_SESSION_TYPE
#				x11
#		printf $DESKTOP_SESSION
#			/usr/share/xsessions/cinnamon
#				this does not appear to use wayland...
#
#		to use X11:  ./IdsEditor -platform xcb
#
# return 0 in all cases so as not to abort a wsl session (zero for success).

ORIG_DIR=
NEW_DIR=

if [ $# -ne 0 ]; then
	printf "\nto run Squid use the following command:\n"
	printf "\n     sudo /usr/local/squid/sbin/squid -N -d 1"
	printf "\n  if you see this error:"
	printf "\n      logfileHandleWrite: daemon:/var/logs/access.log: error writing ((32) Broken pipe"
	printf "\n  do the following:"
	printf "\n      add your user to the staff group:"
	printf "\n         sudo usermod -a -G staff yourusername"
	printf "\n            (then shutdown, restart)"
	printf "\n      sudo chmod 777 /usr/local/squid -R"

	printf "\n\nto run c-icap use the following command:"
	printf "\n     sudo /usr/local/bin/c-icap -N -D -d 1"
	printf "\n  if you see this error:"
	printf "\n      /usr/local/bin/c-icap: error while loading shared libraries libicapapi.so.5:"
	printf "\n               cannot open shared object file: No such file or directory"
	printf "\n  do the following:"
	printf "\n      sudo ldconfig"
	printf "\n  then run c-icap again."
	return 0
fi

#		NOTE:  if the icap machine is rebooted, the directories for the icap lock file will no longer exist, 
#		and must be recreated: you may see the following error when starting c-icap:
#			Cannot open the pid file: /var/run/c-icap/c-icap.pid or c-icap.ctl
#										or
#			Error opening control socket No such file or directory: /var/run/c-icap/c-icap.ctl.
#		do:
#			sudo mkdir /var/run/c-icap
#		this happens because /var/run is a tmpfs filesystem, so it
#		is emptied at each boot, to have this directory created after each
#		boot, add a .conf file to /usr/lib/tmpfiles.d:
#			/usr/lib/tmpfiles.d/c-icap.conf with the follow content:
#				d /var/run/c-icap 0755 - - -

# required packages
printf "\nThe Following required packages will now be installed:"
printf "\n    g++, libsqlite3-dev, libxml2-dev, libxml2, uuid-dev, git & libcurl4"
printf "\n\nPress just the [Enter] key to continue with this Installation, or"
printf "\n  else enter 'S' to skip this step, otherwise enter 'N' to terminate completely:\n"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	printf "\nInstallation of Required Packages Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		printf "\nSkipping this step."
	else
		printf "\nInstallation Terminated.\n"
		return 0
	fi
else
	printf "\nInstalling Required Packages..."
	if sudo apt-get install g++; then
		if sudo apt-get install libsqlite3-dev; then
			if sudo apt-get install libxml2; then
				if sudo apt-get install libxml2-dev; then
					if sudo apt-get install uuid-dev; then
						if sudo apt-get install git; then
							if sudo apt-get install libcurl4-openssl-dev; then
								printf "\n\n*** Successfully Installed required packages"
							else
								printf "\nFailed to Install libcurl4, can not continue"
								false
							fi
						else
							printf "\nFailed to Install git, can not continue"
							false
						fi
					else
						printf "\nFailed to Install uuid-dev, can not continue"
						false
					fi
				else
					printf "\nFailed to Install libxml2-dev, can not continue"
					false
				fi
			else
				printf "\nFailed to Install libxml2, can not continue"
				false
			fi
		else
			printf "\nFailed to Install libsqlite3-dev, can not continue"
			false
		fi
	else
		printf "\nFailed to Install g++, can not continue"
		false
	fi
	retval=$?
	if [ $retval -ne 0 ]; then
		printf "\nFailed to Successfully Install all required packages, can not continue\n"
		read -p "Press [Enter] to exit."
		return 0
	fi
fi

ORIG_DIR=$(pwd)
SUBDIR="msspeak"
printf "\nEnter the sub-directory name to install Squid & c-icap to [default: $SUBDIR]:"
printf "\n   NOTE: files will be installed as a sub-directory of the current folder: $(pwd)"
printf "\n  *** WARNING: any existing files in this directory will be deleted. ***\n"
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
printf "\nInstalling to $NEW_DIR"
cd $NEW_DIR
retval=$?
if [ $retval -ne 0 ]; then
	printf "\nFailed to change to $NEW_DIR\n"
	return 0
else
	cd ../
	retval=$?
	if [ $retval -ne 0 ]; then
		printf "\nFailed to change to parent of $NEW_DIR"
		return 0
	fi
fi

#printf "\nPress [Enter] key to continue with the Installation, else 'N' to terminate:\n"
#read DO_INSTALL
#if [ -z "$DO_INSTALL" ]
#then
#	pwd
#	printf "\nCloning repository to" $NEW_DIR
#else
#	printf "\nInstallation Cancelled."
#	return 0
#fi

SKIP=0;
printf "\n\nThe MS-SPEAK source repository will now be cloned to" $NEW_DIR
printf "\n  *** WARNING: any existing files in this directory will be deleted. ***"
printf "\nPress [Enter] to clone, 'S' to skip this step, or 'N' to terminate completely:\n"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	printf "\nCloning of Repository Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		printf "\nSkipping this step."
		SKIP=1;
	else
		printf "\nInstallation Terminated.\n"
		cd $ORIG_DIR
		return 0
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
		printf "\nFailed to clone Install repository, can not continue\n"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return 0
	fi
fi

cd $NEW_DIR/Packages

#Extract Packages:
#printf "\n\nSquid & c-icap will now be extracted to $NEW_DIR/Packages"
#printf "\nPress [Enter] to extract, 'S' to skip this step, or 'N' to terminate completely:\n"
#read DO_INSTALL
#if [ ! -z "$DO_INSTALL" ]; then
#	printf "\nExtraction of Tarballs Cancelled."
#	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
#		printf "\nSkipping this step."
#	else
#		printf "\nInstallation Terminated.\n"
#		cd $ORIG_DIR
#		return 0
#	fi
#else
if [ $SKIP -eq 0 ]; then
	if tar xzf install/squid/squid-4.7.tar.gz; then
		mv squid-4.7-20190507-r2e17b0261 squid-4.7
		if tar xzf install/c_icap/c_icap-0.5.5.tar.gz; then
			printf "\nPackages Extracted Successfully.."
		else
			printf "\nFailed to extract i-cap Package, can not continue\n"
			read -p "Press [Enter] to exit."
			cd $ORIG_DIR
			return 0
		fi
	else
		printf "\nFailed to extract Squid Package, can not continue\n"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return 0
	fi
fi
#fi

#SQUID:
printf "\n\nSquid will now be installed to $NEW_DIR/Packages"
printf "\n     (this typically takes 20 to 30 minutes to complete)"
printf "\nPress [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:\n"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	printf "\nInstallation of Squid Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		printf "\nSkipping this step.\n"
	else
		printf "\nInstallation Terminated.\n"
		cd $ORIG_DIR
		return 0
	fi
else
	cd squid-4.7
	if ./configure; then
		if make; then
			if sudo make install; then
				cd ../
				if sudo cp install/squid/squid.conf /usr/local/squid/etc/; then
					sudo chmod 777 /usr/local/squid -R
					printf "\nSquid Installed Successfully."
				else
					printf "\nFailed to copy squid.conf to local directory."
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
		printf "\nFailed to Successfully Install Squid, can not continue"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return 0
	fi
fi

#c-icap config:
printf "\n\nc-icap will now be installed to $NEW_DIR/Packages"
printf "\nPress [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:\n"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	printf "\nInstallation of c-icap Cancelled."
	if [ "$DO_INSTALL" = "S" ] || [ "$DO_INSTALL" = "s" ]; then
		printf "\nSkipping this step.\n"
	else
		printf "\nInstallation Terminated.\n"
		cd $ORIG_DIR
		return 0
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
		printf "\nFailed to successfully copy c-icap configuration files, can not continue\n"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return 0
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
						if sudo mkdir -p /usr/local/share/c_icap/templates/msp/en; then
							if sudo cp install/c_icap/services/msp/MSP_RESPONSE /usr/local/share/c_icap/templates/msp/en; then
								sudo cp install/c_icap/c-icap.conf /usr/local/etc
								sudo cp install/c-icap.conf.tmpf /usr/lib/tmpfiles.d/c-icap.conf
								sudo cp install/BizRules.db $NEW_DIR
								sudo mkdir -p /var/run/c-icap
								if sudo ln -s $NEW_DIR /home/msspeak; then
									#sudo cp install/qt.qpa.sh /etc/profile.d
									echo '/home/msspeak link created.'
								else
									echo '/home/msspeak link could not be made.'
								fi
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
		printf "\nFailed to Successfully Install c-icap, can not continue\n"
		read -p "Press [Enter] to exit."
		cd $ORIG_DIR
		return 0
	else
		printf "\nc-icap Installed Successfully."
		sudo ldconfig
	fi
fi
# export QT_QPA_PLATFORM=wayland  this only appiles to the current cmd window
echo "export QT_QPA_PLATFORM=wayland" >> ~/.bashrc
echo "alias RuleEdit='~/msspeak/Install/run/IdsEditor 2>/dev/null'" >> ~/.bashrc
echo "alias sqid='sudo /usr/local/squid/sbin/squid -N -d'" >> ~/.bashrc
echo "alias cap='sudo /usr/local/bin/c-icap -N -D -d'" >> ~/.bashrc
# sudo echo "msuser     ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# source is a command implemented in bash, but not in sh, so
# Use dot command to make script bourne compatible
# still does not work
#  . ~/.bashrc

printf "\n\n*** Installation Completed Successfully."
printf "\nto run squid use the following command:"
printf "\n     sudo /usr/local/squid/sbin/squid -N -d 1"
printf "\nto run c-icap use the following command:"
printf "\n     sudo /usr/local/bin/c-icap -N -D -d 1"
printf "\n\nFor help with these commands, run this script with the '-h' option:"
printf "\n   . mspInstall.sh -h\n"
cd $ORIG_DIR
return 0
# cd /usr/local/bin
# sudo ln -s /home/carl/mspInstall/msspeak /home/msspeak
# sudo ln -s $NEW_DIR /home/msspeak
