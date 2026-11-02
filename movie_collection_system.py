#Movie Collection System
import csv
import re
movies = []
with open("movies.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row)
print("\nAll Movie Records")
print("-" * 50)
for movie in movies:
    print(f"Movie ID : {movie['MovieID']}")
    print(f"Title    : {movie['Title']}")
    print(f"Genre    : {movie['Genre']}")
    print(f"Year     : {movie['Year']}")
    print("-" * 50)
movie_id = input("\nEnter Movie ID to Search: ")
found = False
for movie in movies:
    if movie["MovieID"] == movie_id:
        print("\nMovie Found:")
        print(movie)
        found = True
        break
if not found:
    print("Movie ID not found.")
pattern = input("\nEnter movie title pattern to search: ")
print("\nMatching Movies:")
found = False
for movie in movies:
    if re.search(pattern, movie["Title"], re.IGNORECASE):
        print(movie)
        found = True
if not found:
    print("No matching movies found.")