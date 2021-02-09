from PIL import Image, ImageDraw
from math import sqrt, pi, cos, sin
from Canny_Edge_Detection import canny_edge_detector
from collections import defaultdict

# Load image:
input_image = Image.open("/Users/tobieabel/Desktop/Ball/Whiteball1001.jpg")
input_image.show()
# Output image:
output_image = Image.new("RGB", input_image.size)
#output_image.paste(input_image)
draw_result = ImageDraw.Draw(output_image)

# Find circles
rmin = 30
rmax = 40
steps = 100
threshold = 0.3

points = []#an array containing the radius, offset of x and ofset of y for each possible circle
for r in range(rmin, rmax + 1):
    for t in range(steps):
        points.append((r, int(r * cos(2 * pi * t / steps)), int(r * sin(2 * pi * t / steps))))

acc = defaultdict(int)
for x, y in canny_edge_detector(input_image):#iterate through all edges, offset by value from Points[] and store number of times those values occur in acc dictionary
    for r, dx, dy in points:
        a = x - dx
        b = y - dy
        acc[(a, b, r)] += 1

circles = []
for k, v in sorted(acc.items(), key=lambda i: -i[1]):#iterate through all possible circles in acc dict and keep only those over the threshold, and whose centre is outside other circles(to avoid too many circles)
    x, y, r = k
    if v / steps >= threshold and all((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2 for xc, yc, rc in circles):
        print(v / steps, x, y, r)
        circles.append((x, y, r))

for x, y, r in circles:
    draw_result.ellipse((x-r, y-r, x+r, y+r), outline=(255,0,0,0))

# Save output image
output_image.show()
