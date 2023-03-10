This script implements various algorithms for solving different problems, as described below:

# LCS (Longest Common Subsequence)
This function receives two strings and returns the length of the longest common subsequence (LCS) between them. The LCS is defined as the longest sequence of characters that appear in both strings in the same order, but not necessarily in contiguous positions.


# GreedyChange
This function takes an integer representing an amount of money and returns a list of the coins that add up to that amount, using a greedy algorithm. The coins used have denominations of 5, 4, 3, and 1. This is a non-optimal solution for finding the minimum number of coins needed to add up to the given amount of money.

# DynamicChange
This function takes an integer representing an amount of money and a list of coin denominations, and returns the minimum number of coins needed to add up to that amount of money. The function uses dynamic programming to find the solution. If it is not possible to add up to the given amount with the given denominations, the function returns -1.

# MinNumCoins
This function is similar to DynamicChange, but instead of returning only the minimum number of coins, it returns a list of the minimum number of coins needed to add up to each amount of money from 0 to the given amount. If it is not possible to add up to a certain amount, the corresponding element in the list is set to -1.

# DPChange
This is a helper function that reads input from a file in a specific format, calls the DynamicChange function, and writes the output to a file in the same format.

# LongestPath
This function calculates the length of the longest path in a directed acyclic graph (DAG) using recursion. The function takes as input the coordinates of the current position in the graph and a matrix of weights representing the edges of the graph.

# ManhattanTourist
This function calculates the length of the longest path in a rectangular grid graph, where the edges have weights given by two matrices, down and right, representing the vertical and horizontal edges, respectively. The function uses dynamic programming to find the solution.



