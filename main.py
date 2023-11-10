#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 16:54:07 2023
@author: Ajay prabhat gorrumuchu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def LinePlotCreation(title,fontdict,xdata,y1data,y2data,y3data,y4data,xticks,labelx,labely):
    """
        Create a line plot with multiple lines.

        Parameters:
        title (str): The title of the line plot.
        fontdict (dict): A dictionary containing font properties for customizing the title.
        xdata (list): Data points for the x-axis.
        y1data (list): Data points for the first line (typically labeled 'US').
        y2data (list): Data points for the second line (typically labeled 'CAN').
        y3data (list): Data points for the third line (typically labeled 'SK').
        y4data (list): Data points for the fourth line (typically labeled 'AUS').
        xticks (list): Custom tick positions for the x-axis.
        labelx (str): Label for the x-axis.
        labely (str): Label for the y-axis.

        Returns:
        None """

    plt.figure(figsize=(8, 5))
    plt.title(title,fontdict=fontdict)
    plt.plot(xdata,y1data,'b.-', label='US')
    plt.plot(xdata,y2data,'r.-',label='CAN')
    plt.plot(xdata,y3data,'g.-',label='SK')
    plt.plot(xdata,y4data,'y.-',label='AUS')
    plt.xticks(xticks)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.show()



def histogramCreation(data,bin,ylabel,xlabel,title):
    """
        Create a histogram from the given data.

        Parameters:
        data (list): A list of numeric values representing the data for the histogram.
        bin (int): The number of bins or bin edges for the histogram.
        ylabel (str): Label for the y-axis.
        xlabel (str): Label for the x-axis.
        title (str): The title of the histogram.

        Returns:
        None """

    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=bin, color='#abcdef')
    plt.xticks(bin)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend()
    plt.show()
    return

def PieChartCreation(data,labels,colors,title,explode,pctdistance):
    """
        Create a pie chart using the given data and labels.

        Parameters:
        data (list): A list of numeric values representing the data points for the pie chart.
        labels (list): A list of strings representing labels for each data point.
        colors (list): A list of color codes or names to be used for each section of the pie chart.
        title (str): The title of the pie chart.

        Returns:
        None """

    plt.figure(figsize=(8, 5))
    plt.pie(data, labels=labels, colors=colors, explode=explode, pctdistance=pctdistance,autopct='%.2f %%')
    plt.title(title)
    plt.legend()
    plt.show()
    return

def boxPlotCreation():
    plt.figure(figsize=(5, 8), dpi=100)

    plt.style.use('default')

    barcelona = fifa.loc[fifa.Club == "FC Barcelona"]['Overall']
    madrid = fifa.loc[fifa.Club == "Real Madrid"]['Overall']
    revs = fifa.loc[fifa.Club == "New England Revolution"]['Overall']

    bp = plt.boxplot([barcelona, madrid, revs],
                     labels=['FC Barcelona', 'Real Madrid', 'NE Revolution'],
                     patch_artist=True, medianprops={'linewidth': 2})

    plt.title('Professional Soccer Team Comparison')
    plt.ylabel('FIFA Overall Rating')

    for box in bp['boxes']:
        # change outline color
        box.set(color='#4286f4', linewidth=2)
        # change fill color
        box.set(facecolor='#e0e0e0')
        # change hatch
        # box.set(hatch = '/')

    plt.show()
    return


#load Dataset
gasData = pd.read_csv('gas_prices.csv')
fifa = pd.read_csv('fifa_data.csv')

#Data Preparation
xticks = gasData.Year[::3].tolist()+[2011]
bins = [40,50,60,70,80,90,100]
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count().iloc[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count().iloc[0]
labels = ['Left', 'Right']
colors = ['#abcdef', '#aabbcc']

fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count().iloc[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count().iloc[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count().iloc[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count().iloc[0]
heavy = fifa[fifa.Weight >= 200].count().iloc[0]

weights = [light,light_medium, medium, medium_heavy, heavy]
label = ['under 125', '125-150', '150-175', '175-200', 'over 200']
explode = (.4,.2,0,0,.4)

#Line Graph For Gas Prices
LinePlotCreation('Gas Prices over Time (in USD)',{'fontweight':'bold', 'fontsize': 18},gasData.Year,
                 gasData.USA,gasData.Canada,gasData['South Korea'],gasData.Australia,xticks,'year',
                 'US Dollars')
#Histogram
histogramCreation(fifa.Overall,bins,'Number of Players','Skill Level',
                  'Distribution of Player Skills in FIFA 2018')

#Pie Graph
PieChartCreation([left,right],labels,colors,'Foot Preference of FIFA Players',None,0.8)

#Pie Graph
PieChartCreation(weights,label,None,'Weight of Professional Soccer Players (lbs)',explode,0.8)