copy_corpus:t

node: IP*
query: (IP-INF* idomsonly VB|BE|HV|RD|DO|MD) AND ({1}PP idoms {1}IP-INF*) AND (PP idomstotal 3) AND (PP idoms P) AND (PP idoms {2}TO)


extend_span{1, 2}: 