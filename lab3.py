# CIS-117 Lab3
# The module reads the country_full.csv file, creates new CSV files by grouping each country by region, and implements exception handling.
# Group 7: Adhamaryz Vargas (Writing), Oi Kwan Wong (Reading)

# Read country_full.CSV file and store in a dictionary{key(country):value(region)}.
# Countries without region information are assigned the value 'other'.

import csv
country_region = dict()

try:
    with open('country_full.csv') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            country = row["name"]
            region = row["region"]
            if region.strip() == "":
                region = "other"
            country_region[country] = region
    if len(country_region) == 0:
        print("The file is empty, no country data")

    # Writing part: Group the countries by region, creating new files.
    region_americas = []
    region_africa = []
    region_asia = []
    region_europe = []
    region_oceania = []
    region_other = []

    country = list(country_region.keys())
    region = list(country_region.values())

    for i in range(len(country)):
        if region[i] == "Americas":
            region_americas.append({
                "Name": country[i],
                "Region": region[i]
            })
        elif region[i] == "Africa":
            region_africa.append({
                "Name": country[i],
                "Region": region[i]
            })
        elif region[i] == "Asia":
            region_asia.append({
                "Name": country[i],
                "Region": region[i]
            })
        elif region[i] == "Europe":
            region_europe.append({
                "Name": country[i],
                "Region": region[i]
            })
        elif region[i] == "Oceania":
            region_oceania.append({
                "Name": country[i],
                "Region": region[i]
            })
        else:
            region_other.append({
                "Name": country[i],
                "Region": region[i]
            })

    regions_list = [region_americas, region_africa, region_asia, region_europe, region_oceania, region_other]
    regions_names = ["americas", "africa", "asia", "europe", "oceania", "other"]

    for i in range(len(regions_list)):
        with open(f'{regions_names[i]}.csv', mode = 'w', newline = '') as file:
            csv_writer = csv.DictWriter(file, fieldnames = ['Name', 'Region'])
            csv_writer.writeheader()
            csv_writer.writerows(regions_list[i])

# Exeption handling
except FileNotFoundError:
    print("CSV file cannot be found.")
except TypeError:
    print("There is an operation or function being applied to an inappropiate data type.")
except IOError:
    print("Input/Output error.")
except PermissionError:
    print("Permission denied.")
except SyntaxError:
    print("There is a misatake with the syntax used.")
except KeyError:
    print("A key or keys used cannot be found.")
except:
    print("Other type of error is happening. Check the code.")