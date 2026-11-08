# A000990

> Number of plane partitions of n with at most two rows.
> — [OEIS A000990](https://oeis.org/A000990)

Offset 0: 1, 1, 3, 5, 10, 16, 29, 45, 75, 115, 181, 271, 413, 605, 895, 1291, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])<<(d<-1)for d in range(n,0))//n,
```

**How it works**

- The g.f. (1 − x)/∏(1 − xᵐ)² = 1/((1 − x)·∏_{m≥2}(1 − xᵐ)²) is the
  Euler transform of b = 1, 2, 2, 2, …: partitions with one kind of 1 and
  two kinds of every larger part.
- The Euler transform s of b satisfies the log-derivative recurrence
  **m·s(m) = Σₖ k·b(k)·Σⱼ s(m − jk)**, the template of
  [A000041](../A000041/): `a` holds s(0), …, s(m−1), `n` = −m, and with
  d = −k the slice `a[d::d]` is s(m − k), s(m − 2k), … The signs of d and
  n cancel in the division.
- The weight 2 for k ≥ 2 is a shift: `<<(d<-1)` doubles every term but
  the one for k = 1 (as in [A000097](../A000097/)).

**Notes**

- Exact integer arithmetic, and the divisions by m are exact. Each term
  costs about m·ln m additions inside slices: 8439 terms in 60 s here.
  The b-file has 10001 terms; the bar is 6500.
- The entry's a(n) = A000712(n) − A000712(n−1) on top of the
  [A000712](../A000712/) program (with a leading 0 in the list) is 89
  bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000990), CC BY-SA 4.0.
