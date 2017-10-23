from scipy import misc
from scipy import ndimage
from PIL import Image
import numpy
import matplotlib.pyplot as plt
#65*252

xs,ys=[[],[]]
pic=1
outp_dir="b_w/letters/"
digit_index="oABCDE"
for fil in range(1,50):
	if fil%10==0:
		print(fil)
	new = misc.imread("b_w/"+str(fil))

	new=numpy.transpose(new)
	tot=[sum(new[i])//255 for i in range(252)]
	for i in range(247):
		tot[i]=sum(tot[i:i+5])

	start,end=[0,251]

	while tot[start]<3:
		start+=1
	while tot[end]<3:
		end-=1
	diff=(end-start)//5

	prev=start
	img=Image.open("b_w/"+str(fil))
	for i in range(1,5):
		next=prev+diff
		arr=[]
		for j in range(next-7,next+15):
			arr.append([tot[j],j])
		limit=min(arr)
		digit=img.crop((prev,0,limit[1],64))
		digit=digit.resize((30,30),Image.ANTIALIAS)
		digit.save(outp_dir+str(fil)+digit_index[i]+'.png')
		prev=limit[1]
	digit=img.crop((prev,0,end,64))
	digit=digit.resize((30,30),Image.ANTIALIAS)
	digit.save(outp_dir+str(fil)+digit_index[i+1]+'.png')



# xs=[x for x in range(len(ys))]
# plt.plot(xs,ys)
# plt.show()