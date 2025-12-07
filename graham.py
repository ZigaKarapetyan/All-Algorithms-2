def orientation(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def dist_sq(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


def graham_scan(points):
    
    P0 = points[0]
    for p in points:
        if p[1] < P0[1] or (p[1] == P0[1] and p[0] < P0[0]):
            P0 = p

    
    def compare(p):
        
        dx = p[0] - P0[0]
        dy = p[1] - P0[1]
        
        slope = dy / (dx + 0.000001)
        return (slope, dist_sq(P0, p))

    sorted_points = sorted(points, key=compare)

    
    hull = []
    for p in sorted_points:
        
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull



pts = [(0,0), (1,1), (2,0), (2,2), (1,-1), (0,2)]
print("Graham Scan:", graham_scan(pts))
