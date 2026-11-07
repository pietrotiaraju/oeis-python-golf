# A000454

> Unsigned Stirling numbers of first kind s(n,4).
> — [OEIS A000454](https://oeis.org/A000454)

Offset 4: 1, 10, 85, 735, 6769, 67284, 723680, 8409500, 105258076, 1414014888, …

a(n) is the number of permutations of n elements with exactly 4 cycles.

### Python 3 — 66 bytes

```python
a=0;b=1;d=2;c=n=3
while[print(a:=a*n+b)]:b=b*n+c;c=c*n+d;d*=n;n+=1
```

**How it works**

- Write c(n, k) = |s(n, k)|. In a permutation of n + 1 elements, the
  element n + 1 either follows one of the n old elements inside its cycle
  or is a fixed point, so c(n+1, k) = n·c(n, k) + c(n, k−1).
- At the top of the loop `a, b, c, d` hold c(n, 4), c(n, 3), c(n, 2),
  c(n, 1) of the same row n. `a:=a*n+b` makes c(n+1, 4) and prints it;
  then b, c, d are updated in that order, so each line still reads the old
  value of the column below it. The last column c(n, 1) = (n−1)! only
  needs `d*=n`.
- Row 3 is (0, 1, 3, 2), so the first print is c(4, 4) = 1. Since
  c(3, 2) = 3 = n, the start is written `c=n=3` (2 bytes under
  `c=3;n=3`).

**Notes**

- Other versions that print the same terms:
  - the four updates as one tuple assignment from row 4,
    `a=1;b=d=6;c=11;n=4` / `while[print(a)]:a,b,c,d=a*n+b,b*n+c,c*n+d,d*n;n+=1`:
    69 bytes;
  - the coefficient of B⁴ in the rising factorial B(B+1)…(B+n−1) with
    B = nⁿ, `import math` / `n=4` /
    `while[print(math.perm((B:=n**n)+n-1,n)//B**4%B)]:n+=1`: 69 bytes and
    much slower (281 terms in 10 s). Every coefficient is at most n! < nⁿ,
    so the base-B digits do not carry.
- A staggered diagonal as in [A000453](../A000453/) does not help here: the
  multiplier depends on the row, so each column would need its own n + j.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 97 terms print in 0.06 s here. The b-file has 97 terms (up
  to a(100)); the bar is the whole b-file in 60 s.
- a(1559) is the first term with more than 4300 digits, so printing stops
  there (after about 0.3 s).
- [A000399](../A000399/) is the 3-cycle column with the same loop.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 68 | first entry |
| 2026-11-07 | Python 3 | 66 | `c=n=3` shares the start value |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000454), CC BY-SA 4.0.
