from scipy import misc
from scipy import ndimage
from PIL import Image
import numpy
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join 
from sklearn.cluster import KMeans
#65*252



xs,ys=[[],[]]
pic=1
outp_dir="b_w/letters/"
train_dir="b_w/good/"
onlyfiles = [f for f in listdir(train_dir) if isfile(join(train_dir, f))]
# print(onlyfiles)


t_data=[]
min_err=10**8
for coeff in range(10000,10001):
	for fil in onlyfiles:
		img=misc.imread(train_dir+str(fil))
		vec=[0,0]
		for i in range(len(img)):
			for j in range(len(img[i])):
				if img[i][j]>0:
					img[i][j]=1
					vec[0]+=1
					vec[1]+=i*j
		t_data.append(vec)


	# print(t_data)
	X=numpy.array(t_data)
	x,y=[[],[]]
	for row in t_data:
		x.append(row[0])
		y.append(row[1])
	for KM in range(5,6):
		kmeans=KMeans(n_clusters=KM)
		kmeans.fit(X)

		centroids=kmeans.cluster_centers_
		labels=kmeans.labels_
		err=0
		for i in range(len(t_data)):
			err+=(t_data[i][1]-centroids[labels[i]][1])**2
		err=err**0.5
		min_err=min(min_err,err)
		print('cluster',KM,'coeff',coeff,'error',err)
		plt.scatter(x,y)
		plt.show()