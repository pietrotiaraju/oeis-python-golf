# A001392

> a(n) = 9*binomial(2n,n-4)/(n+5).
> — [OEIS A001392](https://oeis.org/A001392)

Offset 4: 1, 9, 54, 273, 1260, 5508, 23256, 95931, 389367, 1562275, 6216210, …

### Python 3 — 54 bytes

```python
a=1;m=9
while[print(a)]:a=a*4*m*-~m//(m*m+4*m-77);m+=2
```

**How it works**

- With a(n) = 9·(2n)!/((n−4)!·(n+5)!), consecutive terms have the ratio
  a(n+1)/a(n) = (2n+2)(2n+1)/((n−3)(n+6)). In the odd variable m = 2n+1
  this is 4m(m+1)/((m−7)(m+11)), and (m−7)(m+11) = m² + 4m − 77.
- The loop starts at n = 4 (the offset) with a = 1 and m = 9. Since
  a(n+1) is an integer, a·4m(m+1) is an exact multiple of the denominator
  and `//` divides without loss; `-~m` is m + 1.

**Notes**

- a(n) = [x^(n−4)] C(x)⁹, where C is the Catalan generating function: the
  number of nonnegative ±1 paths of length 2n from height 0 to height 8, a
  ballot number.
- The binomial itself, `import math` / `m=9` /
  `while[print(math.comb(m,m-9>>1)*9//m)]:m+=2` (using
  a(n) = 9·C(2n+1, n−4)/(2n+1)), is 59 bytes; `(m-7)//(m+11)` as two
  floor divisions is one byte longer than the product.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 197 terms (a(4) to a(200)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001392), CC BY-SA 4.0.
