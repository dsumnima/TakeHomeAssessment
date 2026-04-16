movies = {}

for i in range(3):
    print(f"\nEnter details for Movie {i+1}:")
    title = input("Title: ")
    director = input("Director: ")
    year = input("Release Year: ")
    rating = input("Rating: ")

    movies[title] = {
        "Director": director,
        "Year": year,
        "Rating": rating
    }

print("\nMovie Details:")
for title, details in movies.items():
    print(f"\nTitle: {title}")
    for key, value in details.items():
        print(f"{key}: {value}")
