"""

Author: Tomer Meskin
Date: 22/9/2023
Description: the program encrypts and decrypts letters according to an encryption table of letters that correspond to
numbers, and then saves the encrypted message in a file, or either decrypts an existing encrypted letter contained in a
file and prints it onto the screen
"""

import sys

FILE_PATH = r"C:\Users\tomer\Desktop\Python_Projects\encrypted_msg.txt"
ENCRYPTION_TABLE = {
    'A': '56',
    'B': '57',
    'C': '58',
    'D': '59',
    'E': '40',
    'F': '41',
    'G': '42',
    'H': '43',
    'I': '44',
    'J': '45',
    'K': '46',
    'L': '47',
    'M': '48',
    'N': '49',
    'O': '60',
    'P': '61',
    'Q': '62',
    'R': '63',
    'S': '64',
    'T': '65',
    'U': '66',
    'V': '67',
    'W': '68',
    'X': '69',
    'Y': '10',
    'Z': '11',
    'a': '12',
    'b': '13',
    'c': '14',
    'd': '15',
    'e': '16',
    'f': '17',
    'g': '18',
    'h': '19',
    'i': '30',
    'j': '31',
    'k': '32',
    'l': '33',
    'm': '34',
    'n': '35',
    'o': '36',
    'p': '37',
    'q': '38',
    'r': '39',
    's': '90',
    't': '91',
    'u': '92',
    'v': '93',
    'w': '94',
    'x': '95',
    'y': '96',
    'z': '97',
    ' ': '98',
    ',': '99',
    '.': '100',
    ';': '101',
    '‘': '102',
    '?': '103',
    '!': '104',
    ':': '105'
}


def write_to_file(FILE_PATH, encrypted_msg):
    """
    writes to file the encrypted message, then closes it
    :param FILE_PATH: the file path
    :type param FILE_PATH: string
    :param encrypted_msg:
    :type param encrypted_msg: string
    :return: None
    """

    text_file = open(FILE_PATH, 'w')
    text_file.write(encrypted_msg)
    text_file.close()


def read_from_file():
    """
    reads the file and then closes it
    :return: returns the message in the file
    :rtype: string
    """
    text_file = open(FILE_PATH, "r")
    msg = text_file.read()
    text_file.close()
    return msg


def main():


if __name__ == '__main__':
    main()
