#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        rom_dict = {
                "I" = 1,
                "V" = 5,
                "X" = 10,
                "L" = 50,
                "C" = 100,
                "D" = 500,
                "M" = 1000
                }

        result = 0
        max_num = 1001

        for i in roman_string:
            if rom_dict[i] > max_num:
                result += rom_dict[i] - (max_num * 2)
            else:
                result += rom_dict[i]
            max_num = rom_dict[i]

        return result
    return 0
