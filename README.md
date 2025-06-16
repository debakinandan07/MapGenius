# 🗺️ GuessTheStates 🐢

An interactive US States guessing game built using Python's `turtle` graphics and `pandas`. This project challenges you to recall and name all 50 US states — with visual feedback and progress tracking!

---

## 🚀 Features

- 🧠 Guess state names interactively
- 📍 State names appear on the map when guessed correctly
- 💾 Saves progress across sessions
- 📊 Exports remaining and guessed states to CSV
- 🐢 Built with Python's `turtle` module

---

## 🎮 How to Play

1. Run the main script (`main.py`)
2. Enter US state names in the pop-up dialog
3. Type `"Save"` or close the dialog to exit
4. View your progress in:
   - `guessed_states.csv`
   - `remaining_states_to_guess.csv`
5. Next time you run the game, it will remember your previous guesses!

---

## 📁 File Structure

```plaintext
project/
├── main.py
├── guessing_board.py
├── write_state_name_on_map.py
├── csv_files/
│   ├── 50_states.csv
│   ├── guessed_states.csv
│   ├── remaining_states_to_guess.csv
├── blank_states_img.gif
├── correctly_guessed_count
