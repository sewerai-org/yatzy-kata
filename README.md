# Yatzy Kata

## How to use this Kata

You are given a repository for Yatzy. It is implemented in many languages, but you can choose the language of your choice.

Your goal is to refactor it, keeping in mind language conventions, readbility, and maintabability. Feel free to change improve the tests, too.

Note: Some languages do not have the correct scores in the unit tests.

## Kata: Yatzy rules

The game of Yatzy is a simple dice game. Each player rolls five six-sided dice. They can re-roll some or all of the dice up to three times (including the original roll).

For example, suppose a players rolls:

> 3,4,5,5,2

They hold (-,-,5,5,-) and re-roll (3,4,-,-,2):

> 5,1,5,5,3

They hold (5,-,5,5,-) and re-roll (-,1,-,-,3):

> 5,6,5,5,2

The player then places the roll in a category, such as ones, twos, fives, pair, two pairs etc (see below). If the roll is compatible with the category, the player gets a score for the roll according to the rules. If the roll is not compatible with the category, the player scores zero for the roll.

For example, suppose a player scores 5,6,5,5,2 in the fives category they would score 15 (three fives). The score for that go is then added to their total and the category cannot be used again in the remaining goes for that game.
A full game consists of one go for each category. Thus, for their last go in a game, a player must choose their only remaining category.

Your task is to score a GIVEN roll in a GIVEN category.
*You do NOT have to program the random dice rolling.*
The game is NOT played by letting the computer choose the highest scoring category for a given roll.

## Kata: Yatzy Categories and Scoring Rules

### Chance

The player scores the sum of all dice, no matter what they read.
For example:
  
- 1,1,3,3,6 placed on "chance" scores 14 (1+1+3+3+6)
- 4,5,5,6,1 placed on "chance" scores 21 (4+5+5+6+1)  

### Yatzy

If all dice have the same number,
the player scores 50 points.
For example:
  
- 1,1,1,1,1 placed on "yatzy" scores 50
- 1,1,1,2,1 placed on "yatzy" scores 0

### Ones, Twos, Threes, Fours, Fives, Sixes

The player scores the sum of the dice that reads one, two, three, four, five or six, respectively.
For example:

- 1,1,2,4,4 placed on "fours" scores 8 (4+4)
- 2,3,2,5,1 placed on "twos" scores 4  (2+2)
- 3,3,3,4,5 placed on "ones" scores 0

### Pair

The player scores the sum of the two highest matching dice.
For example, when placed on "pair":
  
- 3,3,3,4,4 scores 8 (4+4)
- 1,1,6,2,6 scores 12 (6+6)
- 3,3,3,4,1 scores 6 (3+3)
- 3,3,3,3,1 scores 6 (3+3)

### Two pairs

If there are two pairs of dice with the same number, the player scores the sum of these dice.
For example, when placed on "two pairs":
  
- 1,1,2,3,3 scores 8 (1+1+3+3)
- 1,1,2,3,4 scores 0
- 1,1,2,2,2 scores 6 (1+1+2+2)

### Three of a kind

If there are three dice with the same number, the player scores the sum of these dice.
For example, when placed on "three of a kind":

- 3,3,3,4,5 scores 9 (3+3+3)
- 3,3,4,5,6 scores 0
- 3,3,3,3,1 scores 9 (3+3+3)

### Four of a kind

If there are four dice with the same number, the player scores the sum of these dice.
For example, when placed on "four of a kind":
  
- 2,2,2,2,5 scores 8 (2+2+2+2)
- 2,2,2,5,5 scores 0
- 2,2,2,2,2 scores 8 (2+2+2+2)

### Small straight

When placed on "small straight", four sequential numbers will score 30, *regardless of the sum of the numbers*

- 1-2-3-4 
  or
- 2-3-4-5
  or
- 3-4-5-6

all score 30

### Large straight

When placed on "large straight", five sequential numbers will score 40, *regardless of the sum of the numbers*

- 1-2-3-4-5 
  or
- 2,3,4,5,6

each combination scores 40

### Full house

If the dice are two of a kind and three of a kind. E.g. if the dice read

- 1,1,2,2,2 scores 25
- 2,2,3,3,4 scores 0
- 4,4,4,4,4 scores 0
