# create virtualenv
`virtualenv -ppython3 venv`

# activate the virtualenv
`source venv/bin/activate`

# play game
`python game.py`

#Run Test Cases
Navigate to src folder and type below command
`python -m unittest discover -s . -p "*_test.py"`


# src and src_1.0 include games.
1) Pattern Based
2) Number Based


#Tic-Tac-Toe Game

#Design a tic-tac-toe game that has two modes

#Pattern based
First user places X on any position and the second player places O

 | 0 | X |   |
---------------
 |   | X |   |
---------------
 |   | 0 |   |

The first player to get his a row, column or diagonal filled with his pattern wins.


#Number based
First user places any of the odd numbers from 1 to 9 and the second player uses even numbers from 2 to 8

 | 6 | 3 |   |
---------------
 |   | 1 |   |
---------------
 |   | 4 |   |

First player to get a sum of 15 on any row, column or diagonal wins
(The row or column or diagonal can contain numbers entered by other player as well)

Each digit should be entered only once and cannot be repeated

The application should ask for the mode and proceed with the game accordingly.
After each step the application responds with 3 possibilities.
    • Continue (The game should continue)
    • Won (The player has met the criteria for win)
    • Draw (No more positions available)


