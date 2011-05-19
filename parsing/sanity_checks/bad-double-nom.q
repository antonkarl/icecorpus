node: IP*

copy_corpus: t

query: (IP* iDoms [1]{1}NP-SBJ*|NP-OB*|NP-ADV|NP-DIR|NP-TMP)
   AND (IP* iDoms [2]{2}NP-SBJ*|NP-OB*|NP-ADV|NP-DIR|NP-TMP)
   AND ([1]NP-SBJ*|NP-OB*|NP-ADV|NP-DIR|NP-TMP idoms [3]*-N)
   AND ([2]NP-SBJ*|NP-OB*|NP-ADV|NP-DIR|NP-TMP idoms [4]*-N)

add_leaf_before{1}: (CODE *ZZZ_TWONOMS*)
append_label{2}: -ZZZ-TWONOMS