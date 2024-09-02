import sys

# Braille dictionary (alphabet -> braille)
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
    ' ': '......',
    'cap': '.....O',  # Capitalization leadd
    'num': '.O.OOO',  # New number lead
}

# Reverse mapping of Braille to English
english_dict = {b: e for e, b in braille_dict.items()}

number_braille_dict = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OOO...': '4', 'O..O..': '5',
    'OO.O..': '6', 'OOO.O.': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
}

num_to_braille = {b: e for e, b in number_braille_dict.items()}


def is_braille(input_string : str) -> bool:
    # Check if the input is in Braille or not
    for char in input_string:
        if char != 'O' and char != '.' and char != ' ':
            return False
    return True

def braille_to_english(braille_string):
    english_output = []
    capitalize_next = False
    number_mode = False
    i = 0
    
    while i < len(braille_string):
        braille_char = braille_string[i:i+6]
        i += 6
        
        # Handle special cases and update the state
        handled, capitalize_next, number_mode = handle_special_braille(braille_char, english_output, capitalize_next, number_mode)
        if handled:
            continue
        
        # Convert braille to the appropriate character (number or letter)
        char = convert_braille_to_char(braille_char, number_mode)
        
        # If character was detected, check for capitalization and append to output
        if char:
            if capitalize_next:
                char = char.upper()
                capitalize_next = False
            english_output.append(char)
    
    return ''.join(english_output)

def handle_special_braille(braille_char, english_output, capitalize_next, number_mode):
    if braille_char == braille_dict['cap']:
        return True, True, number_mode  # Set capitalize_next to True
    elif braille_char == braille_dict['num']:
        return True, capitalize_next, True  # Set number_mode to True
    elif braille_char == braille_dict[' ']:
        english_output.append(' ')
        return True, capitalize_next, False  # Set number_mode to False after space
    return False, capitalize_next, number_mode

def convert_braille_to_char(braille_char, number_mode):
    if number_mode:
        char = number_braille_dict.get(braille_char, '')
        if not char:
            number_mode = False  # Exit number mode if invalid number character
        return char
    else:
        return english_dict.get(braille_char, '')






def translate(input_string : str) -> str:
    # TODO: Implement this function
    return ""


if __name__ == 'main':
    input_string = sys.argv[1]
    print(translate(input_string))