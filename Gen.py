
import numpy as np
import random

""" parameters to change """
#expected output: x1,x5,not(x6),not(x7),not(x8),x9
lits = [2,3,3,3,2,1,1,1,2,3,3,3] #2:pos 1:neg 3:none
rounds = 200

train = []
for i in range(rounds):
    line = []
    y = 1
    for j in range(len(lits)):
        cur = random.choice([0,1])
        line.append(cur)
        if((cur==0 and lits[j]==2) or (cur==1 and lits[j]==1)):
            y = 0;
    line.append(y)
    train.append(line)
    
np.savetxt("example2.txt",train,"%i")