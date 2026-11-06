# A000311

> Schroeder's fourth problem; also series-reduced rooted trees with n labeled leaves; also number of total partitions of n.
> — [OEIS A000311](https://oeis.org/A000311)

Offset 0: 0, 1, 1, 4, 26, 236, 2752, 39208, 660032, 12818912, 282137824, 6939897856, 188666182784, …

### Python 3 — 81 bytes

```python
p=0;R=[1]
while[print(p)]:t=p=0;R=[t:=t+len(R)*(p+(p:=R.pop(0)))for x in R*1]+[t]
```

**How it works**

- The program rests on a T-fraction for the ordinary generating function:

  Σ_{n≥0} a(n+1)·tⁿ = 1/(1 − t/(1 − t − 2t/(1 − 2t − 3t/(1 − …)))),

  with coefficients αᵢ = i and δᵢ = i − 1. This is Theorem 1.1 of
  A. Elvey Price and A. D. Sokal, *Phylogenetic trees, augmented perfect
  matchings, and a Thron-type continued fraction (T-fraction) for the
  Ward polynomials*, Electron. J. Combin. 27(4) (2020) P4.6, at x = 1: the
  Ward polynomials Wₙ(x) count phylogenetic trees with n + 1 labeled
  leaves, so Wₙ(1) = a(n+1). It is also the continued fraction in the
  OEIS entry (Gladkovskii, 2013).
- A T-fraction counts Schröder paths: rises cost nothing, a fall from
  height h weighs h·t, and a level step at height h weighs h·t (δ_{h+1} = h).
  Let w_m(h) be the total weight of the ways to go from height h down to 0
  with m steps that carry a t. Then w_0(h) is 1 for h = 0 and 0 otherwise,
  a(m+1) = w_m(0), and

  w_{m+1}(h) = Σ_{h' ≥ h} h'·(w_m(h') + w_m(h'−1)):

  climb freely from h to some h', then take a level step (stay at h') or a
  fall (to h' − 1), both of weight h'. Rows are finite: w_m(h) = 0 for h > m.
- `R` holds row m from the top, [w_m(m), …, w_m(0)]. The new row is a
  running sum `t` from the top down: its entry for height h' adds
  h'·(w_m(h') + w_m(h'−1)), and h' = 0 adds nothing, so the last entry
  repeats (`+[t]`).
- `len(R)*(p+(p:=R.pop(0)))`: while the comprehension runs over the copy
  `R*1`, R still holds the entries from w_m(h'−1) down, so `len(R)` is the
  weight h'. `p` is the entry popped just before, w_m(h'), with 0 at the
  top, and the pop gives w_m(h'−1).
- After a pass, `p` is the last entry popped, w_m(0) = a(m+1), and the
  next pass prints it before resetting `t=p=0`. So `p=0` at the start
  prints a(0) = 0 and `R=[1]` is row 0.

**Notes**

- Rows: [1], [1, 1], [2, 4, 4], [6, 18, 26, 26], [24, 96, 184, 236, 236], …
  The top entry is m! and the last two are a(m+1).
- Alternatives tried: the Ward-number triangle W(n, k) = k·W(n−1, k) +
  (n+k−1)·W(n−1, k−1) with row sums a(n+1) needs both indices in the
  weights and a separate `print(0)` (105 bytes); the recurrence
  a(n) = −(n−1)·a(n−1) + Σ C(n, k)·a(k)·a(n−k) needs `math.comb`
  (about 110 bytes); the polynomials of h = 1/(2 − eᵘ) with
  P_{n+1} = h²(2h−1)·P_n′ and a(n) = P_n(1) are about 90.
- Exact integer arithmetic, so the program is right for every n, by the
  theorem above. a(1380) is the first term with more than 4300 digits, so
  Python 3.11+ stops there with a `ValueError` from the int-to-str limit,
  which is not counted as a failure.
- The b-file has 376 terms (n = 0 to 375); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000311), CC BY-SA 4.0.
