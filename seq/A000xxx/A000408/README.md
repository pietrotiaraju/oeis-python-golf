# A000408

> Numbers that are the sum of three nonzero squares.
> — [OEIS A000408](https://oeis.org/A000408)

Offset 1: 3, 6, 9, 11, 12, 14, 17, 18, 19, 21, …

### Python 3 — 117 bytes

```python
n=1;s={1};t={2};k=2
while 1:
 if n==k*k:s.add(n);t|={n+x for x in s};k+=1
 if any(n-x in t for x in s):print(n)
 n+=1
```

**How it works**

The sets s and t contain positive squares and sums of two positive
squares. On encountering a new square n, add n+x for every x in s.
This generates each possible unordered pair when its largest square
first becomes available. The final test searches n=x+y with x in s
and y in t. Every representation needed for the current candidate
uses squares at most n, so the test is exact for every candidate.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000408), CC BY-SA 4.0.
