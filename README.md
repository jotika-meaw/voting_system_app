# Voting Systems App 🗳️

**An interactive Streamlit web app for simulating and comparing five voting systems.**

Made by Mahir Faisal and Jotika Das.

## 📌 Overview

This app lets students, researchers, and curious voters explore how different voting methods behave. Pick a system, enter candidates and ballots, and see the winner, tally, and an animated celebration — all in one interactive interface.

## ✨ Features

- **Five voting systems** — First Past the Post, Approval, Preferential, Condorcet, and Borda Count
- **Configurable inputs** — set the number of candidates and voters from the sidebar
- **Interactive ballots** — enter candidate names and votes/rankings with Streamlit widgets
- **Detailed results** — winner announcement plus raw vote counts or scores for every candidate
- **Fireworks animation** — celebrates when a winner is declared
- **Sidebar settings** — switch voting systems without losing your inputs

## 🗳️ Voting Systems Explained

### 1. First Past the Post (FPTP)
Each voter selects one candidate. The candidate with the most votes wins.

### 2. Approval Voting
Voters approve as many candidates as they like. The candidate with the most approvals wins.

### 3. Preferential Voting
Voters rank candidates. Votes are counted in rounds, eliminating the least popular candidate each round until a majority winner emerges.

### 4. Condorcet Method
Voters rank candidates. The winner is the candidate who beats every other candidate in pairwise comparisons (the app reports "No Condorcet Winner" when none exists).

### 5. Borda Count
Voters rank candidates. Points are awarded by rank position and the highest total wins.

## 🛠️ Technologies

- Python 3
- [Streamlit](https://streamlit.io/) (UI and state)
- Standard library: `itertools`, `random`

## 🚀 Installation

```bash
git clone https://github.com/jotika-meaw/voting_system_app.git
cd voting_system_app
pip install streamlit
```

> The only external dependency is Streamlit.

## 💻 Usage

```bash
streamlit run voteapp.py
```

The app opens in your browser. Then:

1. **Choose a voting system** in the sidebar.
2. **Set the number of candidates and voters** (sidebar).
3. **Enter candidate names**, then fill in each voter's ballot as prompted.
4. **Run the voting system** and review the winner, counts, and fireworks.

## 🌐 Live Demo

[https://votingapp.streamlit.app/](https://votingapp.streamlit.app/)

## 📂 Project Structure

```text
voting_system_app/
├── voteapp.py   # Streamlit app: voting logic, UI and fireworks
└── README.md
```

## 👩‍💻 Author

**Jotika Das** — [GitHub](https://github.com/jotika-meaw) · [LinkedIn](https://www.linkedin.com/in/jotikadas) · [Email](mailto:jotikadas57@gmail.com)

Co-developed with Mahir Faisal.