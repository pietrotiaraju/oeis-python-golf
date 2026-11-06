# A000339

> Number of partitions into non-integral powers.
> — [OEIS A000339](https://oeis.org/A000339)

Offset 2: 1, 5, 18, 45, 100, 185, 323, 522, 804, 1180, 1687, 2322, 3139, …

### Python 3 — 62 bytes

```python
n=2
while[print(sum(s*s//4//n//n for s in range(n*n+1)))]:n+=1
```

**How it works**

- As the OEIS comment puts it, a(n) counts the pairs of integers
  1 ≤ x ≤ y with √x + √y ≤ n: Agarwala and Auluck's partitions of n into
  two parts k^(1/2), counted with ≤.
- Write y = x + t with t ≥ 0. Then √(x + t) ≤ n − √x is the same as
  t ≤ n² − 2n√x (squaring is safe: the right-hand side then forces
  √x ≤ n/2), and with s = n² − t this is s² ≥ 4n²x with 0 ≤ s ≤ n². So
  the pairs (x, y) correspond one to one to the pairs (s, x) with
  0 ≤ s ≤ n² and 1 ≤ x ≤ s²/(4n²), and

  a(n) = Σ_{s=0}^{n²} ⌊s²/(4n²)⌋.

  For example a(3) = ⌊36/36⌋ + ⌊49/36⌋ + ⌊64/36⌋ + ⌊81/36⌋ = 1 + 1 + 1 + 2 = 5.
- That is integer arithmetic only, so the program is exact with no square
  root at all; `s*s//4//n//n` is ⌊s²/(4n²)⌋ because nested floor
  divisions by positive integers compose.

**Notes**

- Round n takes n² + 1 steps, so the program prints about 740 terms in
  60 s of the 7031 in the b-file. The bar is 560 terms in 60 s.
- Counting the pairs directly with the squared test
  (n² − x − y ≥ 0 and (n² − x − y)² ≥ 4xy) or summing
  n² − isqrt(4n²x − 1) over x ≤ n²/4 is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000339), CC BY-SA 4.0.
