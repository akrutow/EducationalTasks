from functools import total_ordering


@total_ordering
class RomanNumeral:
    _roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 
              'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    
    _arabic = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 
          50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    
    def __init__(self, number):
        self.number = number

    @classmethod
    def convert_to_roman(cls, arabic_number):
        result = ''
        for i in cls._arabic:
            if arabic_number > 1000:
                result += 'M'
                arabic_number -= 1000
            if arabic_number % i != arabic_number and i != 1:
                result += cls._arabic[i] * (arabic_number // i)
                arabic_number = arabic_number % i
            if arabic_number % i != arabic_number and i == 1:
                result += cls._arabic[i] * arabic_number
        return result

    @classmethod
    def convert_to_arabic(cls, roman_number):
        result = 0
        for i in range(1, len(roman_number)):
            if cls._roman[roman_number[i-1]] >= cls._roman[roman_number[i]]:
                result += cls._roman[roman_number[i-1]]
            else:
                result -= cls._roman[roman_number[i-1]]
        result += cls._roman[roman_number[-1]]
        return result

    def __str__(self):
        return f'{self.number}'
    
    def __int__(self):
        return __class__.convert_to_arabic(self.number)
    
    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return __class__.convert_to_arabic(self.number) == __class__.convert_to_arabic(other.number)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return __class__.convert_to_arabic(self.number) < __class__.convert_to_arabic(other.number)
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(__class__.convert_to_roman(__class__.convert_to_arabic(self.number) + __class__.convert_to_arabic(other.number)))
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(__class__.convert_to_roman(__class__.convert_to_arabic(self.number) - __class__.convert_to_arabic(other.number)))
        return NotImplemented

