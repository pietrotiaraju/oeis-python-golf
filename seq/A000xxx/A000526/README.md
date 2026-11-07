# A000526

> Number of partially labeled trees with n nodes (5 of which are labeled).
> — [OEIS A000526](https://oeis.org/A000526)

Offset 5: 125, 1296, 8716, 47787, 232154, 1040014, 4395772, 17781210, 69498964, 264248924, …

### Python 3 — 186 bytes

```python
*r,n=0,1,1,2,4,-3
while 1:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;X=99**-n;T=0;[T:=T*X+c for c in r];U=X**-~-n-T;print(T**5*(((15*T+85*U)*T+171*U*U)*T+125*U**3)//U**7%X)
```

**What is counted**

- Free (unrooted) trees with n nodes, five of them labeled 1, …, 5 and the
  rest unlabeled. With R(x) the rooted-tree series
  ([A000081](../A000081/)) the OEIS generating function (Riordan 1958,
  p. 138) is R⁵(125 − 204R + 118R² − 24R³)/(1 − R)⁷. Writing
  125 − 204R + 118R² − 24R³ in R and 1 − R gives
  P = 15R⁸/(1−R)⁷ + 85R⁷/(1−R)⁶ + 171R⁶/(1−R)⁵ + 125R⁵/(1−R)⁴, that is
  R·B⁴(125 + 171B + 85B² + 15B³) with B = R/(1 − R) (A000107).

**How it works**

- The program is the [A000524](../A000524/) one with this generating
  function: the Euler-transform recurrence appends r_m (m = 1 − n), Horner
  in base X gives T = X^m·R̂(1/X), and U = X^m − T = X^m·(1 − R̂(1/X)).
  The numerator has degree 8 and the denominator degree 7, so the factor
  X^m is already there:

  X^m·P̂(1/X) = T⁵(15T³ + 85T²U + 171TU² + 125U³)/U⁷,

  and its integer part mod X is a(m). In T and U the cubic has small
  positive coefficients and needs no V, 3 bytes under the form in
  V = X^m.
- The seed `*r,n=0,1,1,2,4,-3` holds r₀, …, r₄ = 0, 1, 1, 2, 4 (rooted
  trees with up to 4 nodes) and the matching counter, so the first pass
  appends r₅ and prints a(5) instead of the zeros a(2), a(3), a(4).
- The bounds. P is a power series in R with nonnegative coefficients, so
  0 ≤ p̂_j ≤ a(j). Choosing a free tree and five of its nodes in order
  covers every case, and free trees are at most rooted ones, so
  a(j) ≤ j⁵·r_j ≤ j⁵·4^(j−1) (r_j ≤ Catalan(j−1), via plane embeddings).
  With X = 99^(m−1) and m ≥ 5 the tail Σ_{j>m} p̂_j X^(m−j) is at most
  Σ_{i≥1} (m+i)⁵·4^(m+i−1)/99^((m−1)i) ≤ 6⁵·4⁵/99⁴ + … < 0.09, and
  a(m) ≤ m⁵·4^(m−1) < X, so the digit read is exact.

**Notes**

- In V = X^m, `T**5*(((125*V-204*T)*V+118*T*T)*V-24*T**3)//(V-T)**7%X`
  with `V=X**-~-n`: 189 bytes. The first entry evaluated R at
  B = m^m + 1 with `pow(1-S,-7,M)` and an `if m>=5:` block: 218 bytes.
- Exact integer arithmetic, so the program is right for every n.
- About 185 terms in 60 s here; the whole b-file takes a little over 60 s.
- a(n) grows like 2.96^n, so the 4300-digit int-to-str limit is out of
  reach.
- The b-file has 196 terms (up to a(200)); the bar is 30 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 218 | first entry |
| 2026-11-07 | Python 3 | 186 | evaluate at x = 1/X and floor, seeded tree counts |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000526), CC BY-SA 4.0.
