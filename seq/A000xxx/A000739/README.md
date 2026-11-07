# A000739

> Expansion of Product_{k>=1} (1 - x^k)^16.
> — [OEIS A000739](https://oeis.org/A000739)

Offset 0: 1, -16, 104, -320, 260, 1248, -3712, 1664, 6890, -7280, -5568, -4160, 33176, 4640, -74240, 29824, 14035, 54288, 27040, -142720, …

### Python 3 — 83 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=16*sum(d*sum(a[d::d])for d in range(n,0))//-n,
```

**How it works**

- **The recurrence.** Let A(x) = Π_{k≥1} (1 − x^k)¹⁶ = Σ_m a(m)·x^m. Its
  logarithmic derivative is x·A′(x)/A(x) = −16 Σ_{k≥1} k·x^k/(1 − x^k) =
  −16 Σ_{t≥1} σ(t)·x^t, and comparing coefficients of x^m gives

  m·a(m) = −16 Σ_{k=1}^{m} k·(a(m−k) + a(m−2k) + a(m−3k) + …).

  The right side is m·a(m) exactly, so the floor division by m is exact.
- **Negative steps.** The list `a` holds a(0), …, a(m−1) and n = −m. For
  d = −k the slice `a[d::d]` is a(m−k), a(m−2k), …, so `d*sum(a[d::d])` is
  −k times the inner sum; the minus signs of d and of −16 cancel against
  `//-n`, which divides by m.
- `*a,n=1,0` sets a = [a(0)] = [1] and n = 0; `print(a[-1])` in the loop
  condition prints a(0) first and then each new coefficient.
- The signs need no care: the recurrence runs on the signed values
  directly (packing the series into one big integer would need a bias per
  digit to survive the borrows, which costs more than it saves).

**Notes**

- This is the template of [A000594](../A000594/) (exponent 24) with the
  factor 16; the other powers in this group, [A000727](../A000727/), [A000728](../A000728/), [A000729](../A000729/), [A000730](../A000730/), [A000731](../A000731/), [A000735](../A000735/), differ
  only in that factor.
- Ties: counting n up with `n+=1`, `range(-n,0)` and `//n`, or writing
  `sum(…)*16` or `-16*sum(…)//n`, all give the same length.
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m): about 9245 terms in 60 s
  here. The b-file has 10001 terms; the bar is 7000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000739), CC BY-SA 4.0.
