import math

def euclideanDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    p = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return p

points = [(2, 3), (8, 3), (8, 15)]

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        res = euclideanDistance(points[i], points[j])
        distances.append(res)

minDistance = min(distances)
print("Distances listesindeki minimum mesafe: ", round(minDistance, 2))
