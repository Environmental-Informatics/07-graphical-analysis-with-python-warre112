#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Les Warren
@author: warre112
ABE 65100 Spring 2020, Purdue University
Created on Fri Feb 28 13:33:51 2020

This program inputs a .csv dataset using the read_table fcn from panadas,
creates six different figures to perform graphical analysis on the data including
histogram, scatterplot, KDE plot, and Q-Q plot.

Files runs off of "all_month.csv" input file in this directory

"""

import pandas 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import scipy.stats as stats

data= pandas.read_table("all_month.csv", sep= "," )
#inputs dataset using function from pandas 

new_data= data.dropna(axis=0, subset=['mag']) 
# removes any rows with "NA" values in the 'mag' column

plt.hist(new_data['mag'], bins=10, range=(0,10)) #histogram of magnitudes
plt.xlabel('Magnitude')
plt.ylabel('Frequency')

sb.kdeplot(np.array(new_data['mag']),kernel='gau', bw=0.2) #KDE plot of magnitudes with a kernel width of 0.2
plt.xlabel('Magnitude')
plt.ylabel('Frequency')

plt.scatter(new_data['longitude'], new_data['latitude'], marker=".") #scatter plot of lat/long with longitude on x axis and latitude on y axis
plt.xlabel('Longitude')
plt.ylabel('Latitude')


depth_data= new_data['depth'] #creates variable with just depth
dep=np.sort(depth_data) #sort array
cd=np.linspace(0,1,len(new_data['depth'])) #evenly spaces numbers over interval 

plt.plot(dep,cd) #plot of sorted depths and depths spaced over interval 
plt.xlabel("Depth")
plt.ylabel("Cumulative Distribution")
plt.show()

plt.scatter(new_data['mag'], new_data['depth'], marker ='.') #scatter plot o magnitude and depth
plt.xlabel('Magnitude')
plt.ylabel('Depth')

stats.probplot(new_data['mag'], dist='norm', plot=plt) #QQ plot with normal distribution 
