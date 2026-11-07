# A000735

> Expansion of Product_{k>=1} (1 - x^k)^12.
> — [OEIS A000735](https://oeis.org/A000735)

Offset 0: 1, -12, 54, -88, -99, 540, -418, -648, 594, 836, 1056, -4104, -209, 4104, -594, 4256, -6480, -4752, -298, 5016, …

### Python 3 — 83 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=12*sum(d*sum(a[d::d])for d in range(n,0))//-n,
```

**How it works**

- **The recurrence.** Let A(x) = Π_{k≥1} (1 − x^k)¹² = Σ_m a(m)·x^m. Its
  logarithmic derivative is x·A′(x)/A(x) = −12 Σ_{k≥1} k·x^k/(1 − x^k) =
  −12 Σ_{t≥1} σ(t)·x^t, and comparing coefficients of x^m gives

  m·a(m) = −12 Σ_{k=1}^{m} k·(a(m−k) + a(m−2k) + a(m−3k) + …).

  The right side is m·a(m) exactly, so the floor division by m is exact.
- **Negative steps.** The list `a` holds a(0), …, a(m−1) and n = −m. For
  d = −k the slice `a[d::d]` is a(m−k), a(m−2k), …, so `d*sum(a[d::d])` is
  −k times the inner sum; the minus signs of d and of −12 cancel against
  `//-n`, which divides by m.
- `*a,n=1,0` sets a = [a(0)] = [1] and n = 0; `print(a[-1])` in the loop
  condition prints a(0) first and then each new coefficient.
- The signs need no care: the recurrence runs on the signed values
  directly (packing the series into one big integer would need a bias per
  digit to survive the borrows, which costs more than it saves).

**Notes**

- This is the template of [A000594](../A000594/) (exponent 24) with the
  factor 12; the other powers in this group, [A000727](../A000727/), [A000728](../A000728/), [A000729](../A000729/), [A000730](../A000730/), [A000731](../A000731/), [A000739](../A000739/), differ
  only in that factor.
- Ties: counting n up with `n+=1`, `range(-n,0)` and `//n`, or writing
  `sum(…)*12` or `-12*sum(…)//n`, all give the same length.
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m): about 9079 terms in 60 s
  here. The b-file has 10001 terms; the bar is 7000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000735), CC BY-SA 4.0.
