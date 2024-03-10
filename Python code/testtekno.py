import pandas as pd
prod=pd.read_csv('ninja_pv_50.2900_5.5600_uncorrected (3).csv')
vec = [10, 20, 0, 0, 0, 0, 40,50]  # Example vector
cons=[5,5,5,5,10,10,20,20]

jour = 0  # Initialize variable to store sum during the day
nuit = 0  # Initialize variable to store sum during the night
z = 1  # Initialize z variable
y=1

consjour=0
consnuit=0

for i in range(len(vec)):
    if (i+1) % 7 == 0:
        z = 0
    if (i+1) % 22 == 0:
        z = 1
    if z == 0:
        jour += vec[i]
    if z == 1:
        nuit += vec[i]

for i in range(len(cons)):
    if (i+1) % 7 == 0:
        y = 0
    if (i+1) % 22 == 0:
        y = 1
    if y == 0:
        consjour += cons[i]
    if y == 1:
        consnuit += cons[i]
Savingsnuit=-(consnuit-nuit)*0.25*15
Savingsjour=-(consjour-jour)*0.25*15
print(Savingsjour)
print(Savingsnuit)
injday=0
injnuit=0
retday=0
retnuit=0
for i in range(len(vec)):
    if (i+1) % 7 == 0:
        z=1
    if (i+1) % 22 ==0:
        z=0
    if vec(i+1)>cons(i+1) and z==1:
        injday+=vec(i+1)-cons(i+1)
    if vec(i+1)>cons(i+1) and z==0:
        injnuit+=vec(i+1)>cons(i+1)
    if vec(i+1)<cons(i+1) and z==1:
        retday+=cons(i+1)-vec(i+1)
    if vec(i+1)>cons(i+1) and z==0:
        retnuit+=cons(i+1)-vec(i+1)



