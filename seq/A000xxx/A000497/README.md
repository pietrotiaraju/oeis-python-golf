# A000497

> S2(j,2j+2) where S2(n,k) is a 2-associated Stirling number of the second kind.
> — [OEIS A000497](https://oeis.org/A000497)

Offset 1: 1, 25, 490, 9450, 190575, 4099095, 94594500, 2343240900, 62199262125, 1764494857125, …

### Python 3 — 64 bytes

```python
a=n=1
while[print(a)]:n+=1;a=a*(n+1)*(2*n+1)**2//((2*n-1)*(n-1))
```

**How it works**

- These associated Stirling numbers count partitions of 2n+2 labeled
  elements into n blocks, all of size at least two. There are two
  extra elements beyond pairs: either one block has size 4, or two
  blocks have size 3; all other blocks have size 2.
- Counting those two cases gives, for n≥2,
  (2n+2)!/(4!·2^(n−1)(n−1)!)
  +(2n+2)!/(3!²·2^(n−2)·2!·(n−2)!).
  Simplifying gives n(n+1)(2n+1)(2n+1)!!/18, also valid at n=1.
- Taking the ratio of this expression at n and n−1 gives the
  recurrence listed on the OEIS page:

  **(2n−1)(n−1)a(n)=(n+1)(2n+1)²a(n−1).**

- Initialize a=n=1. Increment n before the update so its denominator
  is nonzero, and multiply the full numerator before dividing. At
  n=2 this gives 1·3·25/(3·1)=25, the next term.

**Notes**

- For n=2 the two cases are block sizes 4+2 (15 partitions) and
  3+3 (10 partitions), giving a(2)=25 directly.
- Exact division follows from the partition count, not just a match
  to the b-file. The rational ratio need not itself be an integer;
  it is the complete updated product that is divisible.
- Only the current term and index are retained; there is no full
  associated Stirling triangle or factorial recomputation. Python
  3.11+ eventually meets its default 4300-digit output conversion
  limit, an interpreter limit.
- The b-file has 100 terms (indices 1 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000497), CC BY-SA 4.0.
