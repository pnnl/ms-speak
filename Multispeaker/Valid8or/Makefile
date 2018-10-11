#   add to eclipse -
#      project-->propertie->java build path-->libraries, add external JARS
#   jar cvf lib/valid.jar -C bin/valid .
#    run:  java -cp lib/Valid8.jar:lib/commons-cli-1.3.1.jar JRun
#				-sd "/home/carl/Desktop/MS-SPEAK/V507/XSDS/EndPoints/"
#				-ep "CD_Server"
#				-xf "/home/carl/Desktop/MS-SPEAK/files/InitCDReq.xml"
#    run:  java -cp "lib/*" JRun

# note: The $1.class files are anonymous inner classes
all: compile

# the following JValid and JParseSoap probably not needed, they seem
# to get built automatically due to their references inside JRun

bin/JRun.class: JRun.java bin/JValid.class
	javac JRun.java -d bin -classpath bin:lib/commons-cli-1.3.1.jar
	jar cvf lib/Valid8.jar -C bin .
	cp lib/*.jar /home/carl/MS-SPEAK/repo/Multispeaker/Debug/run
	
bin/JValid.class: JValid.java  bin/JParseSOAP.class
	javac JValid.java -d bin

bin/JParseSOAP.class: JParseSOAP.java bin/JReturn.class
	javac JParseSOAP.java -d bin

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
