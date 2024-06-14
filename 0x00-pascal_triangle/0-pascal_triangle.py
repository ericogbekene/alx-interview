#!/usr/bin/python3
"""
module to print pascal triangle
"""


def pascal_triangle(n):
    """
    this funtion will print the pascal triangle, n lines
    """
    if (n <= 0):
        return []

    results = [[0 for x in range(n)]
               for y in range(n)]
    for line in range(0, n):
        for i in range(0, line + 1):
            if i == 0 or i == line:
                results[line][i] = 1
                # print(results_array[line][row])
                # print("")
            else:
                results[line][i] = results[line-1][i - 1] + results[line-1][i]
    return results
