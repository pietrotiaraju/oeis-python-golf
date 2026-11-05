# A000201

> Lower Wythoff sequence (a Beatty sequence): a(n) = floor(n*phi), where phi = (1+sqrt(5))/2 = A001622.
> — [OEIS A000201](https://oeis.org/A000201)

Offset 1: 1, 3, 4, 6, 8, 9, 11, 12, 14, 16, …

### Python 3 — 43 bytes

```python
l=[2]
for d in l:l+=(1,2)[-d:print(len(l))]
```

**How it works**

- The differences a(n+1) − a(n) form the Fibonacci word on {2, 1}:
  F = 2 1 2 2 1 2 1 2 2 1 2 2 …, the fixed point of φ: 2 → 21, 1 → 2.
  (Coded 0 = 2, 1 = 1 this is the Fibonacci word 0100101001…; its zeros
  sit at ⌊nφ⌋, and the images φ(F_k) start exactly at those zeros.)
- With the conjugate map φ′: 2 → 12, 1 → 2, one has 2·φ′(w) = φ(w)·2
  letter by letter, so for the infinite word F = 2·φ′(F). The list `l`
  starts as `[2]` and appends φ′(d) for each element d it reads. A list
  iterator sees items appended during the loop, so this builds F forever.
- |φ′(d)| = d, so when the loop reaches F_k the list has length
  1 + F_0 + … + F_{k−1} = a(1) + (a(k+1) − a(1)) = a(k+1). That length is
  the term: no counter is needed.
- φ′(d) is `(1,2)[-d:]`: the whole tuple for d = 2, just `(2,)` for d = 1.
  `print` returns `None`, so it fits in the slice's end: `[-d:None]` is
  `[-d:]`, and the print runs before `+=` grows the list. One byte under
  `print(len(l));l+=(1,2)[-d:]`.

**Notes**

- No floats and no square roots, so it is correct for every n; it rests on
  the classical fact that the zeros of the Fibonacci word are at ⌊nφ⌋
  (the Fibonacci word is the characteristic Sturmian word of slope 1/φ²).
- The list holds about 1.6 entries per printed term, so memory grows
  linearly. It prints the whole b-file (10000 terms) at once; the bar is the
  whole b-file in 60 s.
- The arithmetic route, a(n) = a(n−1) + 1 + [5n² > (2a(n−1) + 4 − n)²],
  is 51 bytes; `(n+isqrt(5*n*n))//2` with `from math import*` is 58.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000201), CC BY-SA 4.0.
