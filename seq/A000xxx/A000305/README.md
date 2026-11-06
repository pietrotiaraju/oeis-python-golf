# A000305

> Number of certain rooted planar maps.
> — [OEIS A000305](https://oeis.org/A000305)

Offset 1: 1, 4, 18, 89, 466, 2537, 14209, 81316, 473338, 2793454, 16674417, 100487896, 610549829, …

### Python 3 — 91 bytes

```python
n=0
while 1:n+=1;y=z=j=0;b=1;exec("x,y,z=y,z,b-z+y;b=b*(3*n+~j)//(j:=j+1);"*n);print(z-4*x)
```

**How it works**

- a(n) is the row sum of [A091665](https://oeis.org/A091665): T(n, k)
  counts the nonseparable planar maps with 2n + 1 edges and an outer face
  of 2k edges that a half turn leaves invariant (W. G. Brown, Canad. J.
  Math. 15 (1963), Table II). The OEIS gives
  T(n, k) = k/(2n−k+1)!·Σ_j (2j−k+1)(j−1)!(3n−k−j)!/((j−k+1)!(j−k)!(2k−j−1)!(n−j)!).
- The program uses the closed form

  a(n) = [t^(n−1)] (1−4t²)·(1+t)^(3n−1)/(1+t−t²),

  derived below from that formula. With R_j = [t^j] (1+t)^(3n−1)/(1+t−t²),
  dividing by 1 + t − t² is the recurrence R_j = C(3n−1, j) − R_{j−1} +
  R_{j−2}, and a(n) = R_{n−1} − 4·R_{n−3}.
- For each n, `exec` runs j = 0 … n−1 with the window `x,y,z` =
  R_{j−2}, R_{j−1}, R_j and the binomial `b`, stepped by
  `b*(3*n+~j)//(j:=j+1)` (3n − 1 − j over j + 1, exact). It starts from
  R_{−1} = R_{−2} = 0 (`y=z=0`); after the last pass z = R_{n−1} and
  x = R_{n−3}.

**Why the closed form holds**

- Put i = j − k and Cat(i) = (2i)!/(i!(i+1)!). The formula becomes
  T(n, k) = k/(2n−k+1)·Σ_i (k+2i+1)·Cat(i)·C(k+i−1, 2i)·C(3m+c−1, m),
  with m = n − k − i and c = k + 2i + 1.
- Let u = x(1+u)³ (u + 1 is the ternary-tree series). Lagrange inversion
  gives [x^m] (1+u)^c = c/(2m+c)·C(3m+c−1, m), and 2m + c = 2n − k + 1.
  So Σ_n T(n, k)·xⁿ = k·Σ_i Cat(i)·C(k+i−1, 2i)·x^(k+i)·(1+u)^(k+2i+1).
- Summing over k, then over i with the Catalan series, and using
  (1+u+u²)² − 4u²(1+u) = (1+u−u²)² for the square root, everything
  collapses to Σ a(n)·xⁿ = u(1+2u)/(1+u−u²). Lagrange inversion once more
  ([xⁿ] H(u) = [tⁿ] H(t)(1+t)^(3n)·(1−2t)/(1+t)) gives the closed form.
- So the program is exact for every n given the A091665 formula; the
  b-file confirms it for n ≤ 200.

**Notes**

- Alternatives: the A091665 double sum with factorials is about 190
  bytes; reading the coefficient of u(1+2u)/(1+u−u²) from one big integer
  (u iterated in base 8ⁿ, then a modular inverse with `pow`) is 105 bytes
  and much slower (117 terms in 30 s); an order-3 recurrence with quartic coefficients fits
  the data but is longer.
- Each term costs n steps, so the program prints about 1500 terms in 60 s
  (the 4300-digit limit is near n = 5190, much later).
- The b-file has 200 terms (n = 1 to 200); they print in about a second.
  The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000305), CC BY-SA 4.0.
