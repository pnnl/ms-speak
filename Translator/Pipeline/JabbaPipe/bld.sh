#
# -g:{keyword list}
# 	Generate only some kinds of debugging information, specified by a comma separated list of keywords. 
# 	Valid keywords are:
# 		source - Source file debugging information
# 		lines  - Line number debugging information
# 		vars   - Local variable debugging informatio
#
javac src/JValid.java src/JParseSOAP.java -d bin/valid
jar cvf lib/valid.jar -C bin/valid .
#rm bin/valid/*
rm -R bin/*.class

javac -g:{source,lines,vars} -classpath .:./lib/commons-cli-1.3.1.jar:./lib/saxonsa.jar:./lib/XMLConverters.jar:./bin:./lib/valid.jar src/JabbaPipe.java src/JSecureListen.java src/JConnectionProc.java src/JabbaConstructHeader.java -d bin

#javac -classpath .:./lib/commons-cli-1.3.1.jar:./lib/saxonsa.jar:./lib/XMLConverters.jar:./bin:./lib/valid.jar src/JabbaPipe.java src/JSecureListen.java src/JConnectionProc.java src/JabbaConstructHeader.java -d bin

export CLASSPATH=.:./lib/commons-cli-1.3.1.jar:./lib/XMLConverters.jar:./bin:./lib/valid.jar


