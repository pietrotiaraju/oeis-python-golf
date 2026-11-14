# A001699

> Number of binary trees of height n; or products (ways to insert parentheses) of height n when multiplication is non-commutative and non-associative.
> — [OEIS A001699](https://oeis.org/A001699)

Offset 0: 1, 1, 3, 21, 651, 457653, 210065930571, 44127887745696109598901, …

### Python 3 — 32 bytes

```python
a=0
while 1:print(-a+(a:=a*a+1))
```

**How it works**

- **Count by height at most n.** A product (a full binary tree) of height
  at most n is either the single factor x or a product of two products of
  height at most n−1. So T(n), the number of height at most n, satisfies
  T(n) = T(n−1)² + 1 with T(0) = 1 (1, 2, 5, 26, 677, …), and the number of
  height exactly n is a(n) = T(n) − T(n−1), with T(−1) = 0 so that
  a(0) = 1. Check: a(2) = 5 − 2 = 3, the products (xx)x, x(xx), (xx)(xx).
- The program keeps a = T(n−1), from 0. In `-a+(a:=a*a+1)` Python
  evaluates the left operand first, so −a still uses T(n−1) and the
  walrus then stores T(n); the sum is T(n) − T(n−1).

**Notes**

- Exact integers, so the program is right for every n. a(14) has 2899
  digits; a(15) is over Python's 4300-digit limit for printing ints, where
  the program stops with a ValueError.
- The b-file (13 terms, kept as downloaded with its trailing blank lines)
  prints at once; the bar is the whole b-file in 60 s.
- `while[print(a*~-a+1)]:a=a*a+1` (a(n) = T(n−1)² − T(n−1) + 1) is 2 bytes
  longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001699), CC BY-SA 4.0.
