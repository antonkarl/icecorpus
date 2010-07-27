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
echo "Fix NEG inside ADVP"
$CS structure_queries/fix-advp-neg.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Fix EM to be tagged BEPI"
$CS structure_queries/fix-em.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Delete NP that idomsonly CODE"
$CS structure_queries/fix-np-over-code.q $FILE
mv -f $FILE.out $FILE

#These last two queries must run at the end of the sequence, and in the same relative order with extend-ip1.q running first

echo ""
echo "Extending span of IP-SUB to nonfinite verb"
$CS structure_queries/extend-ip1.q $FILE
mv -f $FILE.out $FILE

echo ""
echo "Extending span of IP-SUB to finite verb"
$CS structure_queries/extend-ip.q $FILE

mv -f $FILE $2
