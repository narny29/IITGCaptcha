from scipy import misc
from scipy import ndimage
from PIL import Image
import numpy
#65*252*3

for fil in range(1,50):
	if fil%10==0:
		print(fil)
	arr = misc.imread("test/"+str(fil))

	new=[[0 for i in range(252)] for j in range(65)]
	for i in range(65):
		for j in range(252):
			tot=sum(arr[i][j])
			if tot<740:
				new[i][j]=1
	# for row in new:
	# 	print(row)

	col=numpy.matrix([[1] for i in range(252)])
	for i in range(len(new)):
		row=numpy.matrix(new[i])
		mat=row*col
		if mat[0][0]<50:
			for j in range(252):
				new[i][j]=0


	new=numpy.transpose(new)
	col=numpy.matrix([[1] for i in range(65)])
	for i in range(len(new)):
		row=numpy.matrix(new[i])
		mat=row*col
		if mat[0][0]<7:
			for j in range(60):
				new[i][j]=0
	new=numpy.transpose(new)




	chop_factor=2
	for i in range(65):
		j=0
		while j<252:
			if new[i][j]:
				count=0
				while new[i][j]:
					count,j=[count+1,j+1]
				if count<=chop_factor:
					while count:
						new[i][j-count-1]=0
						count-=1
			j+=1


	new=numpy.transpose(new)
	chop_factor=2
	for i in range(252):
		j=0
		while j<65:
			if new[i][j]:
				count=0
				while new[i][j]:
					count,j=[count+1,j+1]
				if count<=chop_factor:
					while count:
						new[i][j-count-1]=0
						count-=1
			j+=1
	new=numpy.transpose(new)


	misc.imsave("b_w/"+str(fil),new,format="png")