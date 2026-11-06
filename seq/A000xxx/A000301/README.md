# A000301

> a(n) = a(n-1)*a(n-2) with a(0) = 1, a(1) = 2; also a(n) = 2^Fibonacci(n).
> — [OEIS A000301](https://oeis.org/A000301)

Offset 0: 1, 2, 2, 4, 8, 32, 256, 8192, 2097152, 17179869184, …

### Python 3 — 32 bytes

```python
a=b=2
while[print(a:=b//a)]:b*=a
```

**How it works**

- The state is two terms apart: before printing a(n), a holds a(n−1) and
  b holds a(n+1). Then b/a = a(n+1)/a(n−1) = a(n), so `a:=b//a` makes a the
  term to print, and `b*=a` turns b into a(n+1)·a(n) = a(n+2).
- The seeds come from running this once backwards: printing a(0) = 1 needs
  b = a, and the next pass prints b, so a = b = a(1) = 2. One chained
  assignment sets both, 2 bytes under `a,b=1,2`.
- `while[print(…)]:` is a non-empty list, so it is always true.

**Notes**

- Every value is a power of 2 and each `//` divides a(n+1) by a(n−1), a
  factor of it, so the division is exact and every term is exact.
- The plain tuple window `a,b=1,2` + `while[print(a)]:a,b=b,a*b` is 33 bytes,
  and `2**a` over a Fibonacci pair is longer still. A search over update
  chains of products and exact quotients of the two variables (up to three
  statements, 11 bytes of printed expression plus body) found nothing below
  32 bytes.
- a(n) has about 0.301·F(n) digits, so a(22) = 2^17711 (5332 digits) runs into
  Python's 4300-digit limit for converting an int to a string: the program
  prints a(0)…a(21) and stops with a `ValueError`. That is an interpreter
  limit, not a wrong term. The b-file has 19 terms (n = 0 to 18); the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000301), CC BY-SA 4.0.
