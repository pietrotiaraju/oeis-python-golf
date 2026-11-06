# A000453

> Stirling numbers of the second kind, S(n,4).
> — [OEIS A000453](https://oeis.org/A000453)

Offset 4: 1, 10, 65, 350, 1701, 7770, 34105, 145750, 611501, 2532530, …

### Python 3 — 50 bytes

```python
n=4
while 1:print((4**n-4*3**n+6*2**n-4)//24);n+=1
```

**How it works**

- S(n,4) counts partitions of n labeled elements into four nonempty,
  unlabeled blocks. First count onto maps into four labeled boxes.
  Inclusion-exclusion over empty boxes gives

  4ⁿ−C(4,1)3ⁿ+C(4,2)2ⁿ−C(4,3)1ⁿ
  =4ⁿ−4·3ⁿ+6·2ⁿ−4, for n≥1.

- Every unlabeled partition occurs 4!=24 times after labeling its
  boxes. Dividing the whole expression by 24 therefore gives an
  integer, exactly S(n,4).
- The sequence's offset is 4, the first size at which four nonempty
  blocks are possible. Starting `n=4` omits the earlier zeros; the
  first numerator is 256−324+96−4=24 and prints 1.

**Notes**

- Exact integer powers and a single exact division, with no Stirling
  triangle or factorial computation in the program.
- [A000392](../A000392/) is the three-block version; the five-block
  sequence [A000481](../A000481/) instead uses a cascade of short
  recurrences to avoid writing a longer inclusion-exclusion expression.
- There is a constant number of stored integers. S(n,4) grows on the
  scale of 4ⁿ/24; Python 3.11+ eventually stops at its default
  4300-digit output conversion limit, an interpreter limit.
- The b-file has 197 terms (indices 4 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000453), CC BY-SA 4.0.
