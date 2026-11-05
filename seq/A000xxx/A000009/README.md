# A000009

> Expansion of Product_{m >= 1} (1 + x^m); number of partitions of n into
> distinct parts; number of partitions of n into odd parts.
> — [OEIS A000009](https://oeis.org/A000009)

Offset 0: 1, 1, 1, 2, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 27, 32, 38, …

### Python 3 — 68 bytes

```python
p=[1];k=0
while[print(p[k])]:k+=1;p=[*map(sum,zip(p+[0]*k,[0]*k+p))]
```

**How it works**

- `p` holds the coefficients of (1 + x)(1 + x²)…(1 + xᵏ), in full.
- Multiplying by (1 + xᵏ) adds the list to a copy of itself shifted k places:
  `zip(p+[0]*k,[0]*k+p)` pairs the two, padded to the same length, and
  `map(sum,…)` adds each pair.
- Parts larger than k cannot appear in a partition of k, so after the first k
  factors the coefficient `p[k]` is already final: a(k).
- `while[print(...)]:` prints in the loop condition (`[None]` is true) and
  saves a byte over `while 1:print(...);`.

**Notes**

- The product is kept whole, degree k(k+1)/2, because later terms need its
  higher coefficients. That makes term k cost about k² additions, so the
  program prints about 900 terms a minute; the bar is 500 terms in 60 s.
- The same loop with `[a+b for a,b in zip(…)]` is 73 bytes.
- Counting distinct-part partitions with the recursion
  `f=lambda n,k=1:(n<1)+sum(f(n-j,j+1)for j in range(k,n+1))` is 85 bytes
  and exponential.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000009), CC BY-SA 4.0.
