# 🎄 Advent of Code - My Puzzle Playground


This repo is dedicated to solving the yearly [Advent of Code](https://adventofcode.com/) puzzles. Whether it's parsing strange input formats or solving bizarre elfish logic, it's all part of the holiday magic 🎁


## 🔧 Repo Structure

I'm using a hybrid approach for organization — a nice balance between **clarity** and **branching freedom**:

- The `main` branch contains **all years**, each in its own folder:

📦 advent-of-code/</br>
┣ 📂 2022/</br>
┣ 📂 2023/</br>
┣ 📂 2024/</br>
┗ 📂 2025/</br>

- Inside each year:
  - Each **day** (from `day01` to `day25`) within its own folder.
  - Languages may vary – this is my holiday workshop, and I use the tools I enjoy most that year!
  - Some folders might include:
    - `readme.md` for notes or tricky logic explanations
    - `input.txt` for raw puzzle input
    - Unit tests, if I’m feeling festive </br>
📂 2024/</br>
┣ 📂 day01/</br>
┃ ┗ 📄 solution.(go|js|rs|...)</br>
┣ 📂 day02/</br>
┃ ┗ 📄 solution.*  </br>
┃ ... </br>
┗ 📂 day25/</br>
┗ 📄 solution.*


- I'll also have **feature branches** for each year I'm actively working on (e.g. `2024`), which eventually get merged into `main`.


## 🎯 Goals

- Solve each day's puzzle (both parts!) before the next unlocks... or try my best 😅
- Learn or sharpen a language each year


## 📌 Notes

- Browse branches to see past years' progress.
- This isn't a leaderboard chase — just a cozy ritual of code and curiosity.


## 🛷 Getting Started

```bash
git clone https://github.com/ngure1/advent-of-code.git
cd advent-of-code
git checkout 2024  # Or any other year you want to explore
```
