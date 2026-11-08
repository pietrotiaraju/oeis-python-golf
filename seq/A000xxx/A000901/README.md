# A000901

> Number of solutions to the rook problem on a 2n X 2n board having a certain symmetry group (see Robinson for details).
> — [OEIS A000901](https://oeis.org/A000901)

Offset 1: 0, 0, 7, 74, 882, 11144, 159652, 2571960, 46406392, 928734944, 20436096048, …

### Python 3 — 73 bytes

```python
m=0;F=b=c=p=q=1
while 1:c,b,p,q=b,2*b+m*c,q,m*p;m+=2;F*=m;print(F-b-q>>2)
```

**The formula**

D₄, the symmetry group of the square, acts on the (2n)! rook solutions
(permutation matrices) of the 2n × 2n board. The group here is the
half-turn group {1, r²}: a(n) counts the classes of solutions whose only
symmetry is the half turn (a brute-force count of the classes for
2n ≤ 8 gives 0, 0, 7, 74). The OEIS Maple program (`gamma`, doubled up)
is

a(n) = (G − B − R)/4,

- G = 2ⁿ·n! ([A000165](../A000165/)): solutions fixed by the half turn,
  i.e. permutations that commute with i ↦ 2n+1−i;
- B = [A000898](../A000898/)(n), e.g.f. exp(2x + x²), so
  B(n+1) = 2B(n) + 2n·B(n−1): solutions also fixed by one diagonal
  reflection, hence by both;
- R = n!/(n/2)! for even n and 0 for odd n: solutions fixed by the quarter
  turn. A solution fixed by the quarter turn and a diagonal would be fixed
  by an axis reflection, which no permutation matrix of size ≥ 2 is.

So G − B − R solutions have symmetry group exactly {1, r²}, and each class
holds 8/2 = 4 of them.

**How it works**

- `m` holds 2n and `F` = G. At n = 0 every value is 1 (G, B, R at 0) and
  the dummies B(−1), R(−1) are multiplied by m = 0, so one chain sets all
  five; the loop steps to n = 1 before the first print.
- `c,b=b,2*b+m*c` is the [A000898](../A000898/) step, and `p,q=q,m*p` is
  R(n+1) = 2n·R(n−1): for even n+1 = 2j, (2j)!/j! ÷ (2j−2)!/(j−1)! =
  2(2j−1) = 2n, and the odd values stay 0 because R(1) = 0·R(−1).
- `m+=2;F*=m` is G(n+1) = 2(n+1)·G(n), and `F-b-q>>2` the division by 4
  (`-` binds tighter than `>>`).

**Notes**

- Exact integer recurrences, correct for every n.
- 1423 terms print almost at once; a(1424) has more than 4300 digits and
  `str()` stops the program with a `ValueError` (Python 3.11+ limit).
- The b-file has 403 terms (n = 1 to 403); the bar is the whole b-file.
- Printing in the loop test, `while[print(F-b-q>>2)]:`, needs the n = 1
  state as seeds (`m=F=b=2;c=p=1;q=0`): 74 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000901), CC BY-SA 4.0.
