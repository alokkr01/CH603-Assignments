# Harmonic Vibrational Analysis
import numpy as np
'''
# Read the file
input_file = open('geom.txt', 'r')  # open the file
lines = input_file.readlines()          # read the content
input_file.close()                      # close the file
# print(lines)

# Store the input in list
temp_geom= []
for line in lines:
    v_line = line.strip()
    if (len(v_line) > 0):               # Check and remove blank lines
        temp_geom.append(v_line.split())  

# No of atoms
NATOMS = int(temp_geom.pop(0)[0]) 
print(NATOMS)
# print(temp_geom)

atomic_no=[]
for i in range(0, NATOMS):
    atomic_no.append(temp_geom[i][0])
# print(atomic_no)
'''
# Read Hessian Matrix
input_file = open('hessian.txt', 'r')  # open the file
lines = input_file.readlines()          # read the content
input_file.close()                      # close the file

# Store the input in list
temp_hess= []
for line in lines:
    v_line = line.strip()
    if (len(v_line) > 0):               # Check and remove blank lines
        temp_hess.append(v_line.split())  
# print(len(temp_hess))

# No of atoms
NATOMS = int(temp_hess.pop(0)[0]) 

hess = np.array(temp_hess, dtype=np.float32)
# print(hess)
hess_mat =[]
print(len(hess[:]))

# Reshaping the read hessian into a square matrix
'''
x1_x1 x1_y1 x1_z1    x1_x2 x1_y2 x1_z2    x1_x3 x1_y3 x1_z3
.
.
x3_x1 x3_y1 x3_z1    x3_x2 x3_y2 x3_z2    x3_x3 x3_y3 x3_z3
'''
for i in range(0,NATOMS*NATOMS): 
    hess_mat.append(np.reshape(hess[i*NATOMS:(i+1)*NATOMS], 3*NATOMS))
# print(hess_mat)

# at_mass = [16.0, 1.0, 1.0]
at_mass = [15.99491461957, 1.00782503223, 1.00782503223]

mat = []
for i in range(0, NATOMS):
    for j in range(0, NATOMS):
        mat.append(at_mass[i])
# print(mat)
mat_wt_1 = np.reshape(mat, 3*NATOMS)
mat_wt = []
for i in range(0,NATOMS*NATOMS):
    # print(mat_wt_1[i])
    mat_wt.append(mat_wt_1[i]*mat_wt_1)
# print("weight matrix:")
# print(mat_wt)
hess_mat_weighted = np.divide(hess_mat, np.sqrt(mat_wt))
# print(hess_mat_weighted)


# Diagonalizing the hessian matrix
hess_diag = np.linalg.eigh(hess_mat_weighted)
print("Diag")
print(hess_diag)
