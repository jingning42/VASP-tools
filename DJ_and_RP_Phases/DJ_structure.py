import sys

# this script creates POSCAR of Dion-Jacobson phases that have the general formula M+1A(n-1)BnO(3n+1).
# usage python3 DJ_structure.py M A B O n

M, A, B, O = sys.argv[1:5]
n = int(sys.argv[5])

# assume the ratio between l and d is k, l = k*d
k = 2.0
n_layer = 2*n+1*k
d = 1.0/n_layer
l = k*d

# lattice parameter
a = 4.0

# number of elements
elem = {
    M: 1,
    A: (n-1),
    B: n,
    O: (3*n+1),
}

fname = '%s%s%d%s%d%s%d_DJ_POSCAR_unit.vasp' % (M, A, n-1, B, n, O, 3*n+1)
with open(fname, 'w') as f:
    f.write('%s\n' % fname)
    f.write('1.0\n')
    f.write('%18.10f %18.10f %18.10f\n' % (a, 0, 0))
    f.write('%18.10f %18.10f %18.10f\n' % (0, a, 0))
    f.write('%18.10f %18.10f %18.10f\n' % (0, 0, (n+0.5*k)*a))
    f.write('%5s %5s %5s %5s\n' % (M, A, B, O))
    f.write('%5d %5d %5d %5d\n' % (elem[M], elem[A], elem[B], elem[O]))
    f.write('Direct\n')
    # M
    f.write('%18.10f %18.10f %18.10f\n' % (0.5, 0.5, 0.5))
    # A
    for i in range(n-1):
        f.write('%18.10f %18.10f %18.10f\n' % (0.5, 0.5, (-n+2+2*i)*d))

    # B
    for i in range(n):
        f.write('%18.10f %18.10f %18.10f\n' % (0.0, 0.0, (1-n+2*i)*d))

    # O
    for i in range(n):
        f.write('%18.10f %18.10f %18.10f\n' % (0.0, 0.5, (1-n+2*i)*d))
        f.write('%18.10f %18.10f %18.10f\n' % (0.5, 0.0, (1-n+2*i)*d))

    for i in range(n+1):
        f.write('%18.10f %18.10f %18.10f\n' % (0.0, 0.0, (-n+2*i)*d))
