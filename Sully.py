import os

i=5
if i >= 0:
    open("Sully_{}.py".format(i),"w").write(''.join([str(l)for l in open(os.path.basename(__file__),"r").readlines()]).replace('i={}'.format(i),'i={}'.format(i-1)))
    os.system("python3 Sully_{}.py".format(i))
