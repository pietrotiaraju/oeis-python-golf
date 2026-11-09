# A001266

> One-half the number of permutations of length n without rising or falling successions.
> — [OEIS A001266](https://oeis.org/A001266)

Offset 2: 0, 0, 1, 7, 45, 323, 2621, 23811, 239653, 2648395, 31889517, 415641779, …

A succession is a pair i, i+1 standing next to each other, in either
order. Reversing a permutation keeps its successions and never gives the
same permutation back (n ≥ 2), so the permutations without one come in
pairs: a(n) is half of Hertzsprung's number A(n),
[A002464](https://oeis.org/A002464), the column k = 0 of
[A001100](../A001100/).

### Python 3 — 73 bytes

```python
a=b=1;c=d=m=0
while[print(c//2)]:m+=1;a,b,c,d=b,c,d,m*(d-c-b+a)+4*d-c+2*b
```

**How it works**

- Hertzsprung's numbers satisfy, for n ≥ 4,

  **A(n) = (n+1)A(n−1) − (n−2)A(n−2) − (n−5)A(n−3) + (n−3)A(n−4),**

  with A(0..3) = 1, 1, 0, 0. With m = n − 3 the right side is
  m·(A(n−1) − A(n−2) − A(n−3) + A(n−4)) + 4A(n−1) − A(n−2) + 2A(n−3),
  which is the update.
- Why it holds: inclusion–exclusion over sets of glued successions gives
  Flajolet's generating function Σₙ A(n)xⁿ = H(z), H(y) = Σₖ k!·yᵏ,
  z = x(1−x)/(1+x) (see [A000130](../../A000xxx/A000130/)). From
  (k+1)! = (k+1)·k!, y²H′ + (y − 1)H + 1 = 0; substituting y = z and
  clearing denominators,
  x²(1−x)²(1+x)·A′ − (1+x²)(1−2x−x²)·A + (1+x)(1−2x−x²) = 0,
  whose coefficient of xⁿ is the recurrence for n ≥ 4 (the polynomial
  part only reaches x³). The same derivation is on
  [A000544](../../A000xxx/A000544/).
- `a,b,c,d` hold A(n−4) … A(n−1) of the full count, which the recurrence
  needs from A(0) = A(1) = 1 on (their halves are not integers). The loop
  prints `c//2`, starting from A(2)/2 = 0, so the printed index runs two
  behind the window; A(n) is even for n ≥ 2, so the halving is exact.

**Notes**

- Running the halves from a(2..5) = 0, 0, 1, 7 instead, with `print(a)`,
  is 74 bytes (`a=b=m=0;c,d=1,7` and the weights shifted to m = n − 5).
- Exact integer arithmetic; a count of all permutations agrees for
  n ≤ 10.
- The b-file has 449 terms (a(2) to a(450)); the bar is all of them in
  60 s, and they print in a fraction of a second. a(1559) is the first
  term with more than 4300 digits (Python's int-to-str limit), so the
  program stops with a `ValueError` after a(1558).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001266), CC BY-SA 4.0.
