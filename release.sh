CORPUSNAME="icepahc"
VERSION="0.9"
DIRNAME=$CORPUSNAME"-v"$VERSION"/"
TEMPFILE="temp.psd"
rm -rf $DIRNAME
mkdir $DIRNAME
cp lgpl.txt $DIRNAME"lgpl.txt"
cp gpl.txt $DIRNAME"gpl.txt"
cp README $DIRNAME"README"

mkdir $DIRNAME"psd"
mkdir $DIRNAME"txt"
mkdir $DIRNAME"tagged"
mkdir $DIRNAME"info"

echo
echo "Copy finished psd files to release"
cp finished/*.psd $DIRNAME"psd"

echo
echo "Copy info files into info directory"
cp info/*.info $DIRNAME"info"

echo
echo "Generate text versions from psd versions"
./tscripts/src/psd2text.py "finished/*.psd" $DIRNAME"txt/"

echo
echo "Generate tagged versions from psd versions"
./tscripts/src/psd2tagged.py "finished/*.psd" $DIRNAME"tagged/"

echo 
echo "Add README file to top of each psd file"
for i in $(ls icepahc-v0.9/psd/*.psd);
do
echo "/*" >> $TEMPFILE
cat README >> $TEMPFILE
echo "*/" >> $TEMPFILE
cat $i >> $TEMPFILE
mv $TEMPFILE $i
done
exit





