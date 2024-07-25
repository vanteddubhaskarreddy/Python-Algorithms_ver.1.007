class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and grid[i][j] == 1:

                    c = 0
                    if j == 0:
                        try:
                            if grid[i+1][j]==1:
                                c +=1
                                print('2')
                        except:
                            pass
                        try:
                            if grid[i][j+1]==1:
                                c +=1
                                print('4')
                        except:
                            pass
                    else:
                        try:
                            if grid[i+1][j]==1:
                                c +=1
                                print('2')
                        except:
                            pass
                        try:
                            if grid[i][j+1]==1:
                                c +=1
                                print('4')
                        except:
                            pass
                        try:
                            if grid[i][j-1]==1:
                                c +=1
                                print('3')
                        except:
                            pass
                    p += 4-c                          

                elif j == 0 and grid[i][j]==1 and i!=0:
                    c = 0
                    try:
                        if grid[i-1][j]==1:
                            c +=1
                        print('1')
                    except:
                        pass
                    try:
                        if grid[i+1][j]==1:
                            c+=1
                        print('2')
                    except:
                        pass
                    try:
                        if grid[i][j+1]==1:
                            c +=1
                            print('4')
                    except:
                        pass
                    p+=4-c
                
                elif grid[i][j] == 1:
                    c = 0
                    try:
                        if grid[i-1][j]==1:
                            c +=1
                        print('1')
                    except:
                        pass
                    try:
                        if grid[i+1][j]==1:
                            c +=1
                            print('2')
                    except:
                        pass
                    try:
                        if grid[i][j-1]==1:
                            c +=1
                            print('3')
                    except:
                        pass
                    try:
                        if grid[i][j+1]==1:
                            c +=1
                            print('4')
                    except:
                        pass
                    # if grid[i+1][j]==1:
                    #     c+=1
                    # if grid[i][j-1]==1:
                    #     c+=1
                    # if grid[i][j+1]==1:
                    #     c+=1
                    p+=4-c
                    print(c)
        return p
                    