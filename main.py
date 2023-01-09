import random


def small_talk(player_input):
  words = [
  'Hi!',
  'How are you?',
  'That\'s great.',
  'Thats great to hear',
  'what\'s your name?',
  'what do you like to do for fun?',
  'Woww! thats very cool',
  'Oh i\'m sorry about that',
  'What are your hobbies?',
  'Whats your favorite color?',
  'Do you have a favorite sport?'
  ]
  return random.choice(words)


def init_chat():
  quit_word = 'STOP'

  player_input= input('Hello!, Whats your name? \n')

  while player_input != quit_word:
    player_input = input(small_talk(player_input) + '\n')

if __name__ == "__main__":
  init_chat()