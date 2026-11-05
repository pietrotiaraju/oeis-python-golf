# A000139

> a(n) = 2*(3*n)! / ((2*n+1)!*(n+1)!).
> — [OEIS A000139](https://oeis.org/A000139)

Offset 0: 2, 1, 2, 6, 22, 91, 408, 1938, 9614, 49335, 260130, 1402440, …

For n ≥ 1, a(n) is the number of 2-stack-sortable permutations of n letters
(West's conjecture, proved by Zeilberger); it is also the number of rooted
non-separable planar maps with n + 1 edges.

### Python 3 — 55 bytes

```python
a=m=2
while[print(a)]:a=a*27*m*~-m//-~(m:=m+3)//(4*m-2)
```

**How it works**

- **The recurrence.** Dividing the formula for a(n) by the one for a(n−1)
  gives 2(n+1)(2n+1)·a(n) = 3(3n−1)(3n−2)·a(n−1), the D-finite recurrence
  in the entry. Each pass of the loop multiplies by this ratio.
- **The variable.** At the start of the pass that makes a(n), `m` is
  3n − 1, so the numerator (3n−1)(3n−2) is m(m−1), written `m*~-m`.
  `m:=m+3` then moves it to 3n + 2, where m + 1 = 3(n+1) and
  4m − 2 = 6(2n+1). The two divisors multiply to 18(n+1)(2n+1), and the
  27 in front turns 27/18 back into the 3/2 of the recurrence.
- **Evaluation order.** Python evaluates the operands left to right, so
  `a*27*m*~-m` still sees the old m, the walrus inside `-~(…)` updates it,
  and `(4*m-2)` sees the new one. Moving the step into the divisor this way
  is 1 byte shorter than `//(m+4)//(4*m+10);m+=3`.
- **Exactness.** For positive integers p and q, ⌊⌊x/p⌋/q⌋ = ⌊x/(pq)⌋.
  So the two floor divisions give the floor of the exact ratio, which is the
  integer a(n), even when the first quotient on its own is not exact.
- **The start.** a(0) = 2 and the first pass needs m = 3·1 − 1 = 2, so one
  `a=m=2` sets both. `print(a)` sits in the loop condition: it returns
  `None`, and `[None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms:
  - the same recurrence with `m+=3` as a separate statement,
    `a=a*27*m*~-m//(m+4)//(4*m+10);m+=3`, or with `a*=…;a//=…`:
    56 bytes;
  - the recurrence in n itself, `a=2;n=1` and
    `a=a*3*(3*n-1)*(3*n-2)//2//-~n//(n-~n);n+=1`: 66 bytes;
  - the closed form a(n) = 2·C(3n,n)/((2n+1)(n+1)) with `import math`,
    `n=0`, `while[print(2*math.comb(3*n,n)//(n-~n)//-~n)]:n+=1`:
    66 bytes.
- Exact integer arithmetic; correctness for every n rests only on the
  factorial formula. The values were checked against
  2·C(3n,n)/((2n+1)(n+1)) up to n = 6000. The program prints a(0) to
  a(5196) and then stops with a `ValueError` at a(5197), the first term with
  more than 4300 digits (Python's int-to-str limit).
- The b-file has 201 terms (up to a(200)) and all of them print in well
  under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000139), CC BY-SA 4.0.
