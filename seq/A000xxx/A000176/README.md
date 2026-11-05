# A000176

> Generalized tangent numbers d_(n,2).
> — [OEIS A000176](https://oeis.org/A000176)

Offset 1: 2, 11, 46, 128, 272, 522, 904, 1408, 2160, 3154, …

### Python 3 — 126 bytes

```python
D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*(3*a*a-u*u)-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
```

**How it works**

- For n ≥ 2 the OEIS comment gives a(n) = 3!·(2n/π)⁴·L(4)/√n with
  L(4) = Σ_{k odd} χ(k)/k⁴. The character that fits the data is the Jacobi
  symbol χ(k) = (n|k), the even one Shanks uses for the d-numbers: it gives
  all 10000 b-file terms, while (−n|k), as the comment writes it, gives
  11.267… for n = 2. For n = 1 the formula gives d(1) = 1, and a(1) = 2 is
  the tangent number T₂ (Shanks's d_(1,m) are the tangent numbers, with a
  different factor of 2, hence the comment's "for a > 1").
- Gauss sums turn the character into cosines. For odd k prime to n,
  G(k; 4n) = Σ_{y mod 4n} e^{2πiky²/4n} = (1+i)·ε_k⁻¹·2√n·(n|k), so
  Σ_{y mod 2n} cos(πky²/2n) = √n·(n|k). The odd-k Fourier series of the
  Euler polynomial, Σ_{k odd} cos(πkx)/k⁴ = π⁴E₃(x)/24 on [0, 1]
  (DLMF 24.8.5), then sums over k in closed form. π and √n cancel, and each
  y leaves the integer g(u) = u(3n² − u²), where u = |y² mod 4n − 2n| − n.
  This is E₃ after folding x into [0, 1] and using E₃(1−x) = −E₃(x).
- The sum U(n) = ½·Σ_y g(u) also picks up the odd k that share a factor e
  with n: there G(k; 4n) = e·G(k/e; 4n/e), and that gives
  U(n) = Σ_{odd e | n} d(n/e), with d the formula value (d(1) = 1,
  d(n) = a(n) for n ≥ 2). The program peels the divisors off again:
  d(n) = U(n) − Σ_{odd e | n, e > 1} d(n/e).
- `D` holds 2·d(n), so neither part needs a division: each pass sums
  g(u) − D[n/y] over y = 2 … 2n+1. That is a full residue system mod 2n,
  and its odd members > 1 that divide n are exactly the e above:
  `y%2>a%y` means "y odd and y | n", and for y > n the index is 0 and
  D[0] = 0. Starting at 2 keeps out y = 0 (division by zero) and y = 1
  (D[n] is not there yet).
- `D[a]>>1%a` halves 2·d(n) for n > 1 and leaves it alone for n = 1, since
  1%1 = 0: the stored 2·d(1) = 2 is exactly T₂.

**Notes**

- Exact integer arithmetic, correct for every n by the identities above;
  the formula was also checked against all 10000 terms of the b-file. Each
  term takes O(n) steps: about 6000 terms in 60 s here, the whole b-file in
  about 140 s. The bar is 4500 terms in 60 s.
- Summing the Bernoulli series B₄({y²/4n}) and B₄({y²/2n}) instead of E₃
  avoids the `abs` but needs two moduli and about 30 more bytes. Writing the
  divisor sum separately, `sum(D[a//e]for e in range(3,a+1,2)if a%e<1)`,
  costs about 25 more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 126 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000176), CC BY-SA 4.0.
