# A001859

> Triangular numbers plus quarter-squares: n*(n+1)/2 + floor((n+1)^2/4) (i.e., A000217(n) + A002620(n+1)).
> — [OEIS A001859](https://oeis.org/A001859)

Offset 0: 0, 2, 5, 10, 16, 24, 33, 44, 56, 70, 85, 102, 120, 140, …

### Python 3 — 30 bytes

```python
k=2
while[print(k*k//12)]:k+=3
```

**How it works**

- n(n + 1)/2 is an integer, so a(n) = ⌊(2n(n + 1) + (n + 1)²)/4⌋ =
  ⌊(3n² + 4n + 1)/4⌋.
- With k = 3n + 2, k²/12 = (3n² + 4n)/4 + 1/3. If n is even, 3n² + 4n is a
  multiple of 4 and both floors are (3n² + 4n)/4; if n is odd,
  3n² + 4n ≡ 3 (mod 4) and both floors are (3n² + 4n + 1)/4. So
  a(n) = ⌊(3n + 2)²/12⌋ for every n ≥ 0.
- `k` starts at 2 (n = 0) and steps by 3, and `k*k//12` is the floor.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The OEIS forms n + ⌊(3n² + 1)/4⌋ or `(3*n+1)*-~n>>2` with a counter are
  longer.
- G.f. (2x + x²)/((1 − x)²(1 − x²)).
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001859), CC BY-SA 4.0.
