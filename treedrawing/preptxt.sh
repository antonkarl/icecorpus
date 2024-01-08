cat $1.txt | java -classpath "../IceNLP/IceNLPCore.jar" is.iclt.icenlp.runner.RunTokenizer > $1.tok

echo "Done"
