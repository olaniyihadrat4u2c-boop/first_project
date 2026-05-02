# Anime Recommendation System

## How to Improve

The current system only has a few genres and only a few recommendations. It needs:
- A more detailed layout
- More genres
- More anime recommendations
- Better recommendation logic

The current input says:
> "The user enters the system"

That is too vague.

The actual input should be:
- The genres selected by the user

Example:
- action
- fantasy
- dark fantasy
- horror
- thriller
- historical
- adventure
- mystery
- isekai
- supernatural

---

# Genre Tag System

Every anime recommended by the system should have its own tags.

To build the tag system, we should ask questions like:
- Is this anime action?
- Is this anime fantasy?
- Is this anime historical?
- Is this anime horror?
- Is this anime supernatural?
- Is this anime dark fantasy?

Example:

- Mushoku Tensei  
  - fantasy
  - adventure
  - isekai

- Jujutsu Kaisen
  - action
  - fantasy
  - dark fantasy
  - supernatural

---

# Recommendation Logic

The system compares:
- the genres selected by the user
with
- the tags assigned to each anime

The anime with the most matching tags should rank higher.

---

# Example

## User Selected Genres

- action
- fantasy
- dark fantasy

---

## Recommended Anime

### Jujutsu Kaisen
Tags:
- action
- fantasy
- dark fantasy

Score:
- action = 1 point
- fantasy = 1 point
- dark fantasy = 1 point

Total:
- 3 points

---

### Mushoku Tensei
Tags:
- fantasy
- action
- adventure
- isekai

Score:
- fantasy = 1 point
- action = 1 point

Total:
- 2 points

---

# Final Ranking

1. Jujutsu Kaisen (Best Match)
2. Mushoku Tensei

---

# What I Will Do

I will:
- Improve the system by adding more genres
- Improve the recommendation system by arranging anime based on how many matching points they get
- Add tags to every anime
- Make the recommended anime match the genres selected by the user
- Add more anime recommendations
- Improve the layout and structure of the system
- Make the recommendation results more accurate