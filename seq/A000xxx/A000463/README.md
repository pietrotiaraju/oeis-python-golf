# A000463

> n followed by n^2.
> — [OEIS A000463](https://oeis.org/A000463)

Offset 1: 1, 1, 2, 4, 3, 9, 4, 16, 5, 25, …

### Python 3 — 35 bytes

```python
n=1
while[print(n),print(n*n)]:n+=1
```

**How it works**

The sequence interleaves n and n² for n=1,2,3,….
Both print calls run while constructing the loop-condition list,
which is always nonempty. Thus each pass prints n and then n²,
one integer per line, before incrementing n.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000463), CC BY-SA 4.0.
