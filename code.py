import random
import statistics
import plotly.figure_factory as ff
import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    data1 = []
    for i in range(0,counter):
        random_index = random.randint(1,len(data)-1)
        val = data[random_index]
        data1.append(val)
    sample_mean = statistics.mean(data1)
    return sample_mean

def show_figure(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    print(mean)
    fig = ff.create_distplot([df],["reading_time"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,10], mode = "lines", name = "Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(1,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_figure(mean_list)
    standarddevi = statistics.stdev(mean_list)
    print(standarddevi)

setup()