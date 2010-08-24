node: IP*

copy_corpus: t

query: ([2]{2}NP-POS hasSister [1]{1}NP*)
        AND ([2]NP-POS iPrecedes [1]NP*)

extend_span{1, 2}:
