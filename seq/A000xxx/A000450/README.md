# A000450

> a(n) = A058057(n,n-4).
> — [OEIS A000450](https://oeis.org/A000450)

Offset 4: 1, 10, 50, 385, 3130, 28764, 291900, 3249210, 39367395, 515874470, …

A058057 lists the hit polynomials of the straight ménage problem from the
highest power down, so a(n) counts the permutations p of 1, …, n with
exactly 4 hits, where i is a hit when p(i) = i or p(i) = i + 1.

### Python 3 — 86 bytes

```python
a=b=0;c=1;n=3
while[print(abs(8*n*(c-a)+8*a+~b*6-n*n+n)//12)]:a,b,c=b,c,n*(b-c)-a;n+=1
```

**How it works**

- The hits lie on the 2n − 1 cells (i, i) and (i, i + 1), whose K-th rook
  number is C(2n − K, K). Inclusion–exclusion gives the hit polynomial
  Σ_K C(2n−K, K)(n−K)!(t − 1)^K, so
  a(n) = Σ_K (−1)^K C(K, 4)C(2n−K, K)(n−K)!, and its constant term W_n is
  [A000271](../A000271/).
- Generating function: C(2m+K, K)C(K, 4) = C(2m+4, 4)C(2m+K, K−4) and
  Σ_K C(2m+K, K−4)(−z)^K = z⁴/(1+z)^(2m+5), so with m = n − K,
  Σ a(n)zⁿ = z⁴/(1+z)⁵·Σ_m C(2m+4, 4)m!·tᵐ with t = z/(1+z)². The same
  computation with C(K, 0) gives G = Σ W_n zⁿ = F(t)/(1+z), F(t) = Σ m!·tᵐ.
- With (m+1)_j = (m+1)(m+2)⋯(m+j), C(2m+4, 4) = (2/3)(m+1)₄ −
  (10/3)(m+1)₃ + (5/2)(m+1)₂ (the values at m = −1, …, −4 fix the
  coefficients). Since m!(m+1)_j = (m+j)!, each part is a shifted F:
  Σ_m (m+j)!·tᵐ = t^(−j)(F − Σ_{i<j} i!·tⁱ). Back in z the F parts give
  G·((2/3)(1+z)⁴ − (10/3)z(1+z)² + (5/2)z²) = G·(4 − 4z − z² − 4z³ + 4z⁴)/6.
- The leftover parts are a polynomial of degree 3 plus
  −(1/2)z²/(1+z) + (1/6)z³/(1+z)³, whose zⁿ coefficient is
  −(−1)ⁿ(n² − 3n + 8)/12. So for n ≥ 4
  12a(n) = 2(4W_n − 4W_{n−1} − W_{n−2} − 4W_{n−3} + 4W_{n−4})
  − (−1)ⁿ(n² − 3n + 8).
- The recurrence W_q = (q−1)(W_{q−1} + W_{q−2}) + W_{q−3} (q ≥ 3, proved
  on the A000271 page) removes W_n and W_{n−4}:
  12a(n) = 8(n−1)W_{n−1} + 6W_{n−2} − 8(n−2)W_{n−3} − (−1)ⁿ(n² − 3n + 8).
- The program runs X_q = (−1)^q·W_q, for which the recurrence reads
  X_{q+1} = q(X_{q−1} − X_q) − X_{q−2}. At counter n the state is
  (a, b, c) = (−X_{n−2}, −X_{n−1}, −X_n), so the update is `n*(b-c)-a`,
  and n = 3 with W_1 = W_2 = 0, W_3 = 1 gives `a=b=0;c=1`.
- Print: with N = n + 1, `~b*6` is −6b − 6 and n² − n + 6 = N² − 3N + 8,
  so the printed expression is 8n·c − 8(n−1)a − 6b − (N² − 3N + 8)
  = (−1)^N·12a(N). `abs` drops the sign and `//12` is exact, so the loop
  prints a(4), a(5), … from n = 3.

**Notes**

- Measured alternatives: the five-term window form above with constant
  coefficients, `a=1;b=c=0;d=-1;e=3;n=4` and a five-variable update,
  104 bytes; the previous direct sum with `perm` and `comb`, 109.
- Exact integer arithmetic, so the program is right for every n ≥ 4
  (the identities were also checked against the sum up to n = 200).
- The whole b-file prints in about 0.2 s here. The b-file has 447 terms
  (up to a(450)); the bar is the whole b-file in 60 s.
- a(1558) has 4299 digits and a(1559) more than 4300, so the int-to-str
  limit of Python 3.11+ stops the printing there.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |
| 2026-11-06 | Python 3 | 109 | use one-argument perm for the factorial |
| 2026-11-07 | Python 3 | 86 | three-term W recurrence with sign-alternated state and abs |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000450), CC BY-SA 4.0.
