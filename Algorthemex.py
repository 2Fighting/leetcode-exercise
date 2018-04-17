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
