import sys
for line in sys.stdin:
    itens = line.split ("      ")
    if (len (itens) == 3):
        reSplit = itens [2].split(" ") 
        #print (reSplit[-1].replace ("\n",""))
        ext = reSplit[-1].replace ("\n","").split(".")
        if (len (ext)   >1 ):
            print ("%s\t%s" % (ext[1] , 1  ))

        
 