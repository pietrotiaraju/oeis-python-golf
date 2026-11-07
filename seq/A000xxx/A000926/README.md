# A000926

> Euler's "numerus idoneus" (or "numeri idonei", or idoneal, or suitable, or convenient numbers).
> — [OEIS A000926](https://oeis.org/A000926)

Offset 1: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 21, 22, 24, 25, 28, …

### Python 3 — 117 bytes

```python
n=1
while[any(0==r<2*b<a<c for a in range(n)if a*a<2*n for b in range(a)for c,r in[divmod(b*b+n,a)])or print(n)]:n+=1
```

**How it works**

- Euler's definition is about which numbers x² + ny² represent; the test
  used here is its equivalent in Cox, *Primes of the form x² + ny²*,
  Proposition 3.24 (with Theorem 3.22 linking it to Euler's statement):
  n is idoneal if and only if every reduced primitive form
  ax² + Bxy + cy² of discriminant −4n has B = 0, B = a or a = c.
- With B = 2b the forms are ax² + 2bxy + cy² with ac − b² = n. A reduced
  form breaking the rule has 0 < |B| < a < c, and then (a, −B, c) is
  reduced too, so it is enough to look for 0 < 2b < a < c:
  `divmod(b*b+n,a)` gives c and a remainder `r`, and the chain
  `0==r<2*b<a<c` is the whole test (b = 0 fails at `r<2*b`, a = 0 has an
  empty `range(0)`). Such a form needs a² < ac = b² + n < a²/4 + n, so
  a² < 4n/3, hence the filter `a*a<2*n`.
- No primitivity test: a non-primitive form g·(a′, B′, c′) that breaks the
  rule has a primitive part of discriminant −4n/g² whose class has order
  greater than 2 (its inverse is the different reduced form
  (a′, −B′, c′)). The class group of discriminant −4n maps onto that of
  −4n/g² (the class group of an order maps onto that of any larger order,
  Cox §7), so it is not a product of groups of order 2 and n is not
  idoneal anyway (Cox 3.24 again).
- `any(...)or print(n)` prints n when no form breaks the rule; inside
  `while[...]` the loop goes on either way.

**Notes**

- The sequence is finite as far as anyone knows: 65 terms, the last 1848.
  Weinberger proved there is at most one more, and none if the generalized
  Riemann hypothesis holds. The program assumes neither: it tests every n
  forever, so after 1848 it keeps running and prints a 66th term only if
  one exists.
- All 65 terms come out in under a second; the bar is the whole b-file
  (65 terms) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000926), CC BY-SA 4.0.
