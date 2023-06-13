import json
import matplotlib.pyplot as plt
from datetime import datetime
#import spacy

def graph(path):
    with open(path, 'r') as f:
        data = json.load(f)
        keys = list(data["0"].keys())
        years = {2015: 0, 2016: 0, 2017: 0, 2018: 0, 2019: 0, 2020: 0, 2021: 0, 2022: 0, 2023: 0}
        for i in data:
            date = datetime.utcfromtimestamp(int(data[i]['created_utc']))
            years[date.year] += 1
        print(years)
        plt.bar(years.keys(), years.values())
        plt.title('Bar Graph')
        plt.show()
#Hot posts
#graph(r"C:\Users\clash\Documents\PythonCodes\Internship\Data\hot_posts.json")
#Top posts
graph(r"C:\Users\clash\Documents\PythonCodes\Internship\Data\top_posts.json")
