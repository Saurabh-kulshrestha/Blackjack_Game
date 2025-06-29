# 🃏 Blackjack – Python Console Game

A terminal-based Python implementation of the classic card game **Blackjack**.  
Play against the computer (dealer) and test your luck and strategy with real-time decisions and hidden cards!

---

## 🎮 Game Rules (Simplified)

- Each player is dealt **two cards** at the start.
- Cards 2–10 are worth their face value; J, Q, K = 10; Ace = 11.
- Players can choose to:
  - `Hit (y)` – draw another card
  - `Stand (n)` – keep current cards
- The goal is to get as **close to 21** as possible without going over.
- The dealer (computer) draws cards until its score is 17 or more.
- The winner is whoever is closest to 21 without busting.

---

## 🧾 Features

- ✅ ASCII-art logo display on startup  
- ✅ Score calculation and comparison logic  
- ✅ Bust detection for both player and computer  
- ✅ Console-based Hit/Stand prompts  
- ✅ Clean screen between rounds for a polished look

---

## 📂 Project Structure
blackjack/
├── black.py           # 🔹 Main Python file containing all game logic
├── logo.py            # 🎨 Contains ASCII art logo used at the beginning of the game
├── screenshot.png     # 🖼️ A screenshot showing game execution in the terminal
└── README.md          # 📄 Complete project documentation with rules and usage guide

---

## 🖥️ Sample Gameplay

Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [9, 2], current score: 11
Computer's first card: 10
Type 'y' for Hit to get another card, type 'n' for Stand to pass: y

Your cards: [9, 2, 10], current score: 21
Computer's final hand: [10, 7], final score: 17

You have the higher score! You win! 🏆

---

## 🚀 How to Run

### Requirements:
- Python 3.x

### Steps:
```bash
git clone https://github.com/your-username/blackjack-game.git
cd blackjack-game
python black.py

💡 What I Learned
Working with lists and random selection in Python

Implementing game logic with multiple conditional branches

Handling invalid inputs and making the game more user-friendly

Simulating real-world card mechanics in a text environment


