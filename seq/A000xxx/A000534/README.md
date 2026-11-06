# A000534

> Numbers that are not the sum of 4 nonzero squares.
> — [OEIS A000534](https://oeis.org/A000534)

Offset 1: 0, 1, 2, 3, 5, 6, 8, 9, 11, 14, …

### Python 3 — 102 bytes

```python
print(0,1,2,3,5,6,8,9,11,14,17,24,29,32,41,sep='\n')
a=[56,96,128]
while[print(a[0])]:a=a[1:]+[4*a[0]]
```

**How it works**

- The classification quoted by OEIS is the finite exceptional set
  {0,1,3,5,9,11,17,29,41}, together with the three families
  2·4^m, 6·4^m and 14·4^m for m≥0.
- The first print merges those families with the exceptions through 41.
  After that, the three smallest remaining terms are 56,96,128; each
  next block is four times the preceding block.
- The list is a three-entry queue. Removing its first term and appending
  four times that term merges the infinite tails in increasing order.
  Thus the constants encode the finite part of the classification,
  rather than a finite prefix standing in for an unknown continuation.

**Notes**

- Correctness for all terms rests on the four-positive-squares
  classification stated in the OEIS entry.
- The recurrence is exact; the output conversion limit eventually applies.
- The reference file contains 100 terms from the OEIS b-file; the verification
  bar is 100 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 102 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000534), CC BY-SA 4.0.
