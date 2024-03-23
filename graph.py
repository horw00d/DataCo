import csv
import matplotlib.pyplot as plt
import numpy as np
import io
from flask import Flask, send_file
from flask import jsonify

# Recieves file name, opens csv and returns as 2d array
def open_csv(file_name):
    array = []
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            array.append(row)
    return array

# Adds up each column in array and returns sum per column
def sum_years(array):
    sum_per_column = [0] * (len(array[0]) - 1)
    for row in array[1:]:
        for i, value in enumerate(row[1:], start=1):
            sum_per_column[i - 1] += int(value)
    return sum_per_column

# Calculate net emissions
def calc_net_emissions(sum_emissions, sum_offsets):
    net_emissions = []
    for i in range(len(sum_emissions)):
        net_emission = sum_emissions[i] - sum_offsets[i]
        net_emissions.append(net_emission)
    return net_emissions

def calc_next_year(line):
    m = (line[-1] - line[0]) / len(line)
    return m * (len(line) + 1) + line[0]

# Open CSV files
emissions = open_csv('emissions.csv')
offsets = open_csv('offsets.csv')

#net predicted sectors
def net_predicted_sectors():
    sectors = []
    predicted_nets = []

    for i in range(1, len(emissions)):
        sector_name = emissions[i][0]
        emissions_values = [int(j) for j in emissions[i][1:]]
        offsets_values = [int(j) for j in offsets[i][1:]]
        
        sector = calc_net_emissions(emissions_values, offsets_values)
        predicted_net = calc_next_year(sector)
        
        sectors.append(sector_name)
        predicted_nets.append(predicted_net)

    # Bar graph
    plt.figure(figsize=(10, 8))

    colors = ['green' if net >= 0 else 'red' for net in predicted_nets]
    plt.bar(sectors, predicted_nets, color=colors)

    plt.title('Net Predicted Emissions per Sector for 2024')
    plt.xlabel('Sector')
    plt.ylabel('Net Predicted Emissions')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    
    return send_file(img_bytes, mimetype='image/png')

def emissions_per_sector():
    sectors = []
    total_emissions = []

    for i in range(1, len(emissions)):
        sector_name = emissions[i][0]
        emissions_values = [int(j) for j in emissions[i][1:]]
        
        total_emission = sum(emissions_values)
        
        sectors.append(sector_name)
        total_emissions.append(total_emission)

    # Pie chart
    plt.figure(figsize=(10, 8))

    colors = plt.cm.tab20.colors[:len(sectors)]  # Set colors from the tab20 colormap
    plt.pie(total_emissions, labels=sectors, colors=colors, autopct='%1.1f%%', startangle=140)
    
    plt.title('Emissions per Sector for 2024')
    
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    
    return send_file(img_bytes, mimetype='image/png')


