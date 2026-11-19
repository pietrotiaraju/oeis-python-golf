# A002017

> Expansion of e.g.f. exp(sin(x)).
> — [OEIS A002017](https://oeis.org/A002017)

Offset 0: 1, 1, 1, 0, -3, -8, -3, 56, 217, 64, -2951, -12672, 5973, 309376, 1237173, -2917888, …

### Python 3 — 82 bytes

```python
P=Q=[n:=1]
while[print(P[-1])]:m=n=n+1;P,Q=Q,[s:=1]+[s:=s-x*(m:=m-2)**2for x in P]
```

**How it works**

- Put u = sin x. On functions of u, d/dx = cos x · d/du, and since
  cos²x = 1 − u² and (cos x)′ = −u, the second derivative has no square
  root left: D² = (1 − u²)·d²/du² − u·d/du =: L. So a(n) = Dⁿe^u at
  x = 0 (where u = 0 and cos x = 1) gives a(2m) = (Lᵐe^u)(0) and, as D
  commutes with L = D², a(2m + 1) = (Lᵐe^u)′(0).
- On Taylor coefficients, g(u) = Σ g_j u^j/j!, the operator is
  (Lg)_j = g_{j+2} − j²·g_j. Starting from e^u (all g_j = 1):
  G(0, j) = 1, G(m + 1, j) = G(m, j + 2) − j²·G(m, j), and
  a(2m + r) = G(m, r) for r = 0, 1.
- For n = 2m + r the list holds the anti-diagonal G(0, n), G(1, n − 2),
  …, G(m, r), so its last entry is a(n). Solving the recurrence from the
  far end gives the row for n + 2 as running sums: it starts with
  G(0, n + 2) = 1, and each next entry is the previous one minus
  (n − 2q)² times entry q of the old row. That is
  `[s:=1]+[s:=s-x*(m:=m-2)**2for x in P]`, with m walking n, n − 2, ….
- Even and odd n never mix, so `P` and `Q` hold rows n and n + 1 and swap
  every pass. The variable `n` is the row number plus 2 once `m=n=n+1`
  has run (it starts at 1, before row 0), so m starts two above the row
  number and the first weight `(m:=m-2)` is the row number itself.

**Notes**

- The binomial recurrence of y′ = cos(x)·y,
  a(n + 1) = Σⱼ (−1)ʲ C(n, 2j)·a(n − 2j), with `math.comb` is 107 bytes;
  summing the triangle T(n, k) = T(n − 2, k − 2) − k²T(n − 2, k) of
  n!·[xⁿ] sinᵏx/k! over k is 96.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002017), CC BY-SA 4.0.
