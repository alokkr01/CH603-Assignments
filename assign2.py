import numpy as np
from atomic_wt import weights

# reading geom.txt file
geom=np.genfromtxt('geom.txt',skip_header=1)
atomic_no=geom[:,0]
pos=geom[:,1:4]
NATOMS=len(pos)
NATOMS_geom=np.genfromtxt('geom.txt',skip_footer=NATOMS)

# reading hessian.txt file
hess=np.genfromtxt('hessian.txt',skip_header=1)
skip=((NATOMS*3)**2)/3
m=np.genfromtxt('hessian.txt',skip_footer=skip)
NATOMS_hess=int(hess[0][0])

# testing consistency of input files
if NATOMS_geom==NATOMS_hess:
	print('Consistent input files')

# convert hessian from rectangular to square 
rows=len(hess)
columns=len(hess[0])
hessian_matrix=[]
for i in range(int(rows/NATOMS)):
	A=[]
	for j in range(NATOMS):
		A.append(hess[(3*i)+j,:])
		B=np.asarray(A)
		C=B.flatten()
	hessian_matrix.append(C)
np.hm=np.asarray(hessian_matrix)


# creating weight factors with atomic weights
atomic_wt=weights(atomic_no)
np.full_row=np.repeat(atomic_wt,3)

np.mass=np.zeros((int(3*NATOMS),int(3*NATOMS)))
for i in range(int(3*NATOMS)):
    for j in range(int(3*NATOMS)):
        np.mass[i][j]=np.full_row[i]*np.full_row[j]
np.mass_sqrt=np.sqrt(np.mass)

# creating weighted hessian matrix
np.hm_norm=np.zeros((int(3*NATOMS),int(3*NATOMS)))
for i in range(int(3*NATOMS)):
    for j in range(int(3*NATOMS)):
        np.hm_norm[i][j]=np.hm[i][j]/np.mass[i][j]

# calculate eigen values
w,v=np.linalg.eig(np.hm_norm)
print(w)
