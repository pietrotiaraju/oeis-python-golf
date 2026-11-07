# A000982

> a(n) = ceiling(n^2/2).
> — [OEIS A000982](https://oeis.org/A000982)

Offset 0: 0, 1, 2, 5, 8, 13, 18, 25, 32, 41, 50, 61, …

### Python 3 — 31 bytes

```python
n=0
while[print(n*n+1>>1)]:n+=1
```

**How it works**

- ⌈n²/2⌉ = ⌊(n² + 1)/2⌋, and `n*n+1>>1` needs no parentheses because
  `>>` binds looser than `+`.

**Notes**

- Other versions: the running sum with steps 1, 1, 3, 3, 5, 5, …
  (`a+=n|1;n+=1`) is 33 bytes.
- Exact integer arithmetic.
- The b-file has 3001 terms; they print at once. The bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000982), CC BY-SA 4.0.
