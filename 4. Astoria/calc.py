import math

r_pt, u_r = 109.0, 1.0
r_ni = 113.0
r_c = 100.0

def series(r1, r2, r3=0):
    val = r1 + r2 + r3
    err = math.sqrt(u_r**2 + u_r**2 + (u_r**2 if r3 else 0))
    return val, err

def parallel(r1, r2, r3=0):
    if r3 == 0:
        val = 1/(1/r1 + 1/r2)
        dr1 = (val/r1)**2
        dr2 = (val/r2)**2
        err = math.sqrt(dr1*u_r**2 + dr2*u_r**2)
        return val, err
    else:
        val = 1/(1/r1 + 1/r2 + 1/r3)
        dr1 = (val/r1)**2
        dr2 = (val/r2)**2
        dr3 = (val/r3)**2
        err = math.sqrt(dr1*u_r**2 + dr2*u_r**2 + dr3*u_r**2)
        return val, err

print("Series Ni+C:", series(r_ni, r_c))
print("Series C+Pt:", series(r_c, r_pt))
print("Series Ni+Pt:", series(r_ni, r_pt))

print("Parallel C+Pt:", parallel(r_c, r_pt))
print("Parallel Pt+Ni:", parallel(r_pt, r_ni))
print("Parallel C+Pt+Ni:", parallel(r_c, r_pt, r_ni))
