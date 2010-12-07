copy_corpus:t

node: IP*
query: ({2}IP-INF* idomsonly VB|BE|HV|RD|DO|MD) AND (IP-INF* hassister {1}PP) AND (PP iprecedes IP-INF*) AND (PP idomstotal 2) AND (PP idoms P) AND (PP idoms TO)


extend_span{1, 2}: 