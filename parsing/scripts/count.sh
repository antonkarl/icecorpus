echo -e "XXXs per file\n";
ls $1| while read file; do echo -n "$file: "; grep "XXX" "$file" |  wc -l; done
echo -e "Total XXXs: \c"; 
grep "XXX" $1 | wc -l;
echo "";
echo "Words per file";
python3 corpuswords2.py "$1" "$2";

