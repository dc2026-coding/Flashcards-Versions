import json
import os
import turtle

# Project Start Date: October 24, 2026
# Project Version 1 Date: October 25, 2026
# Project Version 2 Date: November 01, 2026

# Python Project I: Flashcards, First of 4 Projects

# --- Graphics Configuration ---
screen = turtle.Screen()
screen.title("Python Flashcard App")
screen.setup(width=600, height=400)
screen.bgcolor("#f0f4f8")

# A dedicated turtle specifically for rendering text safely onto the window
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()

DATA_FILE = "flashcards.json"


class Flashcard:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word} ( {self.meaning} )"


def load_flashcards():
    """Loads saved cards from a local JSON file if it exists."""
    cards_list = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                for item in data:
                    cards_list.append(Flashcard(item["word"], item["meaning"]))
        except Exception:
            pass  # Fallback to an empty list if file is corrupted
    return cards_list


def save_flashcards(cards_list):
    """Saves the current stack of cards back to the JSON file."""
    serializable_data = [
        {"word": c.word, "meaning": c.meaning} for c in cards_list
    ]
    with open(DATA_FILE, "w") as file:
        json.dump(serializable_data, file, indent=4)


def display_message(text):
    """Clears the screen and draws text centered inside the window."""
    drawer.clear()
    drawer.goto(0, 0)
    drawer.write(text, align="center", font=("Arial", 16, "normal"))


# --- Main Application Flow ---
flash = load_flashcards()

if flash:
    display_message(f"Loaded {len(flash)} existing flashcards from memory!")
else:
    display_message("Welcome! No existing cards found. Let's create some.")

# Adding cards using Turtle text inputs instead of terminal inputs
while True:
    word = screen.textinput(
        "Add Flashcard", "Enter the concept/word you want to learn:"
    )
    if word is None:  # User hit 'Cancel'
        break

    meaning = screen.textinput("Add Meaning", f"Enter the meaning of '{word}':")
    if meaning is None:
        break

    flash.append(Flashcard(word, meaning))
    save_flashcards(flash)

    # Ask to continue via a pop-up window
    choice = screen.textinput(
        "Continue?", "Type '0' to add another card, or '1' to finish:"
    )
    if choice != "0":
        break

# --- Quiz Mode (Simple Review Showcase) ---
if flash:
    display_message("Starting Quiz! Look at your Python window.")
    for card in flash:
        # Show the question
        display_message(f"What does this mean?\n\n👉 {card.word}")
        # Wait for the user to press OK to reveal answer
        screen.textinput("Reveal Answer", "Press OK to reveal the meaning...")

        # Show the answer
        display_message(f"Concept: {card.word}\n\nMeaning: {card.meaning}")
        screen.textinput("Next", "Press OK to see the next card...")

display_message("Session finished!\nClose the window to exit.")
turtle.done()