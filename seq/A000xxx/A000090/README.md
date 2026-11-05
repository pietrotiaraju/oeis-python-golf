# A000090

> Expansion of e.g.f. exp((-x^3)/3)/(1-x).
> — [OEIS A000090](https://oeis.org/A000090)

Offset 0: 1, 1, 2, 4, 16, 80, 520, 3640, 29120, 259840, 2598400, 28582400, 343235200, 4462057600, 62468806400, 936987251200, …

a(n) is also the number of permutations of n elements with no 3-cycle.

### Python 3 — 58 bytes

```python
a=t=n=1
while[print(a)]:t*=-n**(x:=n%3>0);a=a*n-t*~-x;n+=1
```

**How it works**

- The formula from the OEIS page: **a(n) = n!·Σ_{i ≤ n/3} (−1)^i/(i!·3^i)**.
  Going from n − 1 to n multiplies every term of the sum by n, and when
  3 | n one more term joins it, t(n) = (−1)^k·n!/(k!·3^k) with k = n/3. So
  **a(n) = n·a(n − 1) + [3 | n]·t(n)**.
- t(n) is ± the product of the numbers up to n that 3 does not divide,
  because n!/(k!·3^k) drops the factors 3, 6, …, 3k. From n − 1 to n it is
  multiplied by n when 3 ∤ n and by −1 when 3 | n.
- `t*=-n**x` with `x=n%3>0` multiplies by −n when 3 ∤ n and by −1 when
  3 | n. That gives t an extra sign (−1)^(n−k) compared with t(n), and
  at n = 3k that is (−1)^(2k) = 1: t is wrong only where it is not used.
  This is 2 bytes shorter than the true ratio, `t*=n%3and n or-1`.
- `~-x` is x − 1, so `a*n-t*~-x` is a·n when 3 ∤ n and a·n + t when
  3 | n. Keeping `n%3>0` in `x` with a walrus is a byte shorter than
  writing `n%3<1` again.
- `while[print(a)]:` prints and loops forever, because `[None]` is a
  non-empty list: a byte shorter than `while 1:print(a);`.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (101 terms) prints at once. a(1559) has 4303 digits,
  past Python's 4300-digit int-to-str limit, so the program stops there
  with a `ValueError` after 1559 terms, in about 0.3 s. The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000090), CC BY-SA 4.0.
