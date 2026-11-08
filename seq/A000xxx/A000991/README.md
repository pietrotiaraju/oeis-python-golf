# A000991

> Number of 3-line partitions of n.
> — [OEIS A000991](https://oeis.org/A000991)

Offset 0: 1, 1, 3, 6, 12, 21, 40, 67, 117, 193, 319, 510, 818, 1274, 1983, 3032, …

### Python 3 — 89 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])*min(3,-d)for d in range(n,0))//n,
```

**How it works**

- The g.f. (1 − x)²(1 − x²)/∏(1 − xᵏ)³ is 1/((1 − x)(1 − x²)²·∏_{k≥3}(1 − xᵏ)³),
  the Euler transform of b = 1, 2, 3, 3, 3, …, that is b(k) = min(k, 3).
- The Euler transform s of b satisfies the log-derivative recurrence
  **m·s(m) = Σₖ k·b(k)·Σⱼ s(m − jk)**, the template of
  [A000041](../A000041/): `a` holds s(0), …, s(m−1), `n` = −m, and with
  d = −k the slice `a[d::d]` is s(m − k), s(m − 2k), … The signs of d and
  n cancel in the division, and the weight is `min(3,-d)`.

**Notes**

- Exact integer arithmetic, and the divisions by m are exact. The whole
  b-file (6001 terms) prints in about 36 s here, 7371 terms in 60 s; the
  bar is the whole b-file.
- The entry's difference formula on top of the 3-kinds program
  [A000716](../A000716/) needs four earlier terms and is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000991), CC BY-SA 4.0.
