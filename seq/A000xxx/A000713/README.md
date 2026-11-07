# A000713

> EULER transform of 3, 2, 2, 2, 2, 2, 2, 2, ...
> — [OEIS A000713](https://oeis.org/A000713)

Offset 0: 1, 3, 8, 18, 38, 74, 139, 249, 434, 734, 1215, 1967, 3132, 4902, 7567, 11523, …

### Python 3 — 82 bytes

```python
*a,n=1,0
while[print(sum(a))]:n-=1;a+=2*sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- The Euler transform of [3, 2, 2, 2, …] has g.f.
  1/(1 − x) · Π 1/(1 − xᵏ)², so a(n) is the running sum of
  [A000712](../A000712/), the partitions into parts of two kinds.
- The program is the A000712 one, `a` holding A000712(0…N), and prints
  `sum(a)` instead of `a[-1]`: one byte for the extra factor 1/(1 − x).
- For A000712: the log derivative of Π 1/(1 − xᵏ)² gives
  N·b(N) = 2·Σ_d d·Σ_j b(N − dj); `n` is −N, `d` runs over −N…−1, the
  slice `a[d::d]` is b(N − |d|), b(N − 2|d|), …, and `//n` divides
  exactly.
- Putting the extra 1 into the Euler weights instead, `(2*d-0**~d)` for
  d·b(d) (`0**~d` is 1 only at d = −1), costs 7 bytes more.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  about 1.58·√n digits, so the 4300-digit int-to-str limit is reached only
  near n = 7·10⁶.
- `sum(a)` adds N numbers per term, cheap next to the slice sums. The whole
  b-file (1001 terms) prints in about a second; the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000713), CC BY-SA 4.0.
