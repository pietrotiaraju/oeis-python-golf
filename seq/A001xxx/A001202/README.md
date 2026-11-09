# A001202

> a(1)=0, a(2n) = a(n)+1, a(2n+1) = 10*a(n+1).
> — [OEIS A001202](https://oeis.org/A001202)

Offset 1: 0, 1, 10, 2, 100, 11, 20, 3, 1000, 101, 110, 12, 200, 21, 30, 4, …

### Python 3 — 46 bytes

```python
print(0);L=[1]
for x in L:print(x);L+=10*x,x+1
```

**How it works**

- Shift the index: with f(k) = a(k+1) the rule becomes f(0) = 0,
  f(2k) = 10·f(k) and f(2k+1) = f(k)+1 (a(2m+1) = 10·a(m+1) is
  f(2m) = 10·f(m), and a(2m) = a(m)+1 is f(2m−1) = f(m−1)+1).
- So the two children of f(k) are 10·f(k) and f(k)+1, and a breadth-first
  walk lists them in order: `L` holds f(1), f(2), f(3), …, and reading
  x = f(k) appends f(2k), f(2k+1), which land exactly at their places.
  `for x in L` keeps reading the list as it grows.
- f(0) = 0 is its own child (10·0), so it is printed apart.

**Notes**

- The whole b-file prints at once. The list grows twice as fast as the
  output, which only matters for memory after millions of terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001202), CC BY-SA 4.0.
