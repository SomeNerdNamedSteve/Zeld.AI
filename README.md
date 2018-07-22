# Zeld.AI

## About
Zeld.AI is an Artificial Intelligence System to play the NES game 'The Legend of Zelda'

## Techical Aspects
Zeld.AI was made in Python 3.5 with the following packages installed via conda:
- keras
- numpy
- opencv
- mss

The emulator that the AI used was called NEStopia.  The following list includes the control input scheme for the AI

- A = L
- B = K
- Up = W
- Left = A
- Down = S
- Right = D
- Start = H
- Select = G

## Emulator Settings and screen configuration
- Set the screen size of NEStopia to 1X

## Code changes
- While the goal is to make no changes to the actual algorithm, the only thing that has to be changed is the capture region.
