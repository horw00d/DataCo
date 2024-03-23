import csv

# Recieves file name, opens csv and returns as 2d array

def open_csv(file_name):
    array = []
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            array.append(row)
    return array

def sum_years(array):
    # Initialize the sum list with zeros, with the length equal to the number of columns
    sum_per_column = [0] * (len(array[0]) - 1)  

    # Iterate over each row starting from the second row
    for row in array[1:]:
        # Iterate over each value in the row starting from the second value
        for i, value in enumerate(row[1:], start=1):
            # Update the corresponding sum for each column
            sum_per_column[i - 1] += int(value)

    return sum_per_column


def calc_net_emissions(sum_emissions, sum_offsets):
    net_emissions = []
    for i in range(len(sum_emissions)):
        net_emission = sum_emissions[i] - sum_offsets[i]
        net_emissions.append(net_emission)

    return net_emissions

def calc_next_year(line):
    m = (line[len(line)-1]-line[0])/(len(line))
    return (m * (len(line)+1) + line[0])


def best_per_sector(companies):
    best = {}
    for company in companies[1:]:
        company_name = company[1]
        sector = company[2]
        CO2_offset_tonnes = int(company[3])
        cost = int(company[4])
        CO2_per_cost = CO2_offset_tonnes / cost

        if sector in best:
            if CO2_per_cost > best[sector][2]:
                best[sector] = [company_name, sector, CO2_per_cost]
        else:
            best[sector] = [company_name, sector, CO2_per_cost]

    return list(best.values())

def find_pos_sectors(best_companies, net_emissions, sectors):
    positive_sectors = []
    for i in range(len(net_emissions)):
        if net_emissions[i] > 0:
            positive_sectors.append(sectors[i])
    #print(positive_sectors)
    best_positive_sectors = []
    for i in best_companies:
        for j in positive_sectors:
            if j == i[1]:
                best_positive_sectors.append(i)
    
    return best_positive_sectors

sector_names = ["Agriculture", "Aviation", "Commercial", "Energy", "Forestry", "Industrial", "Marine", "Residential", "Transportation", "Waste"]
emissions = open_csv('emissions.csv')
offsets = open_csv('offsets.csv')
companies = open_csv('CarbonOffsetCompanies.csv')
best_companies = best_per_sector(companies)
sum_emissions = sum_years(emissions)
sum_offsets = sum_years(offsets)
sum_net = calc_net_emissions(sum_emissions, sum_offsets)

def func():
    best_companies = best_per_sector(companies)
    return best_companies

sectors = []
for i in range(1, len(emissions)):
    sector_name = emissions[i].pop(0)
    offsets[i].pop(0)
    
    sector = calc_net_emissions([int(j) for j in emissions[i]], [int(j) for j in offsets[i]])
    #print(sector)
    sectors.append(calc_next_year(sector))
# print(sectors)

sum_emissions = sum_years(emissions)
sum_offsets = sum_years(offsets)
sum_net = calc_net_emissions(sum_emissions, sum_offsets)

#print(find_pos_sectors(best_companies, sectors, sector_names))