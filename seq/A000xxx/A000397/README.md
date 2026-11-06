# A000397

> Number of partitions into non-integral powers.
> — [OEIS A000397](https://oeis.org/A000397)

Offset 5: 6, 32, 109, 288, 654, 1337, 2506, 4414, 7379, 11822, 18273, …

### Python 3 — 137 bytes

```python
n=5
while[N:=n*n,print(sum((q:=(N+z-x-y)**2-4*x*y-4*N*z)*abs(q)>=64*N*x*y*z for z in range(N)for y in range(z)for x in range(1,y)))]:n+=1
```

**How it works**

- As the OEIS comment puts it, a(n) counts the triples of distinct
  integers 1 ≤ x < y < z with √x + √y + √z ≤ n: Agarwala and Auluck's
  partitions of n into three distinct parts k^(1/2), counted with ≤. The
  smallest sum is 1 + √2 + √3 ≈ 4.15, hence offset 5.
- It is the [A000345](../A000345/) program with strict ranges
  (`range(z)`, `range(1,y)`) and the same exact test: z < n² is enough,
  m = n² + z − x − y > 0 because x + y < 2z, and squaring
  √x + √y ≤ n − √z twice turns it into q ≥ 0 and q² ≥ 64n²xyz with
  q = m² − 4xy − 4n²z, written `q*abs(q)>=64*N*x*y*z`.

**Notes**

- Round n tries about n⁶/6 triples, so the program prints about 17 terms in
  60 s of the 76 in the b-file (OEIS synthesizes it from the entry's
  terms). The bar is 13 terms in 60 s.
- The floor/ceiling recursion of [A000333](../A000333/) restricted to three
  distinct parts is far faster but more than 30 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 137 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000397), CC BY-SA 4.0.
