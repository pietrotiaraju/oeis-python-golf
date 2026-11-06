# A000404

> Numbers that are the sum of 2 nonzero squares.
> — [OEIS A000404](https://oeis.org/A000404)

Offset 1: 2, 5, 8, 10, 13, 17, 18, 20, 25, 26, …

### Python 3 — 91 bytes

```python
n=1;s={1};k=2
while 1:
 if n==k*k:s.add(n);k+=1
 if any(n-x in s for x in s):print(n)
 n+=1
```

**How it works**

The set s contains exactly the positive squares at most n.
When n reaches the next square, add it and advance k.
The membership test asks whether n=x+y for two members of s.
Zero is absent, so both squares are nonzero. Scanning n in increasing
order prints every represented integer once, regardless of multiplicity.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000404), CC BY-SA 4.0.
