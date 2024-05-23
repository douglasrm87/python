import threading
import time

def cozinharMacarrao():
    i = 0
    print("\nCozinhando macarrao...")
    while i<3:
        print("...")
        time.sleep(2)
        i=i+1
    print("\nO macarrao esta pronto!")

def fazerMolhoBolonhesa():
    print("\nPreparando os ingredientes...")
    i = 0
    j = 0
    while i<3:
        print("...")
        time.sleep(1.2)
        i=i+1
    print("\nMolho no fogo!")

    while j<3:
        print("...")
        time.sleep(1.8)       
        j=j+1
    print("\nO molho esta pronto!")


print("\nVou fazer um spaghetti.")
nucleo1 = threading.Thread(target=cozinharMacarrao)
nucleo2 = threading.Thread(target=fazerMolhoBolonhesa)

nucleo1.start()
nucleo2.start()

nucleo1.join()
nucleo2.join()

print("\nEstou misturando os dois...")
k = 0
while k<3:
    print("...")
    time.sleep(0.5)
    k=k+1
print("\n\n- - - Spaghetti esta pronto... - - -\n\n")