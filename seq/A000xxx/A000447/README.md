# A000447

> a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3.
> — [OEIS A000447](https://oeis.org/A000447)

Offset 0: 0, 1, 10, 35, 84, 165, 286, 455, 680, 969, …

### Python 3 — 35 bytes

```python
s=0;n=1
while[print(s)]:s+=n*n;n+=2
```

**How it works**

The definition is the partial sum of positive odd squares.
The state n visits 1, 3, 5, …; after printing the current sum,
add the next odd square. The initial empty sum gives a(0)=0.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1001 terms in 60 s; the official b-file contains 1001 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000447), CC BY-SA 4.0.
