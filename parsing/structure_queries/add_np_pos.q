node: IP*

copy_corpus: t

query: ([1]NP* iDoms [2]N-*)
        AND ([1]NP* iDoms {1}[2]PRO-*)
        AND ([2]PRO-* iDoms *-minn|*-þinn|*-sinn|*-vor)

add_internal_node{1, 1}: NP-POS
