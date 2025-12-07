def orientation(a, b, c):
   
    return (b[0]-a[0]) * (c[1]-a[1]) - (b[1]-a[1]) * (c[0]-a[0])

def jarvis(points):
    hull = []
    left = min(points)  
    p = left

    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            if q == p or orientation(p, q, r) > 0:
                q = r
        p = q
        if p == left:
            break
    return hull


pts = [(0,0),(1,1),(2,0),(2,2),(1,-1),(0,2)]
print("Jarvis March hull:", jarvis(pts))
