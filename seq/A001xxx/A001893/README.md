# A001893

> Number of permutations of (1,...,n) having n-3 inversions (n>=3).
> — [OEIS A001893](https://oeis.org/A001893)

Offset 3: 1, 3, 9, 29, 98, 343, 1230, 4489, 16599, 61997, 233389, 884170, 3366951, …

### Python 3 — 88 bytes

```python
p=[1,1];z=[s:=0,0]
while 1:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)];print(p[len(z)-3])
```

**How it works**

- Counting the permutations of n letters by inversions gives the Mahonian
  polynomial [1]·[2]⋯[n], with [m] = 1 + x + ⋯ + x^(m−1), and a(n) is its
  coefficient of xⁿ⁻³.
- The multiplication is the one of [A000707](../../A000xxx/A000707/):
  `z` holds m zeros, `zip(p+z,z+p)` pairs each coefficient with the one m
  places earlier, so `a-b` runs over p·(1 − x^m), and the running sum `s`
  divides by 1 − x. The coefficients of p·(1 − x^m) add up to 0, so `s` is
  back to 0 after every round (it is set once, in `z=[s:=0,0]`).
- The loop starts from p = [1]·[2] = 1 + x with two zeros in z, then
  multiplies before printing: after `z+=0,` there are m zeros, p is
  [1]⋯[m], and `p[len(z)-3]` is a(m), starting at m = 3. Starting from
  p = [1] instead would print p[−1] for m = 2, a term the sequence does
  not have.

**Notes**

- Exact integer additions; the only fact used is the product formula for
  inversions, so the program is right for every n.
- p keeps the whole product, about m²/2 integers, so time and memory grow
  like m³: about 500 terms in 15 s here, using under 200 MB. The timeout
  is 15 s to keep a run under 300 MB.
- The b-file has 998 terms (n = 3 to 1000); the bar is 400 terms in 15 s.
- Same family: [A000707](../../A000xxx/A000707/) (n − 1 inversions),
  [A001892](../A001892/) (n − 2) and [A001894](../A001894/) (n − 4).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001893), CC BY-SA 4.0.
