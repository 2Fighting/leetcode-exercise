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
