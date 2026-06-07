#python
# Anime Recommendation System

print("Welcome to the Anime Recommendation System")

# Collect user preferences
genre = input("Enter your preferred genre: ")
mood = input("Enter your preferred story mood: ")

# Check if inputs are not empty
if genre != "" and mood != "":

    print("\nAnalyzing user preferences...\n")

    # Simple recommendation system
    if genre.lower() == "action" and mood.lower() == "exciting":
        print("Recommended Anime:")
        print("- Attack on Titan")
        print("- Demon Slayer")

    elif genre.lower() == "fantasy" and mood.lower() == "dark":
        print("Recommended Anime:")
        print("- Berserk")
        print("- Re:Zero")

    elif genre.lower() == "romance" and mood.lower() == "sad":
        print("Recommended Anime:")
        print("- Your Lie in April")
        print("- Clannad")

    elif genre.lower() == "military" and mood.lower() == "thrilling":
        print("Recommended Anime:")
        print("- Code Geass")
        print("- 86")

    else:
        print("Recommended Anime:")
        print("- Link Click")
        print("- Fullmetal Alchemist: Brotherhood")

else:
    print("Please provide the required preferences.")

