from scipy import misc
from scipy import ndimage
from PIL import Image
import numpy
import matplotlib.pyplot as plt
#65*252*3


def find_neighbour_1(m,n,nxt):
	vis[m][n]=1
	if new[m][n+1]==1 and vis[m][n+1]==0:
		nxt.append([m,n+1])
	if new[m][n-1]==1 and vis[m][n-1]==0:
		nxt.append([m,n-1])
	if new[m+1][n-1]==1 and vis[m+1][n-1]==0:
		nxt.append([m+1,n-1])
	if new[m+1][n]==1 and vis[m+1][n]==0:
		nxt.append([m+1,n])
	if new[m+1][n+1]==1 and vis[m+1][n+1]==0:
		nxt.append([m+1,n+1])



def neighbour_count(m,n):
	nxt,prev=[[],[]]
	count=1
	find_neighbour_1(m,n,nxt)
	count+=len(nxt)
	prev=nxt[:]
	nxt=[]
	while len(prev):
		for a,b in prev:
			if vis[a][b]==0:
				find_neighbour_1(a,b,nxt)
		count+=len(nxt)
		prev=nxt[:]
		nxt=[]
	return count



def remove_neighbour_1(m,n,nxt):
	if new[m][n+1]==1:
		nxt.append([m,n+1])
		new[m][n+1]=0
	if new[m][n-1]==1:
		nxt.append([m,n-1])
		new[m][n-1]=0
	if new[m+1][n-1]==1:
		nxt.append([m+1,n-1])
		new[m+1][n-1]=0
	if new[m+1][n]==1:
		nxt.append([m+1,n])
		new[m+1][n]=0
	if new[m+1][n+1]==1:
		nxt.append([m+1,n+1])
		new[m+1][n+1]=0



def remove_cluster(m,n):
	nxt,prev=[[],[]]
	new[m][n]=0
	remove_neighbour_1(m,n,nxt)
	prev=nxt[:]
	nxt=[]
	while len(prev):
		for a,b in prev:
			if vis[a][b]==0:
				remove_neighbour_1(a,b,nxt)
		prev=nxt[:]
		nxt=[]



xs,ys=[[],[]]
for fil in range(1,5000):
	if fil%10==0:
		print(fil)
	arr = misc.imread("test/"+str(fil))

	new=[[0 for i in range(252)] for j in range(65)]
	for i in range(65):
		for j in range(252):
			tot=sum(arr[i][j])
			if tot<720:
				new[i][j]=1
	# for row in new:
	# 	print(row)

	# new = ndimage.median_filter(new,3)
	new= ndimage.binary_opening(new)


	vis=[[0 for i in range(252)] for j in range(65)]
	for i in range(1,64):
		for j in range(1,251):
			if new[i][j] and not vis[i][j]:
			 	cluster=neighbour_count(i,j)
			 	# ys.append(cluster)
			 	if cluster<200:
			 		remove_cluster(i,j)


	
	misc.imsave("b_w/"+str(fil),new,format="png")

# xs=[x for x in range(len(ys))]
# print(numpy.mean(ys))
# plt.scatter(xs,ys)
# plt.show()