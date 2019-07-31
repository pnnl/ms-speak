#!/bin/bash

# required packages
echo "The Following Packages are required and will now be installed:"
echo "    libglib2.0-dev, libxml2-dev, libxml2 & uuid-dev"
echo "Press just the [Enter] key to continue with this Installation, enter 'S' to skip this step, else enter 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Installation of Required Packages Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo "Skipping this step."
	else
		echo "Terminating Installation."
		return -1
	fi
else
	echo "Installing Required Packages..."
	if sudo apt-get install libglib2.0-dev; then
		if sudo apt-get install libxml2; then
			if sudo apt-get install libxml2-dev; then
				if sudo apt-get install uuid-dev; then
					echo "Successfully Installed required packages"
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
		echo "Failed to Install libglib2.0-dev, can not continue"
		false
	fi
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to Successfully Install all required packages, can not continue"
		read -p "Press [Enter] key to terminate."
		popd
		return 1
	fi
fi

echo "Enter the directory name to install Squid & c-icap to [default: /home/msspeak]:"
read NEW_DIR
ORIG_DIR=$(pwd)

if [ -z "$NEW_DIR" ]; then
	#echo "\$NEW_DIR is empty, setting to /home/msspeak"
	NEW_DIR="/home/msspeak"
#else
#	echo "\$$NEW_DIR is NOT empty"
fi

if [ ! -d "$NEW_DIR" ]; then
	#echo $NEW_DIR does NOT exist yet.
	mkdir -p $NEW_DIR
#else
#	echo $NEW_DIR already exists.
fi
pushd .
echo "Installing to $NEW_DIR"
cd $NEW_DIR
retval=$?
if [ $retval -ne 0 ]; then
	echo "Failed to change to $NEW_DIR"
	popd
	return -1
else
	cd ../
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to change to parent of $NEW_DIR"
		popd
		return -1
	fi
fi

echo "Press [Enter] key to continue with the Installation, else 'N' to terminate:"
read DO_INSTALL
if [ -z "$DO_INSTALL" ]
then
	pwd
	echo "Cloning repository to" $NEW_DIR
else
	echo "Installation Cancelled."
	popd
	return -1
fi

echo "The MS-SPEAK source repository will now be cloned to" $NEW_DIR
echo "Press [Enter] to clone, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Cloning of Repository Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo "Skipping this step."
	else
		echo "Terminating Installation."
		return -1
	fi
else
	git clone --branch Install https://github.com/pnnl/ms-speak $NEW_DIR
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to clone Install repository, can not continue"
		read -p "Press [Enter] key to terminate."
		popd
		return -1
	fi
fi

cd $NEW_DIR/Packages

#Extract Packages:
echo "Squid & c-icap will now be extracted to $NEW_DIR/Packages"
echo "Press [Enter] to extract, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Extraction of Tarballs Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo "Skipping this step."
	else
		echo "Terminating Installation."
		return -1
	fi
else
	if tar xzf install/squid/squid-4.7.tar.gz; then
		mv squid-4.7-20190507-r2e17b0261 squid-4.7
		if tar xzf install/c_icap/c_icap-0.5.5.tar.gz; then
			echo "Packages Extracted Successfully.."
		else
			echo "Failed to extract i-cap Package, can not continue"
			read -p "Press [Enter] key to terminate."
			popd
			return -1
		fi
	else
		echo "Failed to extract Squid Package, can not continue"
		read -p "Press [Enter] key to terminate."
		popd
		return -1
	fi
fi

#SQUID:
echo "Squid will now be installed to $NEW_DIR/Packages"
echo "Press [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Installation of Squid Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo "Skipping this step."
	else
		echo "Terminating Installation."
		return -1
	fi
else
	cd squid-4.7
	if ./configure; then
		if make; then
			if sudo make install; then
				if sudo cp install/squid/squid.conf /usr/local/squid/etc/; then
					echo "Squid Installed Successfully."
				else
					echo "Failed to copy squid.conf to local directory."
					false # this should set $? to 1
			fi
		fi
	fi
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to Successfully Install Squid, can not continue"
		read -p "Press [Enter] key to terminate."
		popd
		return -1
	fi
fi

#c-icap config:
echo "c-icap will now be installed to $NEW_DIR/Packages"
echo "Press [Enter] to install, 'S' to skip this step, or 'N' to terminate completely:"
read DO_INSTALL
if [ ! -z "$DO_INSTALL" ]; then
	echo "Installation of c-icap Cancelled."
	if [ "$DO_INSTALL" == "S" ] || [ "$DO_INSTALL" == "s" ]; then
		echo "Skipping this step."
	else
		echo "Terminating Installation."
		return -1
	fi
else
	if cd /home/$NEW_DIR/Packages; then
		if cp install/c_icap/configure c_icap-0.5.5; then
			if cp install/c_icap/c-icap.conf.in c_icap-0.5.5; then
				if mkdir c_icap-0.5.5/services/msp; then
					if cp -r install/c_icap/services/msp/* c_icap-0.5.5/services/msp; then
						if cp install/c_icap/services/Makefile.am c_icap-0.5.5/services/Makefile.am; then
							cp install/c_icap/services/Makefile.in c_icap-0.5.5/services/Makefile.in
						fi
					fi
				fi
			fi
		fi
	fi
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to successfully copy c-icap configuration files, can not continue"
		read -p "Press [Enter] key to terminate."
		popd
		return -1
	fi

	#c-icap make
	if cd c_icap-0.5.5; then
		if ./configure; then
			if make; then
				if sudo make install; then
					if sudo mkdir /usr/local/share/c_icap/templates/msp; then
						if sudo mkdir /usr/local/share/c_icap/templates/msp/en	; then		
							sudo cp install/c_icap/services/msp/MSP_RESPONSE /usr/local/share/c_icap/templates/msp/en
						fi
					fi
				fi
			fi
		fi
	fi
	retval=$?
	if [ $retval -ne 0 ]; then
		echo "Failed to Successfully Install c-icap, can not continue"
		read -p "Press [Enter] key to terminate."
		popd
		return -1
	else
		echo "c-icap Installed Successfully."
	fi
fi
popd

echo "Installation Completed Successfully."

return 0
