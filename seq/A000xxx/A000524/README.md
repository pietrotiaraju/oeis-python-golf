# A000524

> Number of rooted trees with n nodes, 2 of which are labeled.
> — [OEIS A000524](https://oeis.org/A000524)

Offset 2: 2, 9, 34, 119, 401, 1316, 4247, 13532, 42712, 133816, …

### Python 3 — 153 bytes

```python
r=[n:=0,1]
while 1:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;X=99**-n;T=0;[T:=T*X+c for c in r];V=X**-~-n;print(V*T*T*(2*V-T)//(V-T)**3%X)
```

**What is counted**

- Two nodes carry the labels 1 and 2, the other n − 2 are unlabeled. Let
  R(x) = x + x² + 2x³ + 4x⁴ + … count rooted trees ([A000081](../A000081/))
  and B = R/(1 − R). A rooted tree with one marked node v is the sequence
  of the rooted trees hanging at the nodes of the path from the root to v
  (each path node with its off-path subtrees), so B counts those
  (A000107). With two labels, either one labeled node is an ancestor of
  the other (B² each way: the path to the upper one, then the path below
  it) or the two paths part at a third node w (B³: the path to w and the
  two branches below it, told apart by their labels). So the g.f. is
  B³ + 2B² = R²(2 − R)/(1 − R)³ (OEIS, V. Jovovic 2001; Riordan 1958,
  p. 134).

**How it works**

- The Euler-transform recurrence of [A000081](../A000081/),
  `n-=1;r+=…//n,`, appends one more rooted-tree count each pass, so after
  the append r = [r₀, …, r_m] with r₀ = 0 and m = 1 − n.
- Horner over that list in a base X gives T = Σ r_j X^(m−j) = X^m·R̂(1/X),
  with R̂ the truncation of R at degree m, and V = X^m. Then R̂(1/X) = T/V,
  and the truncated generating function P̂ = R̂²(2 − R̂)/(1 − R̂)³ satisfies

  X^m·P̂(1/X) = V·T²(2V − T)/(V − T)³ = Σ_j p̂_j X^(m−j).

  Truncating R at degree m leaves the coefficients up to degree m alone,
  so p̂_j = a(j) for j ≤ m, and the integer part of that number, taken
  mod X, is a(m) if the tail Σ_{j>m} p̂_j X^(m−j) is below 1 and a(m) < X.
  This is the program's `V*T*T*(2*V-T)//(V-T)**3%X`, with no modular
  inverse and no reversed list.
- The bounds. P = R²/(1 − R)² + R²/(1 − R)³ is a power series in R with
  nonnegative coefficients, so 0 ≤ p̂_j ≤ a(j). Choosing a tree and an
  ordered pair of its nodes covers every case, so a(j) ≤ j²·r_j, and
  r_j ≤ 4^(j−1) (every rooted tree has a plane embedding, and there are
  Catalan(j−1) < 4^(j−1) plane trees). With X = 99^(m−1): for m ≥ 3 the
  tail is at most Σ_{i≥1} (m+i)²·4^(m+i−1)/99^((m−1)i) < 0.11, and
  a(m) ≤ m²·4^(m−1) < X. For m = 2 (X = 99), using r₃ = 2 and r₄ = 4 the
  tail is below 12/99 + 48/99² + 0.01 < 0.14, and a(2) = 2.
- `X=99**-n` is 99^(m−1) since n = 1 − m, and `X**-~-n` is X^(1−n) = X^m.

**Notes**

- The original program evaluated R at B = m^m + 1 with
  `pow(1-S,-3,M)` modulo B^(m+1) and printed only from m ≥ 2: 195 bytes.
  That modular route on this one-line frame, with a reversed Horner
  `[S:=S*X+c for c in r[::-1]]` and `pow(1-S,-3,X**len(r))`: 166 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file takes 19–37 s here (two runs), and about 235 terms come
  out in 60 s.
- a(n) grows like 2.96^n, so the 4300-digit int-to-str limit is out of
  reach.
- The b-file has 199 terms (up to a(200)); the bar is 30 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 195 | first entry |
| 2026-11-07 | Python 3 | 153 | evaluate at x = 1/X and floor, appended term read at once |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000524), CC BY-SA 4.0.
