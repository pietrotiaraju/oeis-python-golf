# A000700

> Expansion of Product_{k>=0} (1 + x^(2k+1)); number of partitions of n into distinct odd parts; number of self-conjugate partitions; number of symmetric Ferrers graphs with n nodes.
> — [OEIS A000700](https://oeis.org/A000700)

Offset 0: 1, 1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, …

### Python 3 — 71 bytes

```python
p=[1];j=1
while[print(p[j//2])]:p=[*map(sum,zip(p+[0]*j,[0]*j+p))];j+=2
```

**How it works**

- `p` is the coefficient list of ∏(1+xʲ) over the odd parts j used so far;
  multiplying by 1+xʲ adds the list to itself shifted by j:
  `zip(p+[0]*j,[0]*j+p)`.
- Before the factor 1+xʲ goes in, every odd part up to j−2 is in, so all
  coefficients up to j−1 are final. The program prints `p[j//2]` at that
  moment: for j = 1 it is p[0] = 1, and for j ≥ 3, j//2 ≤ j−2. As j runs
  over 1, 3, 5, … the index j//2 runs over 0, 1, 2, …, one term per pass.

**Notes**

- Exact integer additions; no theorem needed.
- The list keeps the whole product, about n² entries after n terms:
  770 terms in 60 s, using about 160 MB.
- The b-file has 10001 terms; the bar is 600 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000700), CC BY-SA 4.0.
