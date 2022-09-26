#!/usr/bin/python3
"""Creates a class MyList that inherits from list"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        new_list = self[:]
        end_of_list = False
        temp = 0

        while not end_of_list:
            end_of_list = True
            for i in range(len(new_list) - 1):
                if new_list[i] > new_list[i + 1]:
                    temp = new_list[i]
                    new_list[i] = new_list[i + 1]
                    new_list[i + 1] = temp
                    end_of_list = False

        print(new_list)
