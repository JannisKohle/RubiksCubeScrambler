# Rubiks Cube Scrambler

*An Electron Desktop App that randomly generates Scrambles for a Rubiks Cube*

## How to use it:

1. Clone this Repository
2. Make sure you have Python 3 and NodeJS/npm installed
3. To run the App, first (only once!) you have to do
```npm install --save-dev electron``` in the command line.
4. To open the App, execute ```run.py``` (with python3 !!!)

## How it works:

Every time you generate a new scramble in the App, the program adds
the new scramble to a list of all your scrambles. Before the program shows
you the new scramble it generated, it first looks for duplicates in the list.
After that, you have to reload the window with ```Command-R``` to see the new scramble.
I will probably change it so that you don't have to reload the App yourself.

(The probability that there's a duplicate is very low, so you might want to
change that in ```code/backend.py``` because if you use the App a lot, it
could take some time (actually not very long) until you see the new scramble.)
