# A000711

> Number of partitions of n, with three kinds of 1,2,3 and 4 and two kinds of 5,6,7,...
> — [OEIS A000711](https://oeis.org/A000711)

Offset 0: 1, 3, 9, 22, 51, 107, 217, 416, 775, 1393, 2446, 4185, 7028, 11569, 18749, …

### Python 3 — 90 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])*(2+(d>-5))for d in range(n,0))//n,
```

**How it works**

- The g.f. is Π 1/(1 − xᵏ)² times 1/((1 − x)(1 − x²)(1 − x³)(1 − x⁴)): the Euler transform of
  b = [3, 3, 3, 3, 2, 2, …]. Its log derivative gives
  **N·a(N) = Σ_d d·b(d)·Σ_j a(N − dj)** over d = 1…N and j ≥ 1 with
  dj ≤ N, the partition-number recurrence with every group counted twice
  and the groups d = 1…4 three times.
- This is the [A000041](../A000041/) program with the weight
  `*(2+(d>-5))`, which is 3 when d ≥ −4 and 2 otherwise. `n` is −N, `d`
  runs over −N…−1, the slice `a[d::d]` is a(N − |d|), a(N − 2|d|), …, and
  `//n` divides −N·a(N) by −N exactly.
- The ratio 3 : 2 is not a power of two, so the `<<(d>-k)` doubling of
  [A000097](../A000097/) does not fit. Keeping [A000712](../A000712/) in
  the list and adding the small-part factor at print time, as
  [A000713](../A000713/) does with `sum(a)` for 1/(1 − x), needs nested
  running sums here and is longer.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.58·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 7·10⁶.
- The whole b-file (1001 terms) prints in about a second; the bar is the
  whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000711), CC BY-SA 4.0.
