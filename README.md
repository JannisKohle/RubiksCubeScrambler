# Rubiks Cube Scrambler

*An Electron Desktop App that randomly generates Scrambles for a Rubiks Cube*

## How to use it:

1. Clone this Repository
2. Make sure to have Python 3 and NodeJS/npm installed
3. To open the App, execute ```run.py``` (with python3 !!!)

## How it works:

Every time you generate a new scramble in the App, the program adds
the new scramble to a list of all your scrambles. Before the program shows
you the new scramble it generated, it first looks for duplicates in the list.

(The probability that there's a duplicate is very low, so you might want to
change that in ```code/backend.py``` because if you use the App a lot, it
could take some time (actually not very long) until you see the new scramble.)
