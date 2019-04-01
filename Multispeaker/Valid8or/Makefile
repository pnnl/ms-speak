# PowerShell:
#	 Get-ChildItem Env:
#	 Get-ChildItem Env:PATH
#		or just:  $env:Path
#	 Get-ChildItem Env:JAVA_HOME
#		or just $env:java_home
#	 Get-ChildItem Env:JAVA_HOME_8  - C:\Program Files\Java\jdk1.8.0_192
#	 Get-ChildItem Env:JAVA_HOME_11
#
#	[Environment]::SetEnvironmentVariable("JAVA_HOME", "$($Env:JAVA_HOME_8)")
#	[Environment]::SetEnvironmentVariable("JAVA_HOME", "$($Env:JAVA_HOME_11)")
#	[Environment]::SetEnvironmentVariable("PATH", "$($Env:JAVA_HOME)\bin;" + $Env:Path )
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
#	sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/java-7-openjdk-amd64/bin/jar 0
#	sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-7-openjdk-amd64/bin/javac 0
#	sudo update-alternatives --set jar /usr/lib/jvm/java-7-openjdk-amd64/bin/jar
#	sudo update-alternatives --set javac /usr/lib/jvm/java-7-openjdk-amd64/bin/javac
#				or
#	sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/java-8-openjdk-amd64/bin/jar 0
#	sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac 0
#	sudo update-alternatives --set jar /usr/lib/jvm/java-8-openjdk-amd64/bin/jar
#	sudo update-alternatives --set javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac
#
#	java -version
#
#   add to eclipse -
#      project-->properties->java build path-->libraries, add external JARS
#   jar cvf lib/valid.jar -C bin/valid .
#	set CLASSPATH="lib/*;bin"
#   run:   java -cp "lib/*;bin" JRun 
#	 	-sd C:/Users/D3M907/Documents/projects/MS-Speak/multispeaker/multispeaker/WSDLs/EndPoints
#	 	-ep CD_Server
#	 	-xf C:/Users/D3M907/Documents/projects/MS-Speak/multispeaker/multispeaker/WSDLs/LancesCD.xml
#	 	-v 3 
#	  
#	 	-sd /home/carl/Desktop/MS-SPEAK/Multispeaker/WSDLs/EndPoints
#	 	-ep CD_Server
#	 	-xf /home/carl/Desktop/MS-SPEAK/Multispeaker/WSDLs/LancesCD.xml
#	 	-v 3
#
# java -cp "lib/*" JRun -sd /home/carl/Desktop/MS-SPEAK/Multispeaker/WSDLs/EndPoints -ep CD_Server -xf /home/carl/Desktop/MS-SPEAK/Multispeaker/WSDLs/LancesCD.xml -v 3
#
# note: The $1.class files are anonymous inner classes
# build on windoze, in a powershell window:
# 	cd C:\Users\D3M907\Documents\projects\MS-Speak\multispeaker\multispeaker\Valid8or
#		javac -cp "lib/*;bin" JReturn.java -d bin
#		NOTE:
#			javac -cp "lib/*;bin" JParseSOAP.java -d bin
#				does not build under javac 11.0.1 with only commons-cli-1.3.1.jar in ../lib/*
#					on windows (C:\Program Files\Java\jdk-11.0.1)
#			use JAVA_HOME_8
#			Also, it does not compile on linux with javac 11.0.1, but does with javac 1.7.0_121 or javac 1.8.0_181
#			
#		javac -cp "lib/*;bin" JValid.java -d bin
#		javac -cp "lib/*;bin" JRun.java -d bin
#		jar cvf lib/Valid8.jar -C bin .
#
#   NOTE: use lib/* not lib/*.jar
#   NOTE: for linux	NOTE use of COLON, NOT COMMA or SEMICOLON....
#			javac JRun.java -d bin -classpath bin:lib/commons-cli-1.3.1.jar
#
all: compile

# the following JValid and JParseSoap probably not needed, they seem
# to get built automatically due to their references inside JRun

bin/JRun.class: JRun.java bin/JValid.class
	javac JRun.java -d bin -classpath bin:lib/commons-cli-1.3.1.jar
	jar cvf lib/Valid8.jar -C bin .
	cp lib/*.jar /home/carl/MS-SPEAK/repo/Multispeaker/Debug/run
	
bin/JValid.class: JValid.java  bin/JParseSOAP.class
	javac JValid.java -d bin -classpath bin

bin/JParseSOAP.class: JParseSOAP.java bin/JReturn.class
	javac JParseSOAP.java -cp bin:lib/*.jar -d bin

bin/JReturn.class: JReturn.java
	javac JReturn.java -d bin

compile: bin/JRun.class .
	@echo Run::java -cp "lib/*" JRun
	@echo '          -sd /home/carl/Desktop/MS-SPEAK/V507/XSDS/EndPoints/'
	@echo '          -ep CD_Server'
	@echo '          -xf /home/carl/Desktop/MS-SPEAK/files/InitCDReq.xml'
	@echo '          -v 3'
clean:
	rm -f bin/* 
