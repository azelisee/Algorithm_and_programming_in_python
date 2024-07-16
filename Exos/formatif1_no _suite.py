# formatif 1, no2-iii
n=int(input("Saisissez un entier:"))
if n<10:
    x=n**2-n//3
else:
    x=n**0.5-n%3
print("\n\tx=",x)
# formatif 1, no2-iv
r=float(input("Saisissez un reel:"))
if r<0:
    y=1-3*r
elif r == 0:
    y=2
else:
    y=3*r-1
print("\n\ty=",y)

