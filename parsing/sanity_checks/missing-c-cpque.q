node: IP*

copy_corpus: t

query: (IP* idoms {1}CP-QUE|CP-QUE-SBJ) AND (CP-QUE|CP-QUE-SBJ idoms IP-SUB*) AND (CP-QUE|CP-QUE-SBJ idoms !C) AND (IP-SUB* idomsnumber 1 !VB*S|BE*S|DO*S|HV*S)

append_label{1}: -ZZZ-MISS_C