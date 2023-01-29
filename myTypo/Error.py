import random
import re
import datetime
from myTypo.keyboardlayouts import my_default

class StrError:
    """
    This class simulates typographical errors on String data types. Multiple error methods can be chained after
    initializing the class.

    Attributes:
        result (str): Output of the typographical error.
    """

    def __init__(self, value, seed=None):
        """
        The constructor for the StrError class.
        :param value: The string to alter with error.
        :param seed: Seed for random value generation.
        """
        random.seed(seed)
        self.result = value

    def __repr__(self):
        return self.result

    def char_swap(self):
        """
        Swaps two random consecutive word characters (regex \\w) in the string. The replacing character retains the case
        of replaced character. For example, after character swap, 'Happy' may become 'Ahppy'. Here, H and a are
        swapped, and those also retain each other's case. :return: An instance of the StrError class.
        """
        strval = self.result
        # all the locations where there are two consecutive alphanumeric characters.
        locations = [m.start() for m in re.finditer(r'(?=\w{2})', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            # Preserving the cases.
            firstchar = strval[location].upper() if strval[location + 1].isupper() else strval[location].lower()
            secondchar = strval[location + 1].upper() if strval[location].isupper() else strval[location + 1].lower()
            self.result = strval[:location] + secondchar + firstchar + strval[location + 2:]
        return self

    def missing_char(self):
        """
        Skips a random word character (regex \\w) in the string.
        :return: An instance of the StrError class.
        """
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'\w', strval)]
        if len(locations) > 1:
            location = locations[random.randint(0, len(locations) - 1)]
            self.result = strval[:location] + strval[location + 1:]
        return self

    def extra_char(self):
        """
        Adds an extra, keyboard-neighbor, letter next to a random word character (regex \\w).
        :return: An instance of the StrError class.
        """
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'\w', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            trigger_char = strval[location]
            char_to_add = my_default.get_random_neighbor(trigger_char)
            self.result = strval[:location] + char_to_add + strval[location:]
        return self

    def nearby_char(self):
        """
        Replaces a random word character (regex \\w) with keyboard-neighbor letter. The replacing character retains
        the case of the replaced character. :return: An instance of the StrError class.
        """
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'\w', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            char_to_replace = strval[location]
            replace_with = my_default.get_random_neighbor(char_to_replace)
            # preserve case of the replaced character
            replace_with = replace_with.upper() if char_to_replace.isupper() else replace_with.lower()
            self.result = strval[:location] + replace_with + strval[location + 1:]
        return self

    def similar_char(self):
        """
        Replaces a random word character (regex \\w) with another visually similar character. The replacing character
        does not retain the case of the replaced character. :return: An instance of the StrError class.
        """
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'\w', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            char_to_replace = strval[location]
            replace_with = my_default.get_random_visually_similar_char(char_to_replace)
            self.result = strval[:location] + replace_with + strval[location + 1:]
        return self
        
    def random_space(self):
        """
        Adds a random space in the string.
        :return: An instance of the StrError class.
        """
        strval = self.result
        # all the locations where there are non-space characters.
        locations = [m.start() for m in re.finditer(r'\S', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            self.result = strval[:location] + ' ' + strval[location:]
        return self

    def repeated_char(self):
        """
        Repeats a random word character (regex \\w).
        :return: An instance of the StrError class.
        """
        strval = self.result
        # all the locations where there are word characters.
        locations = [m.start() for m in re.finditer(r'\w', strval)]
        if len(locations) > 0:
            location = locations[random.randint(0, len(locations) - 1)]
            char_to_repeat = strval[location]
            self.result = strval[:location] + char_to_repeat + strval[location:]
        return self

class IntError:
    """
    This class simulates typographical errors on Integer data types. Multiple error methods can be chained after
    initializing the class.

    Attributes:
        result (int): Output of the typographical error.
    """

    def __init__(self, value, seed=None):
        """
        The constructor for the IntError class.
        :param value: The integer to alter with error.
        :param seed: Seed for random value generation.
        """
        self.originalseed = seed
        random.seed(seed)
        # parse the integer
        if not isinstance(value, int):
            raise Exception("value: '" + value + "' is not an integer")
        # set sign and absolute value
        self.sign = pow(-1, int(value < 0))
        self.magnitude = abs(value)

    def __repr__(self):
        return self.result

    @property
    def result(self):
        return self.sign * self.magnitude

    # Swaps random two digits, and returns a valid integer
    def digit_swap(self):
        """
        Swaps two random consecutive digits in the integer.
        :return: An instance of the IntError class.
        """
        strval = str(self.magnitude)
        self.magnitude = int(StrError(strval, seed=self.originalseed).char_swap().result)
        return self

    # Randomly skip a digit.
    def missing_digit(self):
        """
        Skips a random digit in the integer.
        :return: An instance of the IntError class.
        """
        strval = str(self.magnitude)
        self.magnitude = int(StrError(strval, seed=self.originalseed).missing_char().result)
        return self

    # Add an extra, nearby digit
    def extra_digit(self):
        """
        Adds an extra, keyboard-neighbor, digit next to a random digit in the integer.
        :return: An instance of the IntError class.
        """
        strval = str(self.magnitude)
        self.magnitude = int(StrError(strval, seed=self.originalseed).extra_char().result)
        return self

    # Replaces a digit with a nearby digit on keyboard.
    def nearby_digit(self):
        """
        Replaces a random digit in the integer with a keyboard-neighbor digit.
        :return: An instance of the IntError class.
        """
        strval = str(self.magnitude)
        self.magnitude = int(StrError(strval, seed=self.originalseed).nearby_char().result)
        return self

    # replaces with another visually similar digit
    def similar_digit(self):
        """
        Replaces a random digit with another visually similar digit.
        :return: An instance of the IntError class.
        """
        strval = str(self.magnitude)
        location = random.randint(0, len(strval) - 1)
        digit_to_replace = strval[location]
        replace_with = my_default.get_random_visually_similar_digit(digit_to_replace)
        self.magnitude = int(strval[:location] + replace_with + strval[location + 1:])
        return self

    # Randomly repeats a digit.
    def repeated_digit(self):
        """
        Repeats a random digit in the integer.
        :return: An instance of the IntError class.
        """
        strval = str(self.magnitude)
        self.magnitude = int(StrError(strval, seed=self.originalseed).repeated_char().result)
        return self

    # Randomly replace a repeated digit with a single one
    def unidigit(self):
        """
        Replaces a random consecutive repeated digit with a single digit.
        :return: An instance of the IntError class.
        """
        strval = str(self.magnitude)
        self.magnitude = int(StrError(strval, seed=self.originalseed).unichar().result)
        return self
