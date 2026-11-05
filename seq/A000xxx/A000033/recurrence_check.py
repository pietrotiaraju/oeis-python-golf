"""Prove the recurrence behind A000033's program, with sympy (Zeilberger's method).

With F(n, k) = (-1)^k (2n-k-1)! (n-k)! / ((2n-2k)! (k-2)!) for 2 <= k <= n (0 otherwise),
a(n) = n b(n) where b(n) = sum_k F(n, k) (A000426). The claim is, for n >= 5,

    2 b(n) - (2n-5) b(n-1) - (3n-9) b(n-2) - (2n-7) b(n-3) - 2 b(n-4) = -2 (-1)^n.

G(n, k) = R(n, k) F(n, k) below is the certificate: for 2 <= k <= n-4, where every F in the
left side is given by the factorial formula, the left side's summand equals
G(n, k+1) - G(n, k). Summing k = 2..n-4 telescopes to G(n, n-3) - G(n, 2), G(n, 2) = 0, and
the terms k = n-3..n, where some F(n-i, k) are past the end of their row, are added by hand.
"""
import sympy as sp

n, k = sp.symbols("n k")
p = [2, -(2*n - 5), -(3*n - 9), -(2*n - 7), -2]       # coefficients of b(n), ..., b(n-4)


def down(m):
    """F(m-1, k) / F(m, k)."""
    return 2*(2*m - 2*k - 1) / ((2*m - k - 1)*(2*m - k - 2))


up = -2*(2*n - 2*k - 1) / ((2*n - k - 1)*(k - 1))      # F(n, k+1) / F(n, k)
ratio = [sp.Integer(1)]                                 # F(n-i, k) / F(n, k)
for i in range(1, 5):
    ratio.append(ratio[-1]*down(n - i + 1))
summand = sum(p[i]*ratio[i] for i in range(5))         # left side's k-th term / F(n, k)

S = (k**6 - 10*k**5*n + 16*k**5 + 40*k**4*n**2 - 132*k**4*n + 113*k**4 - 80*k**3*n**3
     + 404*k**3*n**2 - 714*k**3*n + 415*k**3 + 80*k**2*n**4 - 536*k**2*n**3 + 1460*k**2*n**2
     - 1862*k**2*n + 834*k**2 - 32*k*n**5 + 240*k*n**4 - 856*k*n**3 + 1880*k*n**2 - 2272*k*n
     + 1183*k + 32*n**5 - 224*n**4 + 528*n**3 - 480*n**2 + 122*n + 6)
R = 2*(k - 2)*S / sp.prod([2*n - k - j for j in range(1, 8)])

# 1. Telescoping: summand = G(n, k+1)/F(n, k) - G(n, k)/F(n, k). R has no pole for
#    2 <= k <= n-3 once n >= 5 (2n-k-7 >= n-4), and down/up have none for k <= n-4.
assert sp.cancel(R.subs(k, k + 1)*up - R - summand) == 0

# 2. Ends, divided by (-1)^n. For k = n-s, F(n-i, n-s) (-1)^n is (-1)^s (s-i)!/(2s-2i)!
#    times (n+s-2i-1)!/(n-s-2)!, the rising factorial rf(n-s-1, 2s-2i+1).
def Fend(i, s):
    return (-1)**s*sp.factorial(s - i)/sp.factorial(2*s - 2*i)*sp.rf(n - s - 1, 2*s - 2*i + 1)


assert R.subs(k, 2) == 0                                # G(n, 2) = 0
top = R.subs(k, n - 3)*Fend(0, 3)                       # G(n, n-3) (-1)^n
ends = sum(p[i]*Fend(i, s) for s in range(4) for i in range(s + 1))
assert sp.simplify(sp.expand_func(top + ends) + 2) == 0
print("recurrence proved for n >= 5")

# 3. Sanity: the factorial sum itself, and the program's start b(1..4) = 0, 1, 1, 1.
from math import factorial as f
b = [None] + [sum((-1)**j*f(2*m - j - 1)*f(m - j)//(f(2*m - 2*j)*f(j - 2)) for j in range(2, m + 1))
              for m in range(1, 401)]
assert b[1:5] == [0, 1, 1, 1]
for m in range(5, 401):
    lhs = 2*b[m] - (2*m - 5)*b[m - 1] - (3*m - 9)*b[m - 2] - (2*m - 7)*b[m - 3] - 2*b[m - 4]
    assert lhs == -2*(-1)**m, m
print("and checked directly for n = 5..400")
