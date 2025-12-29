import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import csv
import pandas as pd

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