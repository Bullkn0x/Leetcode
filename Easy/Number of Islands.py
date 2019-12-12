class Solution:
    def chartIsland(self, grid, land, row, col):
        # Assume current row and col have already been mapped            
        # check up, down left and right by 1 index
    
        if row - 1 >= 0 and grid[row-1][col] == '1' and (row-1, col) not in land :
            land.add((row-1,col))
            self.chartIsland(grid, land, row-1, col)
            
        if row + 1 < len(grid) and grid[row+1][col] == '1' and (row+1, col) not in land :
            land.add((row+1,col))
            self.chartIsland(grid, land, row+1, col)
            
        if col - 1 >= 0 and grid[row][col-1] == '1' and (row, col-1) not in land :
            land.add((row,col-1))
            self.chartIsland(grid, land, row, col-1)
            
        if col + 1 < len(grid[row]) and grid[row][col+1] == '1' and (row, col+1) not in land :
            land.add((row,col+1))
            self.chartIsland(grid, land, row, col+1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        land = set()
        
        for row, values in enumerate(grid):
            for col, value in enumerate(values):
                if value == '1' and (row,col) not in land:
                    islands +=1
                    land.add((row,col))
                    self.chartIsland(grid, land, row, col)     
                    
        return islands