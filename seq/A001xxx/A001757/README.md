# A001757

> Expansion of an integral: central elements of rows of triangle in A059366.
> — [OEIS A001757](https://oeis.org/A001757)

Offset 0: 1, 1, 2, 9, 54, 450, 4500, 55125, 771750, 12502350, …

### Python 3 — 50 bytes

```python
a=j=1
while[print(a)]:j+=1;a=a*~-j*(j-2|1)//(j>>1)
```

**How it works**

- The triangle A059366 is T(n, k) = C(2k, k)·C(2n−2k, n−k)·n!/2ⁿ, and its
  central element is the entry's formula
  a(n) = C(2a, a)·C(2b, b)·n!/2ⁿ with a = ⌊n/2⌋, b = ⌈n/2⌉.
- From n − 1 to n exactly one half grows by one: b if n is odd, a if n is
  even, and in both cases the half that grows ends at ⌈n/2⌉. With
  C(2h, h)/C(2h−2, h−1) = 2(2h−1)/h and the factor n/2 from n!/2ⁿ, the ratio
  is n·(2h−1)/h with h = ⌈n/2⌉, and 2h − 1 is n for odd n and n − 1 for
  even n, that is (n−1)|1. So a(n) = a(n−1)·n·((n−1)|1)/⌈n/2⌉
  (2n²/(n+1) for odd n, 2(n−1) for even n).
- The loop counts j = n + 1, which lets it start with `a=j=1` (a(0) = 1):
  n = `~-j`, (n−1)|1 = `j-2|1`, ⌈n/2⌉ = `j>>1`. The quotient is the integer
  a(n), so the floor division is exact.

**Notes**

- Exact integer arithmetic, correct for every n. a(1425) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- Counting n itself, `a=1;n=0` / `…n+=1;a=a*n*(~-n|1)//(-~n>>1)`, is
  53 bytes; two prints per pass (odd and even step) is longer still.
- The b-file has 22 terms (a(0) to a(21)); the bar is the whole b-file in
  60 s, which prints instantly. The column k = 3 of the same triangle is
  [A001756](../A001756/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001757), CC BY-SA 4.0.
