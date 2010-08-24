node: IP*

copy_corpus: t

query: ([1]{1}NP* hasSister [2]{2}NP-POS)
        AND ([1]NP* iPrecedes [2]NP-POS)

extend_span{1, 2}:
