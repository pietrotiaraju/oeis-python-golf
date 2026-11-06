# A000554

> Number of labeled trees of diameter 3 with n nodes.
> — [OEIS A000554](https://oeis.org/A000554)

Offset 4: 12, 60, 210, 630, 1736, 4536, 11430, 28050, 67452, 159588, …

### Python 3 — 44 bytes

```python
n=4
while 1:print(n*(n-1)*(2**(n-3)-1));n+=1
```

**How it works**

- A tree of diameter 3 has a unique central edge and at least one leaf
  attached to each of its endpoints. Choose the two central labels,
  then distribute the other n−2 labels to the endpoints nontrivially.
- There are C(n,2)(2^(n−2)−2)=n(n−1)(2^(n−3)−1) possibilities.
  The smallest such tree has n=4, giving 12.
- The formula counts labeled trees directly and uses one power of two.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 997 terms from the OEIS b-file; the verification
  bar is 997 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000554), CC BY-SA 4.0.
