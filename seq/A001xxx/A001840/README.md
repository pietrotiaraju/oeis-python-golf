# A001840

> Expansion of g.f. x/((1 - x)^2*(1 - x^3)).
> — [OEIS A001840](https://oeis.org/A001840)

Offset 0: 0, 1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 26, 30, 35, 40, 45, 51, …

### Python 3 — 30 bytes

```python
k=3
while[print(k*k//24)]:k+=2
```

**How it works**

- From the generating function, (1 − x³)·A = x/(1 − x)², so
  a(n) = a(n−3) + n (with a(m) = 0 for m < 0), and a(0), a(1), a(2) = 0, 1, 2.
- f(n) = ⌊(n + 1)(n + 2)/6⌋ obeys the same rule: (n + 1)(n + 2) − (n − 2)(n − 1)
  = 6n, so f(n) = f(n−3) + n exactly, and f(0), f(1), f(2) = 0, 1, 2. Hence
  a(n) = ⌊(n + 1)(n + 2)/6⌋ for every n (the formula on the OEIS page).
- With k = 2n + 3, k² = 4(n + 1)(n + 2) + 1, so k²/24 = (n + 1)(n + 2)/6 + 1/24.
  Since (n + 1)(n + 2) is even, (n + 1)(n + 2)/6 is a multiple of 1/3, and
  adding 1/24 never reaches the next integer: ⌊k²/24⌋ = a(n). `k` runs over
  the odd numbers from 3.

**Notes**

- `n*-~n//6` with n = 1, 2, … (the same floor, unshifted) is 31 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001840), CC BY-SA 4.0.
