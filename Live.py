from Utils import ERROR_MESSAGE
import MemoryGame
import GuessGame

def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG). " \
                             "Here you can find many cool games to play."

def load_game():
    chosen_game = int(input('Please choose a game to play:'
              '     1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back'
              '     2. Guess Game - guess a number and see if you chose like the computer'))

    if chosen_game < 1 or chosen_game > 2:
        return ERROR_MESSAGE

    level_of_difficulty = int(input('Please choose game difficulty from 1 to 5:'))

    if level_of_difficulty < 1 or level_of_difficulty > 5:
        return ERROR_MESSAGE

    if chosen_game == 1:
        MemoryGame.play(level_of_difficulty)
    elif chosen_game == 2:
        GuessGame.play(level_of_difficulty)