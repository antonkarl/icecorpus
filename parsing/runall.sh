CS="java -classpath CS_2.002.75.jar csearch/CorpusSearch"

python scripts/splitdet.py $1 $1.out
python scripts/split2person.py $1.out $1.out
python scripts/tagfix.py $1.out $1.out

mv -f $1.out temp.psd
FILE="temp.psd"

echo ""
echo "Prune ADJP"
$CS structure_queries/prune-adjp.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Prune ADVP"
$CS structure_queries/prune-advp.q $FILE
mv -f $FILE.out $FILE


echo ""
echo "Prune VP"
$CS structure_queries/prune-vp.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix CP-ADV"
$CS structure_queries/fix-cpadv.q $FILE
mv -f $FILE.out $FILE


mv -f $FILE $2
