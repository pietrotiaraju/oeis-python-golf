# A001333

> Pell-Lucas numbers: numerators of continued fraction convergents to sqrt(2).
> — [OEIS A001333](https://oeis.org/A001333)

Offset 0: 1, 1, 3, 7, 17, 41, 99, 239, 577, 1393, 3363, 8119, 19601, …

### Python 3 — 33 bytes

```python
a=b=1
while[print(a)]:a,b=b,a+2*b
```

**How it works**

- √2 = [1; 2, 2, 2, …], so the convergent numerators obey
  pₙ = 2pₙ₋₁ + pₙ₋₂ with the usual seeds p₋₁ = 1, p₀ = 1. The entry starts
  from those seeds: a(0) = a(1) = 1 and a(n) = 2a(n−1) + a(n−2), which is
  the formula it gives (1/1, 3/2, 7/5, 17/12, … are the convergents).
- The pair (a, b) holds two consecutive terms; `a,b=b,a+2*b` moves it one
  place, and `a=b=1` sets both seeds at once.
- `print` returns `None` and `[None]` is a non-empty list, so the loop never
  ends. Exact integers, so it is right for every n.

**Notes**

- `a,b=b,a+b+b` and the walrus form `b+=a+(a:=b)` (the right side reads
  the old a before overwriting it) are also 33. Two plain steps,
  `x=1;y=0` + `while[print(x)]:x+=2*y;y=x-y` (x and y the rational and √2
  parts of (1 + √2)ⁿ), are 36. A search over `while[print(a:=E)]:S` forms
  (E and S written with `a b 1 2 + - * ~`) and seeds `a=b=v` found nothing
  shorter.
- a(n) grows like (1 + √2)ⁿ/2, so the terms pass the 4300-digit int-to-str
  limit of Python 3.11+ at n = 11235, where the program stops with a
  `ValueError`.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001333), CC BY-SA 4.0.
