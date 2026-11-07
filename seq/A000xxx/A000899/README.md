# A000899

> Number of solutions to the rook problem on an n X n board having a certain symmetry group (see Robinson for details).
> — [OEIS A000899](https://oeis.org/A000899)

Offset 1: 0, 0, 0, 1, 9, 70, 571, 4820, 44676, 450824, 4980274, 59834748, 778230060, 10896609768, 163456629604, 2615335902176, 44460874280032, 800296440705472, 15205636325496568, 304112744618157872, …

### Python 3 — 97 bytes

```python
a=b=c=d=2;e=f=n=1
while[print(f-e+d-b>>3)]:
 if n%2:c,d=d,2*d+~-n*c;e*=n+1
 a,b=b,b+n*a;n+=1;f*=n
```

**The formula**

D₄, the symmetry group of the square, acts on the n! rook solutions
(permutation matrices); a(n) counts the classes whose only symmetry is the
identity (Robinson). The OEIS formula is

a(n) = (n! − 2·I(n) − C(n) + 2·E(⌊n/2⌋)) / 8,

with I = [A000085](https://oeis.org/A000085) (involutions: fixed by a
diagonal reflection), C(n) = 2^⌊n/2⌋·⌊n/2⌋! =
[A037223](https://oeis.org/A037223) (fixed by the half turn) and
E = [A000898](https://oeis.org/A000898) (fixed by both diagonal
reflections). It is Möbius inversion over the subgroups of D₄: the
solutions with trivial stabilizer are n! − C − 2I + 2E (the quarter turns
have Möbius coefficient 0, the axis reflections fix nothing for n ≥ 2),
and each of their classes has 8 members.

**How it works**

- `f` = n!, `a,b` = (I(n−1), I(n)), `c,d` = (E(m−1), E(m)) and
  `e` = C(n), with m = ⌊n/2⌋; `n` starts at 1 (offset 1).
- `a,b=b,b+n*a` is I(n+1) = I(n) + n·I(n−1). `c,d` and `e` move only
  when n is odd, just before n becomes 2m: E(m) = 2·E(m−1) + 2(m−1)·E(m−2)
  with 2(m−1) = n − 1 = `~-n`, and C(2m) = 2m·C(2m−1) = `e*=n+1`.
- I and E are kept doubled (all four seeds are 2, the recurrences are
  linear), so the print is `f-e+d-b>>3` instead of
  `f-e+2*(d-b)>>3`.
- At n = 1, `a` is 2·I(0) = 2 and `c` is a dummy E(−1), multiplied by
  n − 1 = 0 in the first E step (E(1) = 2·E(0)).

**Notes**

- Exact integer recurrences, correct for every n.
- The b-file has 200 terms (n = 1 to 200); they print instantly. The bar is
  the whole b-file.
- [A000900](../A000900/) uses the same `a,b` and `c,d` steps.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000899), CC BY-SA 4.0.
