import numpy as np
import math as m

geom=np.genfromtxt('geom.txt',skip_header=1)
atomic_no=geom[:,0]
pos=geom[:,1:4]
n=np.genfromtxt('geom.txt',skip_footer=3)
hess=np.genfromtxt('hessian.txt',skip_header=1)
m=np.genfromtxt('hessian.txt',skip_footer=27)
if m==n:
	print('Consistent input files')

rows=len(hess)
columns=len(hess[0])

hessian_matrix=[]
for i in range(int(rows/3)):
	A=[]
	for j in range(3):
		A.append(hess[(3*i)+j,:])
		B=np.asarray(A)
		C=B.flatten()
	hessian_matrix.append(C)
np.hm=np.asarray(hessian_matrix)
#print(np.hm)

np.atomic_wt=[15.99491461957, 1.00782503223, 1.00782503223]
np.full_row=np.repeat(np.atomic_wt,3)
np.mass=np.zeros((int(n**2),int(n**2)))
for i in range(int(n**2)):
    for j in range(int(n**2)):
        np.mass[i][j]=np.full_row[i]*np.full_row[j]
np.mass_sqrt=np.sqrt(np.mass)
#print(np.mass_sqrt)

np.hm_norm=np.zeros((int(n**2),int(n**2)))
for i in range(int(n**2)):
    for j in range(int(n**2)):
        np.hm_norm[i][j]=np.hm[i][j]/np.mass[i][j]

#print(np.hm_norm)
w,v=np.linalg.eig(np.hm_norm)
print(w)

	
