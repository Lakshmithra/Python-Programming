# Tic Tac Toe – Python (CLI Version)

A simple command-line implementation of the classic Tic Tac Toe game using Python.  
The project includes full game logic, input validation, win detection, and replay functionality.

This program was developed as part of my Python learning journey, inspired by the structure taught in the **Complete Python Bootcamp on Udemy** (by Jose Portilla).  
The final implementation and modifications were written by me.

---

## Features

- Two-player command-line gameplay  
- Marker selection (X or O)  
- Random selection of the starting player  
- Error handling and input validation using `try/except`  
- Prevention of moves in occupied positions  
- Detection of all win conditions (rows, columns, diagonals)  
- Draw detection when the board is full  
- Option to replay after each game  

---

## Game Rules

1. Player 1 selects a marker (X or O).  
2. The remaining marker is automatically assigned to Player 2.  
3. A player wins by forming a line of three markers:
   - Horizontal  
   - Vertical  
   - Diagonal  
4. If all positions are filled without a winning combination, the game ends in a draw.

---
