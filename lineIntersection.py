def line_intersection(x1,y1,x2,y2, x3,y3,x4,y4):
    def det(a,b,c,d): return a*d - b*c
    
    A1 = y2 - y1
    B1 = x1 - x2
    C1 = A1*x1 + B1*y1

    A2 = y4 - y3
    B2 = x3 - x4
    C2 = A2*x3 + B2*y3

    D = det(A1,B1, A2,B2)
    if D == 0:
        return None  

    x = det(C1,B1, C2,B2) / D
    y = det(A1,C1, A2,C2) / D
    return (x,y)


print(line_intersection(0,0, 4,4, 0,4, 4,0))
