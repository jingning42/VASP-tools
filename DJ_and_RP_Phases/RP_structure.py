import sys

# this script create POSCAR of Ruddleson-Popper phases that have the general formula A(n+1)BnO(3n+1).
# usage python3 RP_structure.py A B O n

A, B, O = sys.argv[1:4]
n = int(sys.argv[4])

# assume the ratio between l and d is k, l = k*d
k = 1.25
n_layer = 4*n+2*k
d = 1.0/n_layer
l = k*d

# lattice parameter
a = 4.0

# number of elements
elem = {
        A: 2*(n+1),
        B: 2*n,
        O: 2*(3*n+1),
        }

fname = '%s%d%s%d%s%d_RP_POSCAR_unit.vasp'%(A, n+1, B, n, O, 3*n+1)
with open(fname, 'w') as f:
    f.write('%s\n'%fname)
    f.write('1.0\n')
    f.write('%18.10f %18.10f %18.10f\n'%(a, 0, 0))
    f.write('%18.10f %18.10f %18.10f\n'%(0, a, 0))
    f.write('%18.10f %18.10f %18.10f\n'%(0, 0, (2*n+k)*a))
    f.write('%5s %5s %5s\n'%(A, B, O))
    f.write('%5d %5d %5d\n'%(elem[A], elem[B], elem[O]))
    f.write('Direct\n')
    # A
    for i in range(n+1):
        f.write('%18.10f %18.10f %18.10f\n'%(0.5, 0.5, (-n+2*i)*d ))
        f.write('%18.10f %18.10f %18.10f\n'%(0.0, 0.0 , (n+2*i)*d+l))

    # B
    for i in range(n):
        f.write('%18.10f %18.10f %18.10f\n'%(0.0, 0.0 , (1-n+2*i)*d  ))
        f.write('%18.10f %18.10f %18.10f\n'%(0.5, 0.5, (n+1+2*i)*d+l))

    # O
    for i in range(n):
        f.write('%18.10f %18.10f %18.10f\n'%(0.0, 0.5, (1-n+2*i)*d  ))
        f.write('%18.10f %18.10f %18.10f\n'%(0.5, 0.0 , (1-n+2*i)*d  ))
        f.write('%18.10f %18.10f %18.10f\n'%(0.0, 0.5, (n+1+2*i)*d+l))
        f.write('%18.10f %18.10f %18.10f\n'%(0.5, 0.0 , (n+1+2*i)*d+l))
    
    for i in range(n+1):
        f.write('%18.10f %18.10f %18.10f\n'%(0.0, 0.0 , (-n+2*i)*d ))
        f.write('%18.10f %18.10f %18.10f\n'%(0.5, 0.5, (n+2*i)*d+l))
