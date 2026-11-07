# A000525

> Number of partially labeled rooted trees with n nodes (4 of which are labeled).
> — [OEIS A000525](https://oeis.org/A000525)

Offset 4: 64, 625, 4016, 21256, 100407, 439646, 1823298, 7258228, 27983518, 105146732, …

### Python 3 — 185 bytes

```python
*r,n=0,1,1,2,-2
while 1:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;X=99**-n;T=0;[T:=T*X+c for c in r];V=X**-~-n;print(V*T**4*(((64*V-79*T)*V+36*T*T)*V-6*T**3)//(V-T)**7%X)
```

**What is counted**

- Rooted trees with n nodes, four of them labeled 1, 2, 3, 4 and the rest
  unlabeled. With R(x) the rooted-tree series ([A000081](../A000081/)) the
  OEIS generating function (Riordan 1958, p. 134) is
  R⁴(64 − 79R + 36R² − 6R³)/(1 − R)⁷. In B = R/(1 − R) (the series of
  rooted trees with one marked node, A000107) it is the polynomial
  B⁴(64 + 113B + 70B² + 15B³), as for the two-label case on the
  [A000524](../A000524/) page.

**How it works**

- The program is the [A000524](../A000524/) one with this generating
  function: the Euler-transform recurrence appends r_m (m = 1 − n), Horner
  in base X gives T = X^m·R̂(1/X) and V = X^m, and

  X^m·P̂(1/X) = V·T⁴(64V³ − 79V²T + 36VT² − 6T³)/(V − T)⁷,

  whose integer part mod X is a(m). The cubic is written in Horner form,
  `((64*V-79*T)*V+36*T*T)*V-6*T**3`, 4 bytes under the same cubic in
  U = V − T.
- The seed `*r,n=0,1,1,2,-2` holds r₀, …, r₃ = 0, 1, 1, 2 (rooted trees
  with up to 3 nodes) and the matching counter, so the first pass appends
  r₄ and prints a(4); a(2) and a(3) would be zeros. It is 6 bytes over the
  plain `r=[n:=0,1]`, less than a print test.
- The bounds. P = 64B⁴ + 113B⁵ + 70B⁶ + 15B⁷ is a power series in R with
  nonnegative coefficients, so 0 ≤ p̂_j ≤ a(j). Choosing a tree and four
  of its nodes in order covers every case, so a(j) ≤ j⁴·r_j ≤ j⁴·4^(j−1)
  (r_j ≤ Catalan(j−1), via plane embeddings). With X = 99^(m−1) and m ≥ 4,
  the tail Σ_{j>m} p̂_j X^(m−j) is at most
  Σ_{i≥1} (m+i)⁴·4^(m+i−1)/99^((m−1)i) ≤ 5⁴·4⁴/99³ + … < 0.17, and
  a(m) ≤ m⁴·4^(m−1) < X, so the digit read is exact.

**Notes**

- The modular version on this frame, `S**4*(64-79*S+36*S*S-6*S**3)` times
  `pow(1-S,-7,X**len(r))` with a reversed Horner: 190 bytes. The first
  entry used that route with B = m^m + 1 and an `if m>=4:` block:
  214 bytes.
- Exact integer arithmetic, so the program is right for every n.
- About 190 terms in 60 s here.
- a(n) grows like 2.96^n, so the 4300-digit int-to-str limit is out of
  reach.
- The b-file has 21 terms (up to a(24)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 214 | first entry |
| 2026-11-07 | Python 3 | 185 | evaluate at x = 1/X and floor, seeded tree counts |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000525), CC BY-SA 4.0.
