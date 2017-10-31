import os

for i in "abcdefghijklmnopqrstuvwxyz":
	if not os.path.isdir("b_w/categorised/"+i):
		os.makedirs("b_w/categorised/"+i)