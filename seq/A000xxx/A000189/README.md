# A000189

> Number of solutions to x^3 == 0 (mod n).
> — [OEIS A000189](https://oeis.org/A000189)

Offset 1: 1, 1, 1, 2, 1, 1, 1, 4, 3, 1, 1, 2, 1, 1, 1, 4, 1, 3, 1, 2, 1, 1, 1, 4, 5, …

### Python 3 — 53 bytes

```python
n=1
while[print(sum(x**3%n<1for x in range(n)))]:n+=1
```

**How it works**

- The definition, taken literally: count the residues x = 0, …, n−1 with
  n | x³. No factoring. It is the [A000188](../A000188/) program with `x*x`
  turned into `x**3`, one byte more.
- Why it matches the formula a(p^e) = p^⌊2e/3⌋: n | x³ exactly when
  p^⌈e/3⌉ | x for every p^e ∥ n, so the solutions are the multiples of
  m = ∏ p^⌈e/3⌉ (= [A019555](https://oeis.org/A019555)(n)) below n, and there
  are n/m = ∏ p^(e−⌈e/3⌉) = ∏ p^⌊2e/3⌋ of them.
- `while[print(…)]:` is a byte under `while 1:…;` (a one-element list is
  always true), and `<1for` saves the space before `for`.

**Notes**

- Exact integer arithmetic, correct for every n. Each term costs n steps,
  so the whole b-file (10000 terms) takes about 18 s here. The bar is the
  whole b-file in 60 s.
- Tried and longer: a growing list `r=[1]` / `for n in r:` that doubles as
  the range of x (55 B), and n/A019555(n) or a max over divisors d of
  gcd(d², n/d) (both need far more than the count).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000189), CC BY-SA 4.0.
