import nltk
import random

# Sample music recommendations
music_recommendations = {
    "pop": ["Taylor Swift - Shake It Off", "Ed Sheeran - Shape of You", "Dua Lipa - Don't Start Now"],
    "rock": ["Queen - Bohemian Rhapsody", "Led Zeppelin - Stairway to Heaven", "The Beatles - Hey Jude"],
    "hip hop": ["Kendrick Lamar - HUMBLE.", "Drake - God's Plan", "Cardi B - Bodak Yellow"]
}

# Preprocessing user input
def preprocess_input(input_text):
    return nltk.word_tokenize(input_text.lower())

# Function to recommend music based on user input
def recommend_music(input_text):
    tokens = preprocess_input(input_text)
    for token in tokens:
        for genre, songs in music_recommendations.items():
            if token in genre:
                return random.choice(songs)
    return "I'm sorry, I couldn't find any recommendations for that."

# Main loop
def main():
    print("Welcome to Music Recommender Bot!")
    print("You can ask for music recommendations by mentioning genres like 'pop', 'rock', or 'hip hop'.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        recommendation = recommend_music(user_input)
        print("Bot:", recommendation)

if __name__ == "__main__":
    main()
