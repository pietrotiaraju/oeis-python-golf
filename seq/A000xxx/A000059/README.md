# A000059

> Numbers k such that (2k)^4 + 1 is prime.
> — [OEIS A000059](https://oeis.org/A000059)

Offset 1: 1, 2, 3, 8, 10, 12, 14, 17, 23, 24, 27, 28, 37, 40, 41, 44, 45, …

### Python 3 — 64 bytes

```python
m=2
while[1in(-m**4%d for d in range(2,m*m))or print(m//2)]:m+=2
```

**How it works**

- `m` runs over the even numbers 2, 4, 6, … and is 2k, so N = m⁴ + 1 is the
  number to test and `m//2` is k.
- Trial division. If N is composite it has a divisor d with
  2 ≤ d ≤ √N < m² + 1, and d = m² never divides N (it leaves remainder 1), so
  `range(2,m*m)` holds every divisor that matters.
- d divides m⁴ + 1 exactly when −m⁴ ≡ 1 (mod d), and for d ≥ 2 that is
  `-m**4%d==1`. `**` binds tighter than the unary minus, and the minus
  tighter than `%`, so `-m**4%d` is (−m⁴) mod d with no parentheses.
- `1in(…)` asks whether that remainder is ever 1, that is, whether N has a
  divisor. `in` stops the generator at the first hit, so a composite N with a
  small factor is dismissed at once. When there is none, `or` goes on to
  `print(m//2)`.
- The list around it is non-empty, so the loop never stops, as in
  [A000028](../A000028/).
- Exact integer arithmetic and a complete divisor search: the program is
  right for every k, with no probable-prime test.

**Notes**

- A prime N costs m² ≈ 4k² divisions, and primes are what cost: 120 terms
  (k = 572) print in about 8 s, 150 in 20 s and about 200 in a minute. The
  b-file's 10 000 terms reach k = 81 840, where √N ≈ 2.7·10¹⁰, out of reach of
  trial division. The bar is 120 terms in 60 s.
- Every prime factor of m⁴ + 1 with m even is 1 mod 8, so
  `range(9,m*m,8)` is eight times faster for 2 more bytes (66).
- `all(-~m**4%d for d in range(2,m*m))and print(m//2)` is 66 bytes:
  `-~x` is x + 1, and `1in` with `or` saves 1 over `all(…)and`, then testing
  −m⁴ ≡ 1 instead of m⁴ + 1 ≡ 0 saves the `~`.
- Counting k itself, `k=1` +
  `while[1in(-16*k**4%d for d in range(2,4*k*k))or print(k)]:k+=1`, is
  66 bytes: `16*` and `4*` cost 5 and `print(k)` gives back only 3.
- `m=0` + `while m:=m+2:1in(-m**4%d for d in range(2,m*m))or print(m//2)`
  is 65.
- Fermat's test is shorter but wrong: 2³² + 1 = 16 · 128⁴ + 1 is
  641 · 6 700 417, yet 2^(N−1) ≡ 1 (mod N), as for every Fermat number, so it
  would print 128.
- `from sympy import*` + `m=2` +
  `while[isprime(m**4+1)and print(m//2)]:m+=2` is 65 bytes, longer than
  plain Python, and above 3.3·10²⁴ (k > 674 773) `isprime` is the BPSW
  probable-prime test, which is not proved. So there is no sympy entry.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000059), CC BY-SA 4.0.
