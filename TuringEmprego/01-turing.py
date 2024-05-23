'''
Fibonacci
0 1 1 2 3 5 8 13 21 34 55
Next is 34 + 55

Gibonacci
N = 0
X = 0
Y = 1
retorna = 0
gn = g(n-1) - g(n-2)
gn = 0
g0 = x
g1 = y

gfibonacci (N,X,Y)
gfibonacci (0,0,1)
    G0 = G(0-1) - G (0-2) = 0
        X = 0 e y = 1
        G0 = G(0-1) - G (0-2)
        G0 = 0

G1 = G(1-1) - G (1-2) = 1
    gfibonacci (N,X,Y)
    gfibonacci (1,0,1)
    G1 = G(1-1) - G (1-2) = 1
    X = G0 <-> Y = G1
    G1 = Y - X
    G1 = 1 - 0 = 1
    G1 = 1

G2 = G(2-1) - G (2-2) = 1
    gfibonacci (N,X,Y)
    gfibonacci (2,0,1)
    G2 = G(2-1) - G (2-2) = 0
    X = G0 - Y = G1
    G2 = Y - X
    G2 = 1 - 0 = 1
    G2 = 1

G3 = G(3-1) - G (3-2)
    gfibonacci (N,X,Y)
    gfibonacci (3,0,1)
    G3 = G(3-1) - G (3-2) = 0
    X = G2 <-> Y = G1
        X = return 1 in last iteration G2
        Y = return 1 in last iteration G1
    G3 = 1 - 1 = 0

G4 = G(4-1) - G (4-2)
    gfibonacci (N,X,Y)
    gfibonacci (4,0,1)
    G4 = G(4-1) - G (4-2) = ?
    G4 = G(3) - G (2) = ?
    G4 = G(3) - G (2) = ?
    G4 = 0 - 1 = -1
    G4 = -1

G5 = G(5-1) - G (5-2)
    gfibonacci (N,X,Y)
    gfibonacci (5,0,1)
    G5 = G(5-1) - G (5-2) = ?
    G5 = G(4) - G (3) = ?
    G5 = -1 - 0
    G5 = -1

G6 = G(6-1) - G (6-2)
    gfibonacci (N,X,Y)
    gfibonacci (6,0,1)
    G6 = G(6-1) - G (6-2) = ?
    G6 = G(5) - G (4) = ?
    G6 = -1 - -1
    G6 = -2

G7 = G(7-1) - G (7-2)
    gfibonacci (N,X,Y)
    gfibonacci (7,0,1)
    G7 = G(7-1) - G (7-2) = ?
    G7 = G(6) - G (5) = ?
    G7 = -2 -1
    G7 = -3    

G8 = G(8-1) - G (8-2)
    gfibonacci (N,X,Y)
    gfibonacci (8,0,1)
    G8 = G(8-1) - G (8-2) = ?
    G8 = G(7) - G (6) = ?
    G8 = -3 -2
    G8 = -5
'''

