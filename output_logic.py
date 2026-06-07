#python
# Anime Recommendation System - Output Logic

# Anime database
anime_database = [
    {"title": "Attack on Titan", "genres": ["action", "dark fantasy"]},
    {"title": "Demon Slayer", "genres": ["action", "fantasy"]},
    {"title": "Clannad", "genres": ["romance", "drama"]},
    {"title": "Vinland Saga", "genres": ["action", "historical"]},
    {"title": "Re:Zero", "genres": ["fantasy", "thriller"]},
    {"title": "Code Geass", "genres": ["mecha", "thriller"]},
    {"title": "Link Click", "genres": ["thriller", "donghua"]},
    {"title": "Super Cube", "genres": ["action", "donghua"]},
    {"title": "One Piece", "genres": ["fantasy", "adventure"]},
    {"title": "God Of HighSchool", "genres": ["martial arts", "action"]},
    {"title": "cyber punk edgerunners", "genres": ["si-fi", "slice of life"]},
]    

print("Welcome to the Anime Recommendation System")

# Receive user genres
user_input = input("Enter preferred genres separated by commas: ")

# Validate input
if user_input.strip() == "":
    print("Error: No genres entered.")

else:
    # Process input
    selected_genres = user_input.lower().split(",")

    # Remove extra spaces
    selected_genres = [genre.strip() for genre in selected_genres]

    # Create recommendation list
    recommendations = []

    # Search anime database
    for anime in anime_database:

        # Check if anime genres match user genres
        for genre in selected_genres:

            if genre in anime["genres"]:

                # Avoid duplicate recommendations
                if anime["title"] not in recommendations:
                    recommendations.append(anime["title"])

    # Display results
    if len(recommendations) == 0:
        print("No matching anime found.")

    else:
        print("\nRecommended Anime:")

        for anime in recommendations:
            print("-", anime)

