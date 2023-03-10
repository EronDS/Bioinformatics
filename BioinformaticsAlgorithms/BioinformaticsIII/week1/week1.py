class week1:
    def LCS(str1:str,str2:str) -> int:
        ''' Longest Common Subsequence (LCS);
         common sequence of characters in common of 2 strings, 
         not necessarily following the same positions in both strings
         '''
         # Initialize a matrix with zeros, with size (len(str2)+1) x (len(str1)+1)
        m = [[0 for j in range(len(str1) + 1)] for j in range(len(str2) + 1)]
         # Iterate through the characters in the strings from the end to the beginning
        for j in range(len(str1)-1,-1,-1):
            for i in range(len(str2) -1,-1,-1):
                if str1[j] == str2[i]:
                     # If the characters at the current positions in the strings match, add 1 to the previous LCS
                    m[i][j] = 1 + m[i+1][j+1]
                else:
                     # If the characters don't match, take the maximum LCS of the substrings
                    m[i][j] = max(m[i][j+1],m[i+1][j])
         # Return the LCS, which is located in the top-left corner of the m matrix
        return m[0][0]

    def GreedyChange(money:int) -> list:
        ''' keep on giving as many coins of the largest denomination until 
        you the value that remains to be given is less than the value of that denomination.
        Non-optimal solution for returning the minimum number of coins that will summed up 
        to specified amount of money (money) '''
        
        denominations = [5,4,3,1]
        change = [] 
        while money > 0:
            for i in denominations:
                if i <= money:
                    change.append(i)
                    money-=i
        return change
    
    def DynamicChange(money:int, denominations:list) -> list:
        ''' recursion solution to minimum number of coins used to summed up to specific amount of money (money),
        if the amount of money cannot be represented by any combination of available coins (coins), return -1. 
        Assuming infinite number of each coin in coins; '''
        dp = [money + 1] * (money + 1)
        dp[0] = 0 
        
        for i in range(1,money+1,1):
            for coin in denominations:
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
                    
        return dp[money] if dp[money] < (money+1) else -1
    
    def MinNumCoins(money:int, denominations:list) -> list:
        ''' recursion solution to minimum number of coins used to summed up to specific amount of money (money),
        if the amount of money cannot be represented by any combination of available coins (coins), return -1. 
        Assuming infinite number of each coin in coins; '''
        dp = [money + 1] * (money + 1)
        dp[0] = 0 
        
        for i in range(1,money+1,1):
            for coin in denominations:
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])   
        return dp
    
    def DPChange(input_file:str,output_file:str):
        ''' Helper function to receive and write data in specified format 
        as input for Dynamic Change'''
        with open(input_file) as f:
            lines = f.readlines()
            amount = int(lines[0].rstrip())
            denominations = [int(i) for i in lines[1].rstrip().split(' ')]
        
        ans = week1.DynamicChange(money=amount,denominations=denominations)
        with open(output_file, mode = 'w') as f:
            f.write(str(ans))
        return
    
    def LongestPath(i:int, j:int, w:list) -> int:
        # Check if the current position (i, j) is the starting position (0, 0)
        if i == 0 and j == 0:
            # If it is, return 0, since the longest path is of length 0
            return 0

        # Initialize the variables x and y with a very small value
        x, y = float('-inf'), float('-inf')
        
        # Check if it's possible to reach the position (i, j) from the position above (i-1, j)
        if i > 0:
            # Calculate the length of the longest path from (0, 0) to (i-1, j) and add the weight of the vertical edge to reach (i, j)
            x = week1.LongestPath(i-1, j, w) + w[i][j]
        
        # Check if it's possible to reach the position (i, j) from the position to the left (i, j-1)
        if j > 0:
            # Calculate the length of the longest path from (0, 0) to (i, j-1) and add the weight of the horizontal edge to reach (i, j)
            y = week1.LongestPath(i, j-1, w) + w[i][j]
            
        # Return the length of the longest path from (0, 0) to (i, j) by choosing the maximum value between x and y
        return max(x, y)
        
    def ManhattanTourist(n:int, m:int, down:list, right:list) -> int:
        # Initialize the s matrix with zeros, with size (n+1) x (m+1)
        s = [[0] * (m+1) for _ in range(n+1)]

        # Initialize the values in the first column using the down weights
        for i in range(1, n+1):
            s[i][0] = s[i-1][0] + down[i-1][0]

        # Initialize the values in the first row using the right weights
        for j in range(1, m+1):
            s[0][j] = s[0][j-1] + right[0][j-1]

        # Fill in the remaining values using the recurrence relation
        for i in range(1, n+1):
            for j in range(1, m+1):
                s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])

        # Return the maximum score, which is located in the bottom-right corner of the s matrix
        return s[n][m]
        
    def InputManhattanTourist(filepath:str) -> int:
        # Open the file at the specified filepath and read its lines into a list
        file = open(filepath).readlines()

        # Remove newline characters from the end of each line and split the first line into its two integer values
        lines = [line.rstrip() for line in file]
        [n,m] = [int(e) for e in lines[0].split()]

        # Find the index of the line containing the dash character, which separates the down and right matrices
        b = lines.index('-')

        # Extract the down and right matrices from the lines list and convert their elements to integers
        down, right = lines[1:b], lines[b+1:]
        down = [[int(e) for e in E.split()] for E in down]
        right = [[int(e) for e in E.split()] for E in right]

        # Compute the Manhattan Tourist score using the extracted matrices and return it
        return week1.ManhattanTourist(n,m,down,right)
            
    def ManhattanTouristDiag(n:int, m:int, down:list, right:list, diag:list) -> int:
        # Initialize the s matrix with zeros, with size (n+1) x (m+1)
        s = [[0] * (m+1) for _ in range(n+1)]

        # Initialize the values in the first column using the down weights
        for i in range(1, n+1):
            s[i][0] = s[i-1][0] + down[i-1][0]

        # Initialize the values in the first row using the right weights
        for j in range(1, m+1):
            s[0][j] = s[0][j-1] + right[0][j-1]

        # Fill in the remaining values using the recurrence relation
        for i in range(1, n+1):
            for j in range(1, m+1):
                s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1], s[i-1][j-1]+diag[i-1][j-1])

        # Return the maximum score, which is located in the bottom-right corner of the s matrix
        return s[n][m]

    def InputManhattanTouristDiag(filepath:str) -> int:
        # Open the file at the specified filepath and read its lines into a list
        file = open(filepath).readlines()

        # Remove newline characters from the end of each line and split the first line into its two integer values
        lines = [line.rstrip() for line in file]
        [n,m] = [int(e) for e in lines[0].split()]

        # Find the indices of the lines containing the dash character, which separate the down, right, and diag matrices
        b1 = lines.index('-')
        b2 = lines[b1+1:].index('-') + b1 + 1

        # Extract the down, right, and diag matrices from the lines list and convert their elements to integers
        down, right, diag = lines[1:b1], lines[b1+1:b2], lines[b2+1:]
        down = [[int(e) for e in E.split()] for E in down]
        right = [[int(e) for e in E.split()] for E in right]
        diag = [[int(e) for e in E.split()] for E in diag]

        # Compute the Manhattan Tourist score using the extracted matrices and return it
        return week1.ManhattanTouristDiag(n,m,down,right,diag)
    
    def backtrack(v, w):
        # Initialize the matrices with zeros
        s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]
        backtrack = [[None] * (len(w) + 1) for _ in range(len(v) + 1)]

        # Fill the matrices with values and backtrack directions
        for i in range(1, len(v) + 1):
            for j in range(1, len(w) + 1):
                # If the current elements match, add 1 to the diagonal value in s
                match = 0 
                if v[i-1] == w[j-1]:
                    match = 1
                
                s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + match)
                
                # Determine the direction of the backtrack based on the maximum value in s
                if s[i][j] == s[i-1][j]:
                    backtrack[i][j] = '↓'
                elif s[i][j] == s[i][j-1]:
                    backtrack[i][j] = '→'
                elif s[i][j] == s[i-1][j-1] + match:
                    backtrack[i][j] = '↘'
                        
        # Return the matrix of backtrack directions
        return backtrack
    
    def getLCS(v,w):
        backtrack = week1.backtrack(v,w)
        i,j = len(v), len(w) # getting lengths of both strings, remember that -1 because of padding.
        lcs = '' # initializing string
        while i > 0 and j > 0: 
            if backtrack[i][j] == '↘':
                lcs += v[i-1]
                i-=1
                j-=1
            elif backtrack[i][j] == '↓':
                i-=1
            else: j-=1
        return lcs[::-1]

    def getLCSfromfile(file):
        with open(file) as f:
            lines = f.readlines()
            return week1.getLCS(v=lines[0],w=lines[1])
    
    def backtrack(v, w):
        # Initialize the matrices with zeros
        s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]
        backtrack = [[None] * (len(w) + 1) for _ in range(len(v) + 1)]

        # Fill the matrices with values and backtrack directions
        for i in range(1, len(v) + 1):
            for j in range(1, len(w) + 1):
                # If the current elements match, add 1 to the diagonal value in s
                match = 0 
                if v[i-1] == w[j-1]:
                    match = 1
                
                s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + match)
                
                # Determine the direction of the backtrack based on the maximum value in s
                if s[i][j] == s[i-1][j]:
                    backtrack[i][j] = '↓'
                elif s[i][j] == s[i][j-1]:
                    backtrack[i][j] = '→'
                elif s[i][j] == s[i-1][j-1] + match:
                    backtrack[i][j] = '↘'
                        
        # Return the matrix of backtrack directions
        return backtrack 
        
print(week1.getLCSfromfile('example.txt'))