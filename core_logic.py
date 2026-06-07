# AnimeRS - Anime Recommendation System

# -----------------------------
# User Login Data
# -----------------------------
stored_username = "Blazzer"
stored_password = "anime123"

# -----------------------------
# Anime Database
# -----------------------------
anime_database = [
    {
        "title": "Link Click",
        "genres": ["thriller", "donghua"],
        "romance": False,
        "fast_pacing": True,
        "strong_story": True,
        "stream_link": "https://example.com/link-click"
    },

    {
        "title": "Super Cube",
        "genres": ["action", "donghua", "fantasy"],
        "romance": False,
        "fast_pacing": True,
        "strong_story": True,
        "stream_link": "https://example.com/super-cube"
    },

    {
        "title": "Clannad",
        "genres": ["romance", "drama"],
        "romance": True,
        "fast_pacing": False,
        "strong_story": True,
        "stream_link": "https://example.com/clannad"
    },

    {
        "title": "Attack on Titan",
        "genres": ["action", "dark fantasy"],
        "romance": False,
        "fast_pacing": True,
        "strong_story": True,
        "stream_link": "https://example.com/aot"
    },

    {
        "title": "Vinland Saga",
        "genres": ["historical", "action"],
        "romance": False,
        "fast_pacing": False,
        "strong_story": True,
        "stream_link": "https://example.com/vinland-saga"
    }
]

# -----------------------------
# System Start
# -----------------------------
print("Welcome to AnimeRS")

# -----------------------------
# User Authentication
# -----------------------------
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == stored_username and password == stored_password:

    print("\nLogin Successful\n")

    # -----------------------------
    # System Introduction
    # -----------------------------
    print("How AnimeRS Works:")
    print("Select your preferences to receive anime recommendations.\n")

    # -----------------------------
    # Genre Selection
    # -----------------------------
    print("Available Genres:")
    print("Action, Fantasy, Dark Fantasy, Thriller, Historical, Donghua, Mecha\n")

    genres_input = input(
        "Enter preferred genres separated by commas: "
    )

    # Convert input into clean list
    selected_genres = genres_input.lower().split(",")
    selected_genres = [genre.strip() for genre in selected_genres]

    # -----------------------------
    # Dislike Filtering
    # -----------------------------
    print("\nSelect elements you dislike:")
    print("No Romance")
    print("No Slow Pacing\n")

    dislikes_input = input(
        "Enter dislikes separated by commas: "
    )

    dislikes = dislikes_input.lower().split(",")
    dislikes = [item.strip() for item in dislikes]

    # -----------------------------
    # Story Preference
    # -----------------------------
    story_preference = input(
        "\nDo you prefer anime with a strong story? (yes/no): "
    ).lower()

    # -----------------------------
    # Recommendation Processing
    # -----------------------------
    recommendations = []

    for anime in anime_database:

        score = 0

        # -----------------------------
        # Genre Matching
        # -----------------------------
        for genre in selected_genres:

            if genre in anime["genres"]:
                score += 2

        # -----------------------------
        # Dislike Filtering
        # -----------------------------
        if "no romance" in dislikes and anime["romance"]:
            continue

        if "no slow pacing" in dislikes and not anime["fast_pacing"]:
            continue

        # -----------------------------
        # Story Preference Scoring
        # -----------------------------
        if story_preference == "yes" and anime["strong_story"]:
            score += 3

        # -----------------------------
        # Add Valid Recommendations
        # -----------------------------
        if score > 0:
            recommendations.append((anime, score))

    # -----------------------------
    # Sort Recommendations
    # -----------------------------
    recommendations.sort(
        key=lambda item: item[1],
        reverse=True
    )

    # -----------------------------
    # Display Recommendations
    # -----------------------------
    if len(recommendations) == 0:

        print("\nNo matching anime found.")

    else:

        print("\nRecommended Anime:\n")

        for index, (anime, score) in enumerate(recommendations, start=1):

            print(f"{index}. {anime['title']} - Match Score: {score}")

        # -----------------------------
        # Anime Selection
        # -----------------------------
        choice = int(input(
            "\nSelect an anime number to watch: "
        ))

        # Validate choice
        if 1 <= choice <= len(recommendations):

            selected_anime = recommendations[choice - 1][0]

            print("\nRedirecting to streaming website...")
            print("Streaming Link:")
            print(selected_anime["stream_link"])

        else:
            print("Invalid selection.")

else:
    print("\nInvalid Username or Password.")