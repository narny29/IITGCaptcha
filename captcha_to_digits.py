from scipy import misc
from scipy import ndimage
from PIL import Image
import numpy
import matplotlib.pyplot as plt
#65*252

xs,ys=[[],[]]
pic=1
for fil in range(1,5):
	if fil%10==0:
		print(fil)
	new = misc.imread("b_w/"+str(fil))

	new=numpy.transpose(new)
	tot=[sum(new[i]) for i in range(252))]

	start,end=[0,251]

	while tot[start]<3:
		start+=1
	while tot[end]<3:
		end-=1
	diff=(end-start)//5

	for i in range(1,5)




xs=[x for x in range(len(ys))]
plt.plot(xs,ys)
plt.show()