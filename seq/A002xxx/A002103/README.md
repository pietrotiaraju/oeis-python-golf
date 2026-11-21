# A002103

> Coefficients of expansion of Jacobi nome q in certain powers of (1/2)*(1 - sqrt(k')) / (1 + sqrt(k')).
> — [OEIS A002103](https://oeis.org/A002103)

Offset 0: 1, 2, 15, 150, 1707, 20910, 268616, 3567400, 48555069, 673458874, …

### Python 3 — 149 bytes

```python
n=0
while 1:
 X=8<<5*n;N=X**n;B=A=k=0;m=4*n+1
 while k*k<=n:B+=2*X**(k*k);A+=X**(k*k+k);k+=1
 print((pow(B-1,m,N*X)*pow(A,-m,N*X)+N//2)//N%X//m);n+=1
```

**How it works**

- **Definition.** Hanna's g.f. in the entry: Σ a(n)x^(4n+1) is the series
  reversion of φ(x) = (θ₃(x) − θ₃(−x))/(4θ₃(x⁴)) = Σ_(k≥0) x^((2k+1)²)/θ₃(x⁴).
  This is Jacobi's q = ε + 2ε⁵ + 15ε⁹ + … in terms of
  ε = ½(1 − √k′)/(1 + √k′) (Fricke; comments in the entry).
- **Lagrange inversion.** (2k+1)² = 4k(k+1) + 1, so φ(x) = x·ψ(x⁴) with
  ψ = A/B, A(t) = Σ_(k≥0) t^(k(k+1)), B(t) = 1 + 2Σ_(k≥1) t^(k²). Then
  a(n) = [x^(4n)](x/φ)^(4n+1)/(4n+1) = c_n/m, where m = 4n + 1 and
  c_i = [t^i](B/A)^m.
- **One big integer.** t ↦ X is a ring map from series mod t^(n+1) to
  integers mod X^(n+1), and A(X) ≡ 1 (mod X) is invertible there, so
  V = B(X)^m·A(X)^(−m) ≡ Σ_(i≤n) c_i·X^i (mod X^(n+1)) (`pow` with
  exponent −m inverts). Terms with k² > n vanish mod X^(n+1) and are not
  summed.
- **Reading c_n.** The c_i can be negative. If every |c_i| < X/2 − 1, the
  part below X^n is less than X^n/2 in absolute value, so
  ⌊(V + X^n/2)/X^n⌋ ≡ c_n (mod X) and `%X` gives c_n.
- **Size of X.** Coefficientwise |B| ≤ (1+t)/(1−t) and
  |1/A| ≤ 1/(1 − t²/(1−t)) (A − 1 ≤ t² + t³ + …), so
  |B/A| ≤ M(t) = (1+t)/(1−t−t²). For i ≤ n, |c_i| ≤ M(r)^m/r^n at any
  0 < r < 0.6; at r = 1/10, M < 1.236 and M⁴·10 < 23.4 < 2^4.55, so
  |c_i| < 1.24·2^(4.55n) < 2^(5n+2) − 1. X = 2^(5n+3) = `8<<5*n` is
  enough.

**Notes**

- It is exact for every n: the bound above is proved, not observed.
- The integers have about 5n² bits and `pow` reduces modulo X^(n+1) at
  each step, so a term costs roughly n^3.2: about 150 terms in 20 s here.
  The bar is 150 terms in 60 s; the b-file has 801 (n = 0 to 800).
- A sparse Miller recurrence for B^m and A^(−m) (only about √n nonzero
  coefficients each) is much faster but about 100 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 149 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002103), CC BY-SA 4.0.
