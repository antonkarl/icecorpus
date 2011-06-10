copy_corpus:t

node: $ROOT
query: ({1}N-G idoms A*|Á*|B*|C*|D*|E*|É*|F*|G*|H*|I*|Í*|J*|K*|L*|M*|*N*|O*|Ó*|P*|Q*|R*|S*|T*|U*|V*|W*|X*|Y*|Ý*|Z*|Þ*|guð*|[Ss]éra*|[hH]erra*) AND ($ROOT doms .*) AND (.* precedes N-G)

replace_label{1}: NPR-G