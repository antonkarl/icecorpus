CS="java -classpath CS_2.002.75.jar csearch/CorpusSearch"

cp $1 temp.psd
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
echo "Prune PP"
$CS structure_queries/prune-pp.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix NP-POS"
$CS structure_queries/move_np_pos.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix NP-POS"
$CS structure_queries/move_np_pos2.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Add NP-POS for pronouns"
$CS structure_queries/add_np_pos.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix CP-ADV"
$CS structure_queries/fix-cpadv.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix CP-REL"
$CS structure_queries/fix-cprel.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix NP hvad"
$CS structure_queries/fix-np-hva.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix ADVP hvar"
$CS structure_queries/fix-adv-hva.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix EM to be tagged BEPI"
$CS structure_queries/fix-em.q $FILE
mv -f $FILE.out $FILE

mv -f $FILE $2
