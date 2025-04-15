entrada  = ("disponíveis", "mapperDir.py", "reducer.py","teste.txt","teste.txt","teste.txt","testeCop2.txt","testeCopia.txt")
current_word = None
current_count = 0   
for line in entrada:
    line = line.strip()
    itens = line.split ()
    #print ("%s" % (itens[0]))
    if current_word == itens[0]:
       #print (current_word , " - ", current_count)
       current_count += 1   
    else:
        print (current_word , " - ", current_count)
        current_word = itens[0]
        current_count = 1