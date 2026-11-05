# A000068

> Numbers k such that k^4 + 1 is prime.
> — [OEIS A000068](https://oeis.org/A000068)

Offset 1: 1, 2, 4, 6, 16, 20, 24, 28, 34, 46, 48, 54, 56, 74, 80, 82, 88, …

### Python 3 — 60 bytes

```python
k=1
while[-1in(k**4%~d for d in range(k*k))or print(k)]:k+=1
```

**How it works**

- `k` runs over 1, 2, 3, … and N = k⁴ + 1 is the number to test.
- Trial division. If N is composite it has a divisor m with
  2 ≤ m ≤ √N < k² + 1, so the candidates m = 1, …, k² cover every divisor
  that matters.
- `~d` is −d − 1, so as `d` runs over `range(k*k)`, `~d` runs over
  −1, −2, …, −k², that is, −m for m = 1, …, k². Starting at 0 saves the `2,`
  that `range(2,k*k)` would need.
- Python's `%` takes the sign of the divisor: with k⁴ = qm + r and
  0 ≤ r < m, `k**4%-m` is r − m when r > 0 and 0 when r = 0. It is −1 exactly
  when r = m − 1, that is, when m divides k⁴ + 1. m = 1 gives 0, so it never
  counts as a divisor, and m = k² gives 0 too.
- `**` and the unary `~` both bind tighter than `%`, so `k**4%~d` needs no
  parentheses, and `-1in(…)` is `(-1) in (…)`.
- `in` stops the generator at the first hit, so a composite N with a small
  factor is dismissed at once: every odd k > 1 falls to m = 2. When there is
  none, `or` goes on to `print(k)`. For k = 1 the only candidate is m = 1 and
  N = 2 is printed.
- The list around it is non-empty, so the loop never stops, as in
  [A000028](../A000028/).
- Exact integer arithmetic and a complete divisor search: the program is
  right for every k, with no probable-prime test. Whether there are
  infinitely many terms is open (it is a case of Landau's fourth problem), so
  the program keeps searching forever.

**Notes**

- The terms after 1 are twice those of [A000059](../A000059/), and the cost
  is the same: a prime N costs k² divisions. 120 terms (k = 1142) print in
  about 7 s, 150 in 15 s and about 230 in a minute. The b-file's 10 000 terms
  reach k = 163 670, out of reach of trial division. The bar is 120 terms in
  60 s.
- `1in(-k**4%d for d in range(2,k*k))` is the direct form, 61 bytes:
  (−k⁴) mod d is 1 exactly when d divides k⁴ + 1.
- `k=0` + `while k:=k+1:-1in(k**4%~d for d in range(k*k))or print(k)` is 61.
- Odd prime factors of k⁴ + 1 are 1 mod 8, but `range(9,k*k,8)` would also
  skip 2, and then odd k would slip through: 3⁴ + 1 = 2 · 41 has no other
  factor below 9.
- Fermat's test is shorter but wrong: 2³² + 1 = 256⁴ + 1 is
  641 · 6 700 417, yet 2^(N−1) ≡ 1 (mod N), as for every Fermat number, so it
  would print 256.
- `from sympy import*` + `k=1` +
  `while[isprime(k**4+1)and print(k)]:k+=1` is 62 bytes, longer than plain
  Python, and above 3.3·10²⁴ `isprime` is the BPSW probable-prime test, which
  is not proved. So there is no sympy entry.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000068), CC BY-SA 4.0.
