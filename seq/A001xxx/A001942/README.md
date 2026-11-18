# A001942

> Expansion of reciprocal of theta series of Leech lattice.
> — [OEIS A001942](https://oeis.org/A001942)

Offset 0: 1, 0, -196560, -16773120, 38237799600, 6589219553280, …

### Python 3 — 158 bytes

```python
*a,n=1,0;T=[1]
while[print(a[-1])]:n-=1;a+=65520*sum(d**11*sum(a[d::d])+T[~d]*a[d]for d in range(n,0))//691,;T+=24*sum(d*sum(T[d::d])for d in range(n,0))//-n,
```

**How it works**

- **The theta series.** With q^k counting vectors of norm 2k, the theta
  series Θ of the Leech lattice is a modular form of weight 12 for
  SL₂(ℤ), so Θ = E₁₂ + c·Δ, where E₁₂ = 1 + (65520/691) Σ σ₁₁(k)·q^k and
  Δ = q·Π(1 − q^j)^24 = Σ τ(k)·q^k. The Leech lattice has no vectors of
  norm 2, so the q¹ coefficient 65520/691 + c vanishes and
  Θ = 1 + (65520/691) Σ_{k≥1} (σ₁₁(k) − τ(k))·q^k
  (Conway and Sloane, *Sphere Packings, Lattices and Groups*, ch. 4;
  equivalently Θ = E₄³ − 720Δ). This gives 1, 0, 196560, 16773120, …
  ([A008408](https://oeis.org/A008408)).
- **The reciprocal.** Since Θ starts with 1, a(0) = 1 and for m ≥ 1

  a(m) = −(65520/691) Σ_{k=1..m} (σ₁₁(k) − τ(k))·a(m−k).

  The coefficients of Θ are integers and 691 is a prime that does not
  divide 65520, so 691 divides every σ₁₁(k) − τ(k) (Ramanujan's
  congruence) and the floor division `//691` is exact.
- **One sum over d.** The list `a` holds a(0), …, a(m−1), n = −m, and d
  runs over −m, …, −1. The σ₁₁ part is Σ_{d≥1} d¹¹·(a(m−d) + a(m−2d) + …),
  which is `d**11*sum(a[d::d])` with negative d (as in
  [A001943](../A001943/)); `d**11` is −|d|¹¹. The τ part is a plain
  convolution, and with k = −d its terms are `T[~d]*a[d]`, because
  `a[d]` = a(m−k) and `T[~d]` = T(k−1) = τ(k), where T holds the
  coefficients of Π(1 − q^j)^24. Both parts share the one generator, and
  the sign of `d**11` matches the minus in σ₁₁ − τ:
  a(m) = 65520·Σ_d (d¹¹·S_d + τ(−d)·a(m+d))/691.
- **τ on the side.** After each step T gets its next coefficient by the
  Euler-transform recurrence of [A000594](../../A000xxx/A000594/), with
  the same negative slices: m·T(m) = −24 Σ_{k≥1} k·(T(m−k) + T(m−2k) + …).

**Notes**

- Exact integer arithmetic, so the program is right for every n. The terms
  grow geometrically (|a(n)| has about 2.66·n digits), so printing stops
  with Python's 4300-digit int-to-str limit near n = 1600; the b-file ends
  at n = 376.
- The bar is the whole b-file (377 terms, n = 0 to 376) in 60 s, which
  takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 158 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001942), CC BY-SA 4.0.
