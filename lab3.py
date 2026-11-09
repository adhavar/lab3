# CIS-117 Lab3
# The module reads the country_full.csv file, creates new CSV files by grouping each country by region, and implements exception handling.
# Group 7: Adhamaryz Vargas (Writing), Oi Kwan Wong (Reading)

# Reading part: Uses file handling, and opens and reads the CSV file using the 'with' statement.

# Writing part: Groups the countries by region generating one file per region and implements effective exception handling.


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