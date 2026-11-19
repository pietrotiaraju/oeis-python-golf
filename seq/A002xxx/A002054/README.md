# A002054

> Binomial coefficient C(2n+1, n-1).
> — [OEIS A002054](https://oeis.org/A002054)

Offset 1: 1, 5, 21, 84, 330, 1287, 5005, 19448, 75582, 293930, 1144066, …

### Python 3 — 52 bytes

```python
a=n=1
while[print(a)]:a=a*(4*n+6)*-~n//n//(n+3);n+=1
```

**How it works**

- a(n+1)/a(n) = C(2n+3, n)/C(2n+1, n−1) = (2n + 3)(2n + 2)/(n(n + 3)),
  written `(4*n+6)*-~n` over n·(n + 3). The whole product is formed before
  the two floor divisions, and ⌊⌊x/n⌋/(n + 3)⌋ = ⌊x/(n(n + 3))⌋, which is
  exact here because a(n+1) is an integer.
- `a=n=1` starts at a(1) = C(3, 0) = 1.

**Notes**

- `import math` with `math.comb(m,m//2-1)` over the odd m = 2n + 1 is
  54 bytes.
- Exact integer arithmetic, so the program is right for every n; a(n) is
  about 4ⁿ, so Python's 4300-digit int-to-str limit stops the output near
  n = 7140.
- The b-file has 1000 terms (n = 1 to 1000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002054), CC BY-SA 4.0.
