# import required libraries
from audioop import ulaw2lin
import glob
from termios import NL0
import h5py as h5
import numpy as np
import matplotlib.pyplot as plt



# Read H5 file
for filename in glob.glob("*.dat"):
	print('Reading file:')
	print(filename)
	f = open(filename, "r")
	t = []
	nL = []
	uL = []
	n0 = []
	u0 = []
	for data in f:
		t.append(data.split()[0])
		nL.append(data.split()[1])
		uL.append(data.split()[2])
		n0.append(data.split()[3])
		u0.append(data.split()[4])	

	plt.plot(t, nL, label=filename)
	#plt.xticks(np.arange(0, 1.2, 0.1))
	#plt.yticks(np.arange(0.3, 1.5, 0.05))
	plt.xlabel("t")
	plt.ylabel("nL")
 
	plt.title('My first graph!')
	plt.show()
f.close()