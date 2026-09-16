movies = [
    {
        "title": "Interstellar",
        "rating": 9,
        "country": "USA",
        "year": 2014,
        "genre": "Sci-Fi"
    },
    {
        "title": "Parasite",
        "rating": 8.5,
        "country": "South Korea",
        "year": 2019,
        "genre": "Drama"
    },
    {
        "title": "Alice in Borderland",
        "rating": 7.8,
        "country": "Japan",
        "year": 2020,
        "genre": "Drama"
    },
    {
        "title": "The Untamed",
        "rating": 8.7,
        "country": "China",
        "year": 2019,
        "genre": "SuperNatural Fantasy"
    }
]


while True:
    print("\n===== Movie Manager =====")
    print("1. Show movie list")
    print("2. Add movie")
    print("3. Remove movie")
    print("4. Search movie")
    print("5. Filter by country")
    print("6. Filter by genre")
    print("7. Show movies with rating > 8")
    print("8. Calculate average rating")
    print("9. Exit")
    choice = input("Choose option: ")

    # Show movies
    if choice == "1":

        for movie in movies:
            print(
                movie["title"], "|",
                movie["rating"], "|",
                movie["country"], "|",
                movie["year"], "|",
                movie["genre"]
            )

    # Add movie
    elif choice == "2":

        title = input("Enter title: ")
        rating = float(input("Enter rating: "))
        country = input("Enter country: ")
        year = int(input("Enter year: "))
        genre = input("Enter genre: ")

        new_movie = {
            "title": title,
            "rating": rating,
            "country": country,
            "year": year,
            "genre": genre
        }

        movies.append(new_movie)

        print(f"{title} added!")

    # Remove movie
    elif choice == "3":

        title = input("Enter movie to remove: ")

        found = False

        for movie in movies:
            if movie["title"] == title:
                movies.remove(movie)
                print(f"{title} removed!")
                found = True
                break

        if not found:
            print(f"{title} is not in your movie list.")

    # Search movie
    elif choice == "4":

        title = input("Enter movie to search: ")

        found = False

        for movie in movies:
            if movie["title"] == title:
                print("\nMovie found:")
                print("Title:", movie["title"])
                print("Rating:", movie["rating"])
                print("Country:", movie["country"])
                print("Year:", movie["year"])
                print("Genre:", movie["genre"])

                found = True
                break

        if not found:
            print(f"{title} is not in your movie list.")

    # Filter by country
    elif choice == "5":

        country = input("Enter country: ")

        found = False

        for movie in movies:
            if movie["country"] == country:
                print(
                    movie["title"], "|",
                    movie["rating"], "|",
                    movie["country"], "|",
                    movie["year"], "|",
                    movie["genre"]
                )

                found = True

        if not found:
            print(f"No movies found from {country}.")

    # Filter by genre
    elif choice == "6":

        genre = input("Enter genre: ")

        found = False

        for movie in movies:
            if movie["genre"] == genre:
                print(
                    movie["title"], "|",
                    movie["rating"], "|",
                    movie["country"], "|",
                    movie["year"], "|",
                    movie["genre"]
                )

                found = True

        if not found:
            print(f"No movies found in genre: {genre}.")

    # Movies with rating > 8
    elif choice == "7":

        print("\n===== Movies with rating > 8 =====")

        found = False

        for movie in movies:
            if movie["rating"] > 8:
                print(
                    movie["title"], "|",
                    movie["rating"], "|",
                    movie["country"], "|",
                    movie["year"], "|",
                    movie["genre"]
                )

                found = True

        if not found:
            print("No movies found with rating above 8.")

    # Average rating
    elif choice == "8":

        if len(movies) == 0:
            print("There are no movies.")

        else:
            total = 0

            for movie in movies:
                total += movie["rating"]

            average = total / len(movies)

            print(f"Average rating: {average}")

    # Exit
    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")