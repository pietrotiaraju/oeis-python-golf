# A001326

> Number of equivalence classes of n-valued Post functions of 2 variables under action of semi-direct product of symmetric group S_2 and complementing group D(2,n).
> — [OEIS A001326](https://oeis.org/A001326)

Offset 2: 6, 2862, 537157696, 37252918396015625, 1289303099816839265917858176, …

a(n) counts the functions f: {0,…,n−1}² → {0,…,n−1} up to swapping the two
variables and complementing either of them, x ↦ n−1−x (the complementing
group D(2,n), of order 4). Only the inputs are transformed. On the n×n
grid of inputs the 8 maps are the symmetries of a square.

### Python 3 — 93 bytes

```python
n=2
while[print((n**(k:=n*n)+n**(k+1>>1)+2*(n**(k+3>>2)+n**(-~n//2*n)+n**(k+n>>1)))//8)]:n+=1
```

**How it works**

- By Burnside's lemma a(n) is the average over the 8 symmetries of n^c,
  where c is the number of cycles of the symmetry on the k = n² inputs (a
  function is fixed exactly when it is constant on each cycle).
- The cycle counts, for every n:
  - the identity: k;
  - the two quarter turns (swap and complement one variable): the points
    fall into orbits of 4, plus the centre when n is odd, so ⌈k/4⌉
    (k ≡ 1 mod 4 for odd n), `k+3>>2`;
  - the half turn (complement both): pairs plus the centre, ⌈k/2⌉,
    `k+1>>1`;
  - the two reflections in a middle line (complement one variable): pairs
    of rows, the middle row fixed when n is odd, so n·⌈n/2⌉, `-~n//2*n`;
  - the two diagonal reflections (swap, and swap with both complemented):
    n points on the diagonal and pairs off it, n(n+1)/2, `k+n>>1`.
- So a(n) = (n^k + n^⌈k/2⌉ + 2·(n^⌈k/4⌉ + n^(n⌈n/2⌉) + n^(n(n+1)/2))) / 8,
  and `//8` is exact because Burnside's sum is a multiple of the group
  order. Exact integers throughout, so the program is right for every n.

**Notes**

- a(3) = 2862 is [A001325](../A001325/)(2): the same count for 3 values and
  2 variables.
- Halving first, `((n**k+n**(k+1>>1)>>1)+…)//4`, is 1 byte longer than the
  factor 2.
- The terms grow like n^(n²)/8: a(50) has 4247 digits and a(51) has 4441,
  so Python's 4300-digit limit for printing integers stops the program
  after a(50), in 0.1 s.
- The OEIS b-file is synthesized from the entry: 8 terms (n = 2 to 9). The
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001326), CC BY-SA 4.0.
