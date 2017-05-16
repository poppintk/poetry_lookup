# The main module - need to import so that window code works correctly
import annotate_poetry

NO_STRESS_SYMBOL = 'x'
PRIMARY_STRESS_SYMBOL = '/'
SECONDARY_STRESS_SYMBOL = '\\'  # note: len('\\') == 1 due to special character

"""
A pronouncing table: a nested list, [list of str, list of list of str]
  o a two item list, contains two parallel lists
  o the first item is a list of words (each item in this sublist is a str
    for which str.isupper() is True)
  o the second item is a list of pronunciations, where a pronunciation is a 
    list of phonemes (each item in this sublist is a list of str) 
  o the pronunciation for the word at index i in the list of words is at index
    i in the list of pronunciations
"""

# A small pronouncing table that can be used in docstring examples.
SMALL_TABLE = [['A', 'BOX', 'CONSISTENT', 'DON\'T', 'FOX', 'IN', 'SOCKS'],
               [['AH0'],
                ['B', 'AA1', 'K', 'S'],
                ['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'],
                ['D', 'OW1', 'N', 'T'],
                ['F', 'AA1', 'K', 'S'],
                ['IH0', 'N'],
                ['S', 'AA1', 'K', 'S']]]

# A small poem that can be used in docstring examples.
SMALL_POEM = "\nI'll sit here instead,\n\n\n\nA cloud on my head\n\n"

"""
A pronouncing dictionary is a list of pronouncing lines, where a pronouncing
line is a line in the CMU Pronouncing Dictionary format: 
  a word followed by the phonemes describing how to pronounce the word.
  o example:
    BOX  B AA1 K S
"""

# A small pronouncing dictionary that can be used in docstring examples.
SMALL_PRONOUNCING_DICT = [
    'A AH0',
    'BOX B AA1 K S',
    'CONSISTENT K AH0 N S IH1 S T AH0 N T',
    'DON\'T D OW1 N T',
    'FOX F AA1 K S',
    'IN IH0 N',
    'SOCKS S AA1 K S']


# ===================== Provided Helper Functions =============================

def prepare_word(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been converted to 
    uppercase and punctuation characters have been stripped from both ends. 
    Inner punctuation is left unchanged.
    
    This function prepares a word for looking up in a pronouncing table.

    >>> prepare_word('Birthday!!!')
    'BIRTHDAY'
    >>> prepare_word('"Quoted?"')
    'QUOTED'
    >>> prepare_word("Don't!")
    "DON'T"
    """

    punctuation = """!"`@$%^&_+-={}|\\/—,;:'.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


def get_rhyme_scheme_letter(offset):
    """ (int) -> str

    Precondition: 0 <= offset <= 25

    Return the letter corresponding to the offset from 'A'.  Helpful when 
    labelling a poem with its rhyme scheme.

    >>> get_rhyme_scheme_letter(0)
    'A'
    >>> get_rhyme_scheme_letter(25)
    'Z'
    """

    return chr(ord('A') + offset)


# ======== Students: Add Any Helper Functions Below This Line ================


# ======== Students: Add Any Helper Functions Above This Line ================

# ======== Students: Add One Docstring Example And Function ===================
# ========           Body Code To Each Function Below       ===================

def get_word(pronouncing_line):
    """ (str) -> str

    Precondition: pronouncing_line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return the word in pronouncing_line.

    >>> get_word('ABALONE  AE2 B AH0 L OW1 N IY0')
    'ABALONE'
    """
    res = ''

    # loop over index i until see ' ' empty char
    i = 0
    while pronouncing_line[i] != ' ':
        res += pronouncing_line[i]
        i += 1

    return res


def get_pronunciation(pronouncing_line):
    """ (str) -> list of str

    Precondition: pronouncing_line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return a list containing the phonemes in pronouncing_line.

    >>> get_pronunciation('ABALONE  AE2 B AH0 L OW1 N IY0')
    ['AE2', 'B', 'AH0', 'L', 'OW1', 'N', 'IY0']
    """
    res = []
    l = pronouncing_line.split()

    # looping through the prounncing_list and append to result
    # skip first one
    i = 1
    while i < len(l):
        res.append(l[i])
        i += 1
    return res


def make_pronouncing_table(pronouncing_list):
    """ (list of str) -> pronouncing table

    Precondition: pronouncing_list is a list of pronouncing lines.  
                  Each pronuncing line has the form:
                  WORD  PHONEME_1 PHONEME_2 ... PHONEME_LAST

    Return a pronouncing table for the data in pronouncing_list.

    >>> SMALL_TABLE == make_pronouncing_table(SMALL_PRONOUNCING_DICT)
    True
    """
    # initializing a 2 Dimension res_table for return
    res_table = [[], []]
    # looping through the prounicing line in pronouncing list
    for pronouncing_line in pronouncing_list:
        # append words to first list
        res_table[0].append(get_word(pronouncing_line))
        # append prounciation to second list
        res_table[1].append(get_pronunciation(pronouncing_line))

    return res_table


def look_up_pronunciation(word, pronouncing_table):
    """ (str, pronouncing table) -> list of str

    Return the list of phonemes for pronouncing word, as found in
    pronouncing_table.  Ignore the leading and trailing punctuation in word
    as well as the case of any letters in word.

    >>> pronouncing_table = SMALL_TABLE
    >>> look_up_pronunciation("Don't!", pronouncing_table)
    ['D', 'OW1', 'N', 'T']
    """
    index = 0
    # loop through the words in pronouncing_table[0]
    for w in pronouncing_table[0]:
        # found the word
        if w == prepare_word(word):
            # return the the corresponding pronouncing line
            return pronouncing_table[1][index]
        index += 1
    # in case that pronouncing_table is empty or not found
    return []


def is_vowel_phoneme(s):
    """ (str) -> bool

    Return True if and only if s is a vowel phoneme.  Vowel phonemes are three 
    character strings that start with two uppercase letters and end with a 
    single digit of 0, 1 or 2.  The first uppercase letter must be one of 
    A, E, I, O or U.

    >>> is_vowel_phoneme("AE0")
    True
    """
    # return whether or not last index of string is numeric
    return s[-1].isnumeric()


def last_syllable(phoneme_list):
    """ (list of str) -> list of str

    Return the last vowel phoneme and any subsequent consonant phoneme(s) from
    phoneme_list, in the same order as they appear in phoneme_list.

    >>> last_syllable(['K', 'AH0', 'N', 'S', 'IH1', 'S', 'T', 'AH0', 'N', 'T'])
    ['AH0', 'N', 'T']
    """
    # result list to return
    res = []

    # loop through phoneme_list from backwards
    last_index = len(phoneme_list) - 1
    while last_index >= 0:
        # check whether words is vowel
        if is_vowel_phoneme(phoneme_list[last_index]):
            # found the last vowel
            # looping through rest of list
            while last_index < len(phoneme_list):
                # append the word to result list
                res.append(phoneme_list[last_index])
                # increase index
                last_index += 1
            return res
        # decrease by one
        last_index -= 1


# Interested in why the next docstring starts with an r?
# See section 2.4.1:
# https://docs.python.org/3.4/reference/lexical_analysis.html

def convert_to_lines(poem):
    r""" (str) -> list of str

    Return a list of the lines in poem, with leading and trailing whitespace
    removed from each poem line, and leading and trailing blank lines removed.
    Blank lines between stanzas are reduced to a single blank line.

    >>> convert_to_lines(SMALL_POEM)
    ["I'll sit here instead,", '', 'A cloud on my head']
    """
    result = []
    poem = poem.strip()
    res = poem.split('\n')
    count = res.count('')

    while count > 1:
        index = res.index('')
        res.pop(index)
        count = res.count('')
    for line in res:
        result.append(line.strip())

    return result


def detect_rhyme_scheme(poem_lines, pronouncing_table):
    """ (list of str, pronouncing table) -> list of str

    Return a list of single characters indicating the rhyme scheme for 
    poem_lines, with blank lines that separate stanzas given the rhyme scheme 
    marker ' '.  The marker for the first line in the poem is 'A'. When 
    annotating the rhyme scheme in a poem, consecutive uppercase letters are 
    used, starting with the letters A, B, C, etc

    >>> pronouncing_table = SMALL_TABLE
    >>> poem_lines = ["Don't, in box!", '', 'Fox in socks.', 'Consistent.']
    >>> detect_rhyme_scheme(poem_lines, pronouncing_table)
    ['A', ' ', 'A', 'B']
    """
    syllable_list = []
    # loop through each poem_lines and get the last syllable and append to syllable list
    for s in poem_lines:
        split_str = s.split(' ')
        phoneme_list = look_up_pronunciation(split_str[-1],pronouncing_table)
        syllable_list.append(last_syllable(phoneme_list))

    # initialize a result list and next_letter for offset
    res = []
    next_letter = 0

    # initialize a result list with empty string inside
    for index in range(len(syllable_list)):
        res.append(' ')
    # now we have res = ['','',''] etc
    for i in range(len(syllable_list)):
        # if current element at i is not empty string then continue with next element
        #  =>  current element has been assigned before
        if res[i] == ' ' and syllable_list[i] is not None:
            # get a available letter
            letter = get_rhyme_scheme_letter(next_letter)
            # change letter at index i
            res[i] = letter
            # let j be next index always
            j = i + 1
            # j must be inside the bound
            while j < len(syllable_list):
                # if current element at j is not empty string then continue next element
                #  =>  current element has been assigned before
                if res[j] == ' ':
                    # if current element at index i same as element at index j
                    if syllable_list[i] == syllable_list[j]:
                        res[j] = letter
                # increase index j for current loop
                j += 1
            # increase the letter offset
            next_letter += 1
    return res


def get_stress_pattern(word, pronouncing_table):
    """ (str, pronouncing table) -> str

    Return the stress pattern for pronouncing word using the pronouncing table 
    pronouncing_table.  Separate each stress symbol in the stress pattern by a
    single space, and pad the end of the stress pattern with spaces to make
    the length of the stress pattern the same as the length of word. 

    The stress symbols are given by the defined constants NO_STRESS_SYMBOL,
    PRIMARY_STRESS_SYMBOL, and SECONDARY_STRESS_SYMBOL, which correspond to
    the lexical stress markers 0, 1 and 2, respectively.

    The docstring examples assume NO_STRESS_SYMBOL = 'x', 
    PRIMARY_STRESS_SYMBOL = '/' and SECONDARY_STRESS_SYMBOL = '\\'.

    >>> pronouncing_table = SMALL_TABLE
    >>> get_stress_pattern('consistent', pronouncing_table)
    'x / x     '
    """
    # initialize a result string to return
    res = ''
    # get the result phoneme_list by calling look_up_pronunciation()
    phoneme_list = look_up_pronunciation(word, pronouncing_table)

    # looping through each syllables
    for syllables in phoneme_list:
        # if current syllables is vowel
        if is_vowel_phoneme(syllables):
            # checking if it is unstress
            if int(syllables[-1]) == 0:
                res += NO_STRESS_SYMBOL
            # checking if it is primary stress
            elif int(syllables[-1]) == 1:
                res += PRIMARY_STRESS_SYMBOL
            # checking if it is secondary stress
            elif int(syllables[-1]) == 2:
                res += SECONDARY_STRESS_SYMBOL
            res += ' '
    # pad the end of the stress pattern with spaces to make
    # the length of the stress pattern the same as the length of word.
    for i in range(len(word) - len(res)):
        res += ' '
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
