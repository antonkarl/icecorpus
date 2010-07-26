copy_corpus:t

node: IP*
query: ({1}IP-INF* idomsonly [1]VB|BE|HV|RD|DO|MD) AND (IP-INF* hassister [2]MD*)

delete_node{1}:
