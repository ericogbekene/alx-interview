#!/usr/bin/python3
"""
module to print pascal triangle
"""


def print_pascal(list):
    """
    to print the list out
    """
    for line in list:
        for index in line:
            print(index)


def pascal_triangle(n):
    """
    this funtion will print the pascal triangle, n lines
    """
    if (n < 0):
        return []

    results = [[0 for x in range(n)]
               for y in range(n)]
    for line in range(0, n):
        for row in range(0, line + 1):
            if row == 0 or row == line:
                results[line][row] = 1
                # print(results_array[line][row])
                # print("")
            else:
                results[line][row] = results[line-1][row - 1] + results[line-1][row]
    # print_pascal(results_array)
    return results
