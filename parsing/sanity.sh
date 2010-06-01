CS="java -classpath ../forrit/CS_2.002.69.jar csearch/CorpusSearch"

tempfile="temp.psd"
cp -f $1.psd $tempfile

echo ""
echo "Two subjects"
$CS sanity_checks/2sbj.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Missing subject"
$CS sanity_checks/missing-subject-2.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Superfluous ADJP"
$CS sanity_checks/superfluous-adjp.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Missing CP"
$CS sanity_checks/missing-cp.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Missing C"
$CS sanity_checks/missing-c.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Missing NP-PRN"
$CS sanity_checks/missing-np-prn.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Bare ADJP at IP level"
$CS sanity_checks/bad-bare-adjp-1.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Bad IP daughter"
$CS sanity_checks/bad-ip-daughter.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Bad argument"
$CS sanity_checks/bad-argument.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Bad bare QP"
$CS sanity_checks/bad-bare-qp.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Bad CP-FRL"
$CS sanity_checks/bad-cp-frl-1.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Bad CP-THT-PRN"
$CS sanity_checks/bad-cp-tht-prn.q $tempfile
mv -f $tempfile.out $tempfile


echo ""
echo "SMC with TO"
$CS sanity_checks/smc-with-to.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "RSP no LFD"
$CS sanity_checks/rsp-no-lfd.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Missing index"
$CS sanity_checks/missing-index-3.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Bad *ICH* trace"
$CS sanity_checks/bad-ich-trace.q $tempfile
mv -f $tempfile.out $tempfile



#echo ""
#echo "Missing antecedent"
#$CS sanity_checks/missing-antecedent.q $tempfile
#mv -f $tempfile.out $tempfile

# NP stuff

echo ""
echo "Nonbranching NP"
$CS sanity_checks/nonbranching-np.q $tempfile
mv -f $tempfile.out $tempfile


# PP stuff

echo ""
echo "Bad PP complement"
$CS sanity_checks/bad-pp-complement-1.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Nonbranching PP"
$CS sanity_checks/nonbranching-pp.q $tempfile
mv -f $tempfile.out $tempfile


echo ""
echo "Missing NP-POS"
$CS sanity_checks/missing-np-pos.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "missing-genitive-under-np-pos"
$CS sanity_checks/missing-genitive-under-np-pos.q $tempfile
mv -f $tempfile.out $tempfile

echo ""
echo "Verb iDoms not lemma ending with a"
$CS sanity_checks/v-idoms-ur.q $tempfile
mv -f $tempfile.out $tempfile



mv -f $tempfile $1.sanity.psd
