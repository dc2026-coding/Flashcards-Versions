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

# defines how flashcard functions work
class Flashcard:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word} ( {self.meaning} )"


def save_flashcards(cards_list):
    """Saves the current stack of cards back to the JSON file."""
    serializable_data = [
        {"word": c.word, "meaning": c.meaning} for c in cards_list
    ]
    with open(DATA_FILE, "w") as file:
        json.dump(serializable_data, file, indent=4)


def reset_and_preload_filipino():
    """Clears existing memory and loads starter Filipino flashcards."""
    starter_cards = [
        Flashcard("Bahay", "House"),
        Flashcard("Tubig", "Water"),
        Flashcard("Pagkain", "Food"),
        Flashcard("Aso", "Dog"),
        Flashcard("Pusa", "Cat"),
        Flashcard("Salamat", "Thank you"),
        Flashcard("Kaibigan", "Friend"),
        Flashcard("Araw", "Sun"),
    ]
    # Overwrites and clears memories
    save_flashcards(starter_cards)
    return starter_cards


def display_message(text, color="black"):
    """Clears the screen and draws text centered inside the window."""
    drawer.clear()
    drawer.color(color)
    drawer.goto(0, 0)
    drawer.write(text, align="center", font=("Arial", 16, "normal"))


# Main
# Clear memory, load preset
flash = reset_and_preload_filipino()

display_message(f"Memory cleared! Loaded {len(flash)} Filipino flashcards.")

# Add cards
while True:
    choice = screen.textinput(
        "Add More Cards?",
        "Type '0' to add a new card, or '1' to start the test:",
    )
    if choice != "0":
        break

    word = screen.textinput(
        "Add Flashcard", "Enter the Filipino word you want to learn:"
    )
    if word is None:  # User hit 'Cancel'
        break

    meaning = screen.textinput("Add Meaning", f"Enter the meaning of '{word}':")
    if meaning is None:
        break

    flash.append(Flashcard(word, meaning))
    save_flashcards(flash)

# --- Test Mode (Type the Answer) ---
if flash:
    score = 0
    display_message("Starting Test! Look at the pop-up box.")

    for card in flash:
        # Show the question on the canvas
        display_message(f"What does this mean?\n\n👉 {card.word}")

        # Prompt the user to type in their answer
        user_guess = screen.textinput(
            "Test Your Memory", f"Type the English meaning of '{card.word}':"
        )

        # If the user clicks 'Cancel', end the test early
        if user_guess is None:
            break

        # Check answer (case-insensitive and ignores accidental spaces)
        if user_guess.strip().lower() == card.meaning.strip().lower():
            score += 1
            display_message(
                f"✅ Correct!\n\n{card.word} = {card.meaning}", color="#2e7d32"
            )
        else:
            display_message(
                f"❌ Wrong!\n\nYou typed: '{user_guess}'\nCorrect answer: {card.meaning}",
                color="#c62828",
            )

        # Pause so the user can read whether they were right or wrong
        screen.textinput("Next Card", "Press OK to continue...")

    display_message(
        f"Test finished!\nYou got {score} out of {len(flash)} right.\n\nClose the window to exit."
    )
else:
    display_message("Session finished!\nClose the window to exit.")

turtle.done()