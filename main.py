"""

Author: Tomer Meskin
Date: 22/9/2023
Description: the program encrypts and decrypts letters according to an encryption table of letters that correspond to
numbers, and then saves the encrypted message in a file, or either decrypts an existing encrypted letter contained in a
file and prints it onto the screen
"""

import sys
import logging

logging.basicConfig(filename='my_log.log', level=logging.DEBUG)

FILE_PATH = r"C:\Users\tomer\Desktop\Python_Projects\cyberDemo\encrypted_message.txt"
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

    try:
        text_file = open(FILE_PATH, 'w')
        text_file.write(encrypted_msg)
        text_file.close()
    except FileNotFoundError:
        logging.debug("file doesn't exist")


def read_from_file():
    """
    reads the file and then closes it
    :return: returns the message in the file
    :rtype: string
    """

    try:
        text_file = open(FILE_PATH, "r")
        msg = text_file.read()
        text_file.close()
        return msg
    except FileNotFoundError:
        logging.debug("file doesn't exist")
        return None
    except Exception as err:
        logging.error("error in reading file" + str(err))
        return None


def encrypt(user_msg):
    """
    encrypts the message that is given by the user
    :param user_msg: the message that is written by the user
    :type param user_msg: string
    :return: the message encrypted
    :rtype: string
    """
    encrypted_message_list = []
    for character in user_msg:
        if character in ENCRYPTION_TABLE.keys():
            encrypted_message_list.append(ENCRYPTION_TABLE[character])
    logging.debug(user_msg + ' | ' + ','.join(encrypted_message_list) + ' | msg has been encrypted successfully')
    return ','.join(encrypted_message_list)


def decrypt():
    """
    decrypts the encrypted message written in the file
    :return: the message decrypted
    :rtypte: string
    """
    key_list = list(ENCRYPTION_TABLE.keys())
    val_list = list(ENCRYPTION_TABLE.values())
    decrypted_message = read_from_file()
    if len(decrypted_message) != 0:
        message_list = decrypted_message.strip().split(',')
        new_list = []
        for num in message_list:
            new_list.append(key_list[val_list.index(num)])
        logging.debug(decrypted_message + ' | ' + ''.join(new_list) + ' | msg has been encrypted successfully')
        return ''.join(new_list)
    else:
        logging.debug('Empty msg has been encrypted successfully')
        return ""


def validate(user_msg):
    for char in user_msg:
        if char not in ENCRYPTION_TABLE.keys():
            return False
    return True


def main():
    """
    main function
    """
    sys.argv[0] = 'python'

    if sys.argv[1] == "encrypt":
        user_message = input('please enter a letter to encrypt please: ')
        if validate(user_message):
            encrypted_message = encrypt(user_message)
            if len(user_message) != 0:
                write_to_file(FILE_PATH, encrypted_message)
            else:
                open(FILE_PATH, 'w').close()
        else:
            print("Error, invalid message")

    elif sys.argv[1] == "decrypt":
        print(decrypt())


if __name__ == '__main__':
    assert encrypt("I love you.") == '44,98,33,36,93,16,98,96,36,92,100'
    assert decrypt('33,16,91,102,90,98,34,16,16,91,98,12,91,98,35,36,36,35') == "let‘s meet at noon"
    main()
