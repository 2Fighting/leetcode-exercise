
#第1题 `两数之和`
def twosum(self,set,target):
	d={}
	for i,num in enumerate(nums):
		sub=target-num
		if sub in d:
			return [d[sub],i]
		else:
			d[sub]=i
		return A
#第14题·最长子序列·
def longsub(self,strs):
	if not strs:
		return ""
	for i,regroup in enumerate(zip(*strs)):
		if len(set(regroup))>1:
			return strs[0][:i]
		else:
			return min（str)

			
#第695题`dfs and application`
def dfs(self,grid):
    #深度优先算法（图论）
    if 0<= i < m and 0<= j <n and grid[i][j]:
        grid[i][j]=0
        return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
    return 0
    
def maxAreaOfIsland(self, grid):
        maxArea=0
        m,n = len(grid),len(grid[0])
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j]:
                grid[i][j]=0
                return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
            return 0
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea,dfs(i,j))
        return maxArea
