import sys
current_word = None
current_count = 0   
word = None
for line in sys.stdin:
    nomeArq, qdade = line.split('\t', 1)
    #print (nomeArq  , " - ", qdade) 
    try:
        qdade = int(qdade)
    except ValueError:
        print (nomeArq , " - Erro")
        continue
    if current_word == nomeArq:
       current_count += qdade
    else:
        print (current_word , " - ", current_count)
        current_word = nomeArq
        current_count = 1
print (current_word , " - ", current_count) 
