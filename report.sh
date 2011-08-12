CORPUSNAME="icepahc"
VERSION="0.9"
DIRNAME=$CORPUSNAME"-v"$VERSION"/"

# Generate report
REPORTDIR="report/"
TEMPFILE="temp.psd"
rm -rf $REPORTDIR
mkdir $REPORTDIR
tscripts/src/tagged2lemmadict.py $DIRNAME"tagged/*.tagged" $REPORTDIR"lemmadict.dat"

tscripts/src/tagged2uniquelemmadict.py $DIRNAME"tagged/*.tagged" $REPORTDIR"uniquelemmadict.dat"
