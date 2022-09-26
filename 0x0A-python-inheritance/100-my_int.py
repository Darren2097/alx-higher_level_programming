#!/usr/bin/python3
"""creates a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class that does the opposite"""

    def __eq__(self, op):
        """gets the opposite of equi"""
        return super().__ne__(op)

    def __ne__(self, op):
        """gets the opposite of nonequi"""
        return super().__eq__(op)
