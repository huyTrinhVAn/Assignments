def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    x = [x1, x2, x3, x4, x5, x6]
    y = [y1, y2, y3, y4, y5, y6]

    x.sort()
    y.sort()

    x1, x2, x3, x4 = x[1], x[2], x[4], x[5]
    y1, y2, y3, y4 = y[1], y[2], y[4], y[5]

    if x2 <= x3 and y2 <= y3:
        return triangle_area(x1, y1, x2, y2, x3, y3)
    else:
        return 0

N = int(input())
triangles = []

for i in range(N):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    triangles.append((x1, y1, x2, y2, x3, y3))

total_area = 0

for x1, y1, x2, y2, x3, y3 in triangles:
    total_area += triangle_area(x1, y1, x2, y2, x3, y3)

for i in range(N):
    for j in range(i + 1, N):
        x1, y1, x2, y2, x3, y3 = triangles[i]
        x4, y4, x5, y5, x6, y6 = triangles[j]
        total_area -= intersection_area(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6)

print(total_area)
