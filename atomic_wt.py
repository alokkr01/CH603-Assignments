# This function takes atomic number as input and returns its corresponding atomic mass as a numpy array

def weights(no):
    import numpy as np

    weights=open('weights.txt')
    weights_content=weights.readlines()
    weights.close()

    mod_weights=[]
    for line in weights_content:
      v_line=line.rstrip()
      f=v_line.split()
      mod_weights.append(f)

    wt=np.zeros(len(no))
    for i in range(len(no)):
        for j in range(len(mod_weights)):
             if no[i]==int(mod_weights[j][0]):
                 break
        wt[i]=mod_weights[j][1]
    return wt

