entrada  = ("ola", "ola", "ola")
for line in entrada:
    line = line.strip()
    words = line.split()
    for word in words:
        print ("%s\t%s" % (word, 1))