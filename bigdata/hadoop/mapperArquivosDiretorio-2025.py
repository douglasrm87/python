import sys
for line in sys.stdin:
    itens = line.split ("      ")
    if (len (itens) == 3):
        reSplit = itens [2].split(" ") 
        #print (reSplit[-1].replace ("\n",""))
        print ("%s\t%s" % (reSplit[-1].replace ("\n","") , 1  ))
        
 