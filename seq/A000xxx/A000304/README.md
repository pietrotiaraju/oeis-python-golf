# A000304

> a(n) = a(n-1)*a(n-2).
> — [OEIS A000304](https://oeis.org/A000304)

Offset 2: 2, 3, 6, 18, 108, 1944, 209952, 408146688, 85691213438976, …

### Python 3 — 33 bytes

```python
a,b=2,3
while[print(a)]:a,b=b,a*b
```

**How it works**

- A window of two terms: a is the term to print and b the next one. The tuple
  assignment moves the window, `a,b=b,a*b`, exactly as the Fibonacci loop of
  [A000045](../A000045/) with `*` in place of `+`.
- The seeds are a(2) = 2 and a(3) = 3 (the OEIS data and b-file start there).
- `while[print(…)]:` is a non-empty list, so it is always true.

**Notes**

- Products of integers, so every term is exact. a(n) = 2^F(n−3)·3^F(n−2) with
  F(−1) = 1, the same Fibonacci exponents as [A000301](../A000301/).
- [A000301](../A000301/) saves a byte with `a=b=2` and
  `while[print(a:=b//a)]:b*=a`, which keeps a(n−1) and a(n+1) and divides.
  Here that needs a = 3/2 before the first pass, since a(1) = a(3)/a(2) is
  not an integer, and equal seeds cannot work either: they would make every
  term a power of one number, but the terms need both 2 and 3. A search over
  update chains of products and exact quotients of the two variables (up to
  three statements, 11 bytes of printed expression plus body) found nothing
  shorter; the best of them, `while[print(a)]:b=a*(a:=b)`, is 34 bytes.
- a(22) has 4487 digits, past Python's 4300-digit limit for converting an int
  to a string: the program prints a(2)…a(21) (20 terms) and stops with a
  `ValueError`. That is an interpreter limit, not a wrong term. The b-file has
  17 terms (n = 2 to 18); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000304), CC BY-SA 4.0.
