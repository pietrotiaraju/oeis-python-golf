# A000900

> Number of solutions to the rook problem on an n X n board having a certain symmetry group (see Robinson for details).
> — [OEIS A000900](https://oeis.org/A000900)

Offset 0: 0, 0, 0, 1, 2, 10, 28, 106, 344, 1272, 4592, 17692, 69384, 283560, 1191984, 5171512, 23087168, 105883456, 498572416, 2404766224, …

### Python 3 — 77 bytes

```python
a=b=c=d=1;n=0
while[print(b-d>>1)]:
 if n%2:c,d=d,2*d+~-n*c
 a,b=b,b+n*a;n+=1
```

**The formula**

D₄, the symmetry group of the square, acts on the n! rook solutions
(permutation matrices). The OEIS formula is

a(n) = (I(n) − E(⌊n/2⌋)) / 2,

with I = [A000085](https://oeis.org/A000085) (involutions,
I(n) = I(n−1) + (n−1)·I(n−2)) and E =
[A000898](https://oeis.org/A000898) (E(m) = 2·E(m−1) + 2(m−1)·E(m−2)).
I(n) counts the solutions fixed by a reflection in one diagonal, and
E(⌊n/2⌋) those fixed by both diagonals (involutions that commute with
i ↦ n+1−i; for odd n the middle point is forced). So I − E solutions have
symmetry group exactly {1, d₁}, as many have {1, d₂}, and each such class
holds 8/2 = 4 solutions: (I − E)/2 classes have a diagonal reflection as
their only symmetry.

**How it works**

- `a,b` = (I(n−1), I(n)) and `n` is n: the step `a,b=b,b+n*a` gives
  I(n+1) = I(n) + n·I(n−1), and I(−1) = 1 is harmless because it is
  multiplied by n = 0.
- `c,d` = (E(m−1), E(m)) with m = ⌊n/2⌋. It moves only when n is odd,
  just before n becomes 2m: E(m) = 2·E(m−1) + 2(m−1)·E(m−2), and with
  n = 2m−1 the factor 2(m−1) is `~-n` = n − 1. The dummy E(−1) = 1 is
  multiplied by 0 again.
- Every seed is 1, so one chained assignment sets all four.
- `b-d>>1` halves the difference (`-` binds tighter than `>>`).

**Notes**

- Exact integer recurrences, correct for every n.
- The b-file has 201 terms (n = 0 to 200); they print instantly. The bar is
  the whole b-file.
- Updating `c,d` on every pass with a slice such as
  `c,d=(c,d,2*d+~-n*c)[n%2:n%2+2]` puts the loop on one line, but
  that is 82 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000900), CC BY-SA 4.0.
