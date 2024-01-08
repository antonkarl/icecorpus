echo "Encoding special markup"
python3 ./scripts/encodemarkup.py $1.tok $1.enc

echo "Tagging using IceTagger"
cat $1.enc | java -classpath "../IceNLP/IceNLPCore.jar" is.iclt.icenlp.runner.RunIceTagger > $1.tagged

echo "Lemmatizing using Lemmald"
cat $1.enc | java -Xmx256m -classpath "../IceNLP/IceNLPCore.jar" is.iclt.icenlp.runner.RunIceTagger -of 1 -lem > $1.lemmatized

# python3 ./scripts/joinlemma.py $1.tagged $1.lemmatized

echo "Parsing using IceParser"
cat $1.tagged | java -classpath "../IceNLP/IceNLPCore.jar" is.iclt.icenlp.runner.RunIceParser -f -l > $1.ipsdx

echo "Converting IceParser's ipsd output to labeled bracketing"
# Assumes .ipsd input and .psd output
python3 ./scripts/ipsd2psd.py $1

echo "Decoding special markup"
python ./scripts/decodemarkup.py $1.ipsd $1.ipsd

echo "Removing temporary files"
rm $1.enc
rm $1.tagged
rm $1.lemmatized
rm $1.ipsdx

echo "Done"
