# A001950

> Upper Wythoff sequence (a Beatty sequence): a(n) = floor(n*phi^2), where phi = (1+sqrt(5))/2.
> — [OEIS A001950](https://oeis.org/A001950)

Offset 1: 2, 5, 7, 10, 13, 15, 18, 20, 23, 26, 28, 31, 34, 36, 39, …

### Python 3 — 46 bytes

```python
l=[0,1]
for d in l:l+=(0,0,1)[d:print(len(l))]
```

**How it works**

- a(n) = ⌊nφ²⌋ = n + ⌊nφ⌋, as φ² = φ + 1. As on the page of
  [A000201](../../A000xxx/A000201/), the steps ⌊(n+1)φ⌋ − ⌊nφ⌋ follow the
  Fibonacci word F = 0100101001… (0 for a step of 2, 1 for a step of 1),
  so a(n+1) − a(n) = 3 − F(n−1), counting the letters of F from F(0).
- F is fixed by the square of the Fibonacci substitution, 0 → 010,
  1 → 01. Its conjugate σ: 0 → 001, 1 → 01 satisfies 01·σ(x) = φ²(x)·01
  for both letters (01·001 = 010·01 and 01·01 = 01·01), so 01·σ(F) = F.
  The list starts as `[0,1]` and appends σ(d) for each letter d it reads;
  a list iterator sees items appended during the loop, so this writes F
  forever, always ahead of the reader.
- |σ(d)| = 3 − d, so when the loop reaches F(k) the list has length 2
  plus the sum of 3 − F(j) over j < k, which is a(1) + (a(k+1) − a(1)) =
  a(k+1): the length is the term, and no counter is needed.
- σ(d) is `(0,0,1)[d:]`: the whole tuple for d = 0, `(0,1)` for d = 1
  (σ(1) is a suffix of σ(0), which is why this conjugate is used).
  `print` returns `None`, so it sits in the slice end, as in A000201.

**Notes**

- No floats and no square roots, so it is right for every n; it rests on
  the classical fact behind A000201 that the Fibonacci word is the
  characteristic Sturmian word of slope 1/φ² (its zeros sit at ⌊nφ⌋).
- The list holds about 2.6 entries per printed term, so memory grows
  linearly. The whole b-file (10000 terms) comes in a tenth of a second;
  the bar is the whole b-file in 60 s.
- The arithmetic routes are longer: `n*3+math.isqrt(5*n*n)>>1` makes 59
  bytes, and the step test of the k-Wythoff pages (Wythoff's own game is
  k = 1, test `t*(t-m)<m*m`, print `t+m-2`) makes 50.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001950), CC BY-SA 4.0.
