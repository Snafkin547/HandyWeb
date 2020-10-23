def SGtax(SG):
     x=0
     if SG<20000:
       x=  0
     elif SG>=20000 and SG<30000:
       x= (0+0.02*(SG-20000))
     elif SG>=30000 and SG<40000:
       x= (200+0.035*(SG-30000))
     elif SG>=40000 and SG<80000:
       x=  (550+0.07*(SG-40000))
     elif SG>=80000 and SG <120000:
       x=  (3350+0.115*(SG-80000))
     elif SG>=120000 and SG<160000:
       x=  (7950+0.15*(SG-120000))
     elif SG>=160000 and SG<200000:
       x=  (13950+0.18*(SG-160000))
     return x