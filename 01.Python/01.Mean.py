import numpy as np
 A = np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5],
    [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
 B = A.T
 print B
 print(np.mean(B))
 print(np.mean(B,axis=0))
 print(np.mean(A,axis=1))
