node: IP*

copy_corpus: t

query: 
(IP-SUB* idomsmod A*P*|N*P*|P*P*|Q*P* {1}\*T\**) AND (!{2}W*P* sameIndex \*T\**) AND (IP-SUB* hassister ![1]CONJP*) AND (![2]CONJP* idoms IP-SUB*)

append_label{1}: -ZZZ-WRONG_TRACE
append_label{2}: -ZZZ-WRONG_TRACE