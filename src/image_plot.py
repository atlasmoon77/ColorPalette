import numpy as np
import csv

# Plotly
import plotly.express as px
import plotly.io as pio

#scikit-learn
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt


def get_rgb():

    r, g, b = [], [], []
    with open('image_rgb_output.csv', mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None) # skip header line
        for row in reader:
            r.append(int(row[0])) 
            g.append(int(row[1])) 
            b.append(int(row[2]))
    
    return r, g, b


def plot_rgb_3d():

    r, g, b = get_rgb()
    rgb = zip(r, g, b)

    elem = [f"Element{i}" for i in range(len(r))]
    colors_list = [f"rgb({r_i}, {g_i}, {b_i})" for r_i, g_i, b_i in rgb]     
    
    # fig3 = px.scatter_3d(x=r, y=g, z=b, color=elem, color_discrete_sequence=colors_list)
    pio.renderers.default = "browser"

    fig = px.scatter_3d(
        x = r,
        y = g, 
        z = b,
        color=elem,
        color_discrete_sequence=colors_list
    )

    fig.show()

    #syntax for 3-D projection
    # ax = plt.axes(projection ='3d')

    # x = np.array(r)
    # y = np.array(g)
    # z = np.array(b)
    # C = np.transpose([x])

    # ax.scatter(r, g, b, c=np.transpose([x/255,y/255,z/255]))
    # ax.set_title ('3d Scatter plot for RGB values')
    # plt.show()

def plot_rgb_kmeans():
    r, g, b = get_rgb()
    x, y, z = np.array(r), np.array(g), np.array(b)
    X = zip(r, g, b)
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(np.transpose([r, g, b]))

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    color_map = {0: centroids[0].tolist(), 1: centroids[1].tolist(), 2: centroids[2].tolist(), 3: centroids[3].tolist()}

    point_colors = [color_map[label] for label in labels]
    point_colors_n = [[col/255 for col in row] for row in point_colors]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(r, g, b, c=point_colors_n)
    ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
               kmeans.cluster_centers_[:, 2], marker='x', color='red', s=100 , linewidths=3)
    
    plt.show()
    