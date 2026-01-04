# starter.py

from PIL import Image
import sys
import csv
import image_plot


image_name = sys.argv[1]
img = Image.open(image_name)

width, height = img.size
rgb_img = img.convert('RGB')
r = []
g = []
b = []
for y in range(height):
    for x in range(width):
        r_i, g_i, b_i = rgb_img.getpixel((x, y))
        # DEBUG PURPOSES: print('[', x, ', ', y, '] :: ', 'R: ', r_i, ' G: ', g_i, ' B: ', b_i)
        r.append(r_i)
        g.append(g_i)
        b.append(b_i)

rgb = zip(r, g, b)
column_headers = ['r', 'g', 'b']

with open('image_rgb_output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(column_headers)
    writer.writerows(rgb)

print("File 'image_rgb_output' created successfully")
scores = []

for k in range(2, 11):
    score = image_plot.get_kmeans_score(k)
    print(f"Calculated score for {k} clusters: {score}")
    scores.append(score)

best_k = scores.index(max(scores)) + 2
image_plot.plot_rgb_kmeans(best_k)