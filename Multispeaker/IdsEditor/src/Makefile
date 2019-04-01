# PowerShell:
#	 Get-ChildItem Env:
#	 Get-ChildItem Env:PATH
#		or just:  $env:Path
#	 Get-ChildItem Env:JAVA_HOME
#		or just $env:java_home
#	 Get-ChildItem Env:JAVA_HOME_8
#	 Get-ChildItem Env:JAVA_HOME_11
#
#	[Environment]::SetEnvironmentVariable("JAVA_HOME", "$($Env:JAVA_HOME_11)")
#	[Environment]::SetEnvironmentVariable("PATH", "$($Env:JAVA_HOME)\bin;" + $Env:Path )
#	NOTE: the above settings only remain in effect in the current PowerShell window
#			to permanently change JAVA_HOME, you need to set it via system path in control panel
#
#   Verify Java Version	
#	java -version
#	javac -version
#	whereis java
#	whereis javac
#	echo $JAVA_HOME
#	which javac ; returns the pathnames of the file which would be executed in the current environment
#
#	sudo update-alternatives --config java	
#		
#	According to the generated screenshot, there may be other versions installed. 
#	Enter the number of desired version.
#
#	There are some other binaries to set as default for JDK installation. Execute the commands to set javac and jar as default:
#	sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/jdk-11.0.1/bin/jar 2
#	sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-11.0.1/bin/javac 2
#	sudo update-alternatives --set jar /usr/lib/jvm/jdk-11.0.1/bin/jar
#	sudo update-alternatives --set javac /usr/lib/jvm/jdk-11.0.1/bin/javac
#				or
#	sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/java-8-openjdk-amd64/bin/jar 0
#	sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac 0
#	sudo update-alternatives --set jar /usr/lib/jvm/java-8-openjdk-amd64/bin/jar
#	sudo update-alternatives --set javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac
#
#	java -version
#
#	Using a JavaFX distribution pre-built from OpenJDK sources
#
#	As noted in comments to this question and in another answer, the Debian Linux distributions offer 
#	a JavaFX binary distibution based upon OpenJDK:
#
#	https://packages.qa.debian.org/o/openjfx.html
#	Install via:
#
#	sudo apt-get install openjfx
#
#
#   add to eclipse -
#      project-->properties->java build path-->libraries, add external JARS
#      set CLASSPATH="../bin"
#      run:   java -cp "../bin;../lib/ini4j-0.5.4.jar" IdsEditor 
#
#   NOTE: use lib/* not lib/*.jar
#   NOTE: for linux	NOTE use of COLON, NOT COMMA or SEMICOLON....
#		  for windoze (from IdsEditor):
#				javac src/IdsEditor.java -d bin -classpath "bin;lib/ini4j-0.5.4.jar"
#				java -cp "bin;lib/ini4j-0.5.4.jar" IdsEditor
#
#   USE JAVA_HOME_11, ESPECIALLY ON WINDOWS, OR ELSE THE APP WILL BE UNREADABLY
#		SMALL ON HIGH DENSITY DISPLAYS
#
all: compile

../bin/IdsEditor.class: IdsEditor.java
	javac IdsEditor.java -d ../bin -classpath ../bin:../lib/ini4j-0.5.4.jar

compile: ../bin/IdsEditor.class .
	@echo Run::java -cp "../bin:../lib/ini4j-0.5.4.jar" IdsEditor
	
run: compile
	java -cp "../bin:../lib/ini4j-0.5.4.jar" IdsEditor 

clean:
	rm -f ../bin/* 
