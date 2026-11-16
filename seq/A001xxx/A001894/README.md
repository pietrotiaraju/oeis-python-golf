# A001894

> Number of permutations of {1,...,n} having n-4 inversions (n>=4).
> — [OEIS A001894](https://oeis.org/A001894)

Offset 4: 1, 4, 14, 49, 174, 628, 2298, 8504, 31758, 119483, 452284, 1720774, …

### Python 3 — 92 bytes

```python
p=[1,2,2,1];z=[s:=0]*3
while 1:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)];print(p[len(z)-4])
```

**How it works**

- Counting the permutations of n letters by inversions gives the Mahonian
  polynomial [1]·[2]⋯[n], with [m] = 1 + x + ⋯ + x^(m−1), and a(n) is its
  coefficient of xⁿ⁻⁴.
- The multiplication is the one of [A000707](../../A000xxx/A000707/):
  `z` holds m zeros, `zip(p+z,z+p)` pairs each coefficient with the one m
  places earlier, so `a-b` runs over p·(1 − x^m), and the running sum `s`
  divides by 1 − x. The coefficients of p·(1 − x^m) add up to 0, so `s` is
  back to 0 after every round (it is set once, in `z=[s:=0]*3`).
- The loop starts from p = [1]·[2]·[3] = 1 + 2x + 2x² + x³ with three
  zeros in z, then multiplies before printing: after `z+=0,` there are m
  zeros, p is [1]⋯[m], and `p[len(z)-4]` is a(m), starting at m = 4. A
  smaller start would print terms below the offset (as p[−1], p[−2]); a
  guard such as `len(z)>3==print(…)` costs two bytes more than the seed.

**Notes**

- Exact integer additions; the only fact used is the product formula for
  inversions, so the program is right for every n.
- p keeps the whole product, about m²/2 integers, so time and memory grow
  like m³: about 500 terms in 15 s here, using under 200 MB. The timeout
  is 15 s to keep a run under 300 MB.
- The b-file has 997 terms (n = 4 to 1000); the bar is 400 terms in 15 s.
- Same family: [A000707](../../A000xxx/A000707/) (n − 1 inversions),
  [A001892](../A001892/) (n − 2) and [A001893](../A001893/) (n − 3).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001894), CC BY-SA 4.0.
