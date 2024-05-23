from operator import itemgetter
import sys
  
nomeArqCorrente = None
nomeArqQdade = 0
nomeArq = None
  
for line in sys.stdin:
    # slpiting the data on the basis of tab we have provided in mapper.py
    nomeArq, qdade = line.split('\t', 1)
    nomeArq = nomeArq.split(".")
    if (len (nomeArq) > 1):
        nomeArq = nomeArq[1]
    else:
        continue
    try:
        qdade = int(qdade)
    except ValueError:
        # qdade was not a number, so silently ignore this line
        continue
    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if nomeArqCorrente == nomeArq:
        nomeArqQdade += qdade
    else:
        # Quando a palavrar mudar mostra a quantida anterior
        if nomeArqCorrente:
            # write result to STDOUT
            print ("%s\t%s" % (nomeArqCorrente, nomeArqQdade))
        nomeArqQdade = qdade
        nomeArqCorrente = nomeArq
# do not forget to output the last word if needed!
if nomeArqCorrente == nomeArq:
    print ("%s\t%s" % (nomeArqCorrente, nomeArqQdade))