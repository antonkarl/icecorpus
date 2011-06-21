node: IP*

copy_corpus: t

query: 
(IP-SUB* idomsmod {1}A*P*|N*P*|P*P*|Q*P* \*T\**) AND (!{2}W*P* sameIndex \*T\**) AND (IP-SUB* hassister ![1]CONJP*) AND (![2]CONJP* idoms IP-SUB*)

add_leaf_before{1}: (CODE *ZZZ_WRONG_TRACE*)
add_leaf_before{2}: (CODE *ZZZ_WRONG_TRACE*)