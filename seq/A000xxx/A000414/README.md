# A000414

> Numbers that are the sum of 4 nonzero squares.
> — [OEIS A000414](https://oeis.org/A000414)

Offset 1: 4, 7, 10, 12, 13, 15, 16, 18, 19, 20, …

### Python 3 — 143 bytes

```python
n=1;s={1};t={2};u={3};k=2
while 1:
 if n==k*k:s.add(n);t|={n+x for x in s};u|={n+x for x in t};k+=1
 if any(n-x in u for x in s):print(n)
 n+=1
```

**How it works**

The sets s, t and u contain sums of respectively one, two and three
positive squares. On adding a new largest square n, update t from s
and then u from the updated t, so repetitions of n are included.
Every new pair or triple contains n, and conversely every such sum
is generated. The final membership test appends a fourth positive
square. Scanning candidates increasingly removes duplicates.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 143 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000414), CC BY-SA 4.0.
