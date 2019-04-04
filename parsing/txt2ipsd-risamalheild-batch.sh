### Batch-converts files.
### Processes XML-files from directory $1 and saves its output
### (also temporary files) to directory $2.
### Must be run from icecorpus/parsing/
### $1 and $2 must be absolute paths or relative paths from icecorpus/parsing/

mkdir -p $1
mkdir -p $2

python3 ./scripts/risamalheild_hreinsa.py ./logs/ $1/ $2/ log_risamalheild_hreinsad.txt log_risamalheild_ohreinsad.txt

shopt -s nullglob

for f in $2/*.lemmatized # globs files with extension .lemmatized generated in the previous step
do
    # run a modified version of txt2ipsd.sh customized for Risamálheild
    ./txt2ipsd-risamalheild.sh ${f%.lemmatized} # call using filename with extension .lemmatized removed
    
    # convert from .ipsd to .psd
    ./runall.sh ${f%.lemmatized}.ipsd ${f%.lemmatized}.psd
done
