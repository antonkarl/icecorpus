CS="java -classpath CS_2.002.75.jar csearch/CorpusSearch"

cp $1 temp.psd
FILE="temp.psd"
rm problemfile.txt

echo ""
echo "Prune ADJP"
$CS structure_queries/prune-adjp.q $FILE > problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Prune ADVP"
$CS structure_queries/prune-advp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE


echo ""
echo "Prune VP"
$CS structure_queries/prune-vp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Prune PP"
$CS structure_queries/prune-pp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be SUCH"
$CS structure_queries/label-such-n.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be SUCH"
$CS structure_queries/label-such-a.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be SUCH"
$CS structure_queries/label-such-d.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be SUCH"
$CS structure_queries/label-such-g.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix eður because I can't stand it any more"
$CS structure_queries/ethur.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be Q"
$CS structure_queries/label-wpro-n.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be Q"
$CS structure_queries/label-wpro-a.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be Q"
$CS structure_queries/label-wpro-d.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix labels that should be Q"
$CS structure_queries/label-wpro-g.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Add NP-POS for pronouns"
$CS structure_queries/add_np_pos.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix NP-POS"
$CS structure_queries/move_np_pos.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix NP-POS"
$CS structure_queries/move_np_pos2.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix CP-ADV"
$CS structure_queries/fix-cpadv.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix CP-REL"
$CS structure_queries/fix-cprel.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix NP hvad"
$CS structure_queries/fix-np-hva.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix ADVP hvar"
$CS structure_queries/fix-adv-hvar.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix C hvort"
$CS structure_queries/fix-hvort.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix NP hvad direct questions"
$CS structure_queries/fix-np-hva-direct.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix ADVP hvar direct questions"
$CS structure_queries/fix-adv-hvar-direct.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

#echo ""
#echo "Add hvar trace"
#$CS structure_queries/add-hvar-trace.q $FILE
#mv -f $FILE.out $FILE

echo ""
echo "Add hvenaer trace"
$CS structure_queries/add-hvenaer-trace.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix NEG inside ADVP"
$CS structure_queries/fix-advp-neg.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix EM to be tagged BEPI"
$CS structure_queries/fix-em.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix EM to be tagged BEPI"
$CS structure_queries/Em.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix EIGI to be tagged NEG"
$CS structure_queries/eigi.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix EIGI to be tagged NEG"
$CS structure_queries/Eigi.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix EIGI to be tagged NEG"
$CS structure_queries/Ekki.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Delete NP that idomsonly CODE"
$CS structure_queries/fix-np-over-code.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix NP-PRN"
$CS structure_queries/prune-npprn.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Prune extra NP nodes in conjunction"
$CS structure_queries/prune-extranps.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Add CONJP to NP conjunction"
$CS structure_queries/fix-npconj.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix N labels that should be NPR"
$CS structure_queries/label-npr-n.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix N labels that should be NPR"
$CS structure_queries/label-npr-a.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix N labels that should be NPR"
$CS structure_queries/label-npr-d.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix N labels that should be NPR"
$CS structure_queries/label-npr-g.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix ADVP and ADV labels that should be PP and P"
$CS structure_queries/label-pp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix ADVP and PP and ADV and Plabels that should be RP"
$CS structure_queries/label-rp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix ADVP and PP and ADV and P labels that should be RP"
$CS structure_queries/label-rp2.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix PP and P labels that should be RP"
$CS structure_queries/label-rp3.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix PP and P labels that should be NP and N"
$CS structure_queries/label-mot.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix PP and P labels that should be NP and N"
$CS structure_queries/label-mot2.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix til ad collocation 1"
$CS structure_queries/tilad.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix til ad collocation 2"
$CS structure_queries/tilad2.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix þá"
$CS structure_queries/tha.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix er"
$CS structure_queries/fix-er.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix svo segjandi"
$CS structure_queries/fix-segjandi.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Add some structure to svo sem"
$CS structure_queries/svosem.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

#These last four queries must run at the end of the sequence, and in the same relative order with extend-cp1.q and extend-ip1.q running before the other of the pair

echo ""
echo "Move adjacent thing under CP"
$CS structure_queries/move-thing-under-cp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Move IP-SUB under preceding CP"
$CS structure_queries/move-ip.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Extending span of CP to nonfinite verb"
$CS structure_queries/extend-cp1.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Extending span of CP to finite verb"
$CS structure_queries/extend-cp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Making IP-SUB under CP which does not have an IP-SUB"
$CS structure_queries/make-ip-under-cp.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Extending span of IP-SUB to nonfinite verb"
$CS structure_queries/extend-ip1.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Extending span of IP-SUB to finite verb"
$CS structure_queries/extend-ip.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix ÞAR TIL ER"
$CS structure_queries/fix-thar-til.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix ÁÐUR EN"
$CS structure_queries/cp-cmp-aduren.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

echo ""
echo "Fix IP-INF sister of a modal"
$CS structure_queries/prune-ipinf2.q $FILE >> problemfile.txt
mv -f $FILE.out $FILE

#python3 "scripts/rm-lemmata.py" $FILE > $FILE.out
#mv -f $FILE.out $FILE

mv -f $FILE $2

grep -a12 "WARNING" problemfile.txt

