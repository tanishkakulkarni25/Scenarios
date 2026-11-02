#Develop a Python application to maintain mobile phone records.
import csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="CSV file name")
args = parser.parse_args()
with open(args.filename, "r") as file:
    reader = csv.DictReader(file)
    mobiles = list(reader)
    print("\nAll Mobile Records")
    for mobile in mobiles:
        print(mobile)
    brand = input("\nEnter Brand Name to Search: ")
    print("\nSearch Result:")
    found = False
    for mobile in mobiles:
        if mobile["Brand"].lower() == brand.lower():
            print(mobile)
            found = True
    if not found:
        print("No records found.")