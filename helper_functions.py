from spellchecker import SpellChecker
english = SpellChecker()
def check_word(word):
    if word == english.correction(word):
        return True
    else:
        return False

import re
def is_valid_letters_list(letters_list):
  if len(letters_list) != 4: return False
  for val in letters_list:
    if len(val) != 3: return False
    if not re.match("[a-zA-Z]{3}", val):
      return False
  return True

def check_next_level(letters_list, words_dict, current_string, current_index, max_length=12):
  if len(current_string) >= max_length:
    if check_word(current_string) == True:
      words_dict[current_string] = 1
    return
  else:
    for index in range(len(letters_list)):
      if index != current_index:
        for letter in letters_list[index]:
          check_next_level(letters_list, words_dict, current_string+letter, index, max_length)
          if check_word(current_string) == True & len(current_string) > 2:
            words_dict[current_string] = 1
    return

def find_valid_words(letters_list, max_length=12):
  #if not is_valid_letters_list(letters_list):
  #  raise Exception("letters_list must be a list of four sets of three letters")
  words_dict = {}
  for index in range(len(letters_list)):
    for letter in letters_list[index]:
      check_next_level(letters_list, words_dict, letter, index, max_length)
  return words_dict
