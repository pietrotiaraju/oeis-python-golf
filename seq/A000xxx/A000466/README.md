# A000466

> a(n) = 4*n^2 - 1.
> — [OEIS A000466](https://oeis.org/A000466)

Offset 0: -1, 3, 15, 35, 63, 99, 143, 195, 255, 323, …

### Python 3 — 31 bytes

```python
n=0
while 1:print(4*n*n-1);n+=1
```

**How it works**

Evaluate the defining polynomial 4n²-1 directly for n=0,1,2,….

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 901 terms in 60 s; the official b-file contains 901 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000466), CC BY-SA 4.0.
