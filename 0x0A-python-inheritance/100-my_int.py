#!/usr/bin/python3
"""creates a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class that does the opposite"""

    def __equal__(self, op):
        """gets the opposite of equal(__equal__)"""
        return super().__nequal__(op)

    def __nequal__(self, op):
        """gets the opposite of non-equal(__nequal__)"""
        return super().__equal__(op)
