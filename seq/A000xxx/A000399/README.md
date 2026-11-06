# A000399

> Unsigned Stirling numbers of first kind s(n,3).
> — [OEIS A000399](https://oeis.org/A000399)

Offset 3: 1, 6, 35, 225, 1624, 13132, 118124, 1172700, 12753576, …

### Python 3 — 54 bytes

```python
a=0;b=c=1;n=2
while[print(a:=a*n+b)]:b=b*n+c;c*=n;n+=1
```

**How it works**

- a(n) is the number of permutations of n elements with exactly 3
  cycles. Element n + 1 either joins one of the cycles of a permutation
  of n elements (n places, after any element) or forms a cycle of its
  own, so |s(n+1, k)| = n·|s(n, k)| + |s(n, k−1)|.
- The program keeps a = |s(n, 3)|, b = |s(n, 2)| and
  c = |s(n, 1)| = (n−1)!. Each pass turns them into the values for
  n + 1, in the order a, b, c so that every update still reads the old
  value of the next one.
- The update of a sits inside `print` as a walrus, so the loop starts at
  n = 2 (a = 0, b = c = 1) and its first print is already a(3) = 1. That
  is a byte under `a=1;b=n=3;c=2` with `print(a)` and the update in the
  body.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (410 terms, n = 3 to 412) prints at once; the program stops after
  a(1558), when the next term passes the 4300-digit int-to-str limit of
  Python 3.11+. The bar is the whole b-file in 60 s.
- Reading the coefficient of B³ in B(B+1)…(B+n−1) with B = nⁿ,
  `math.prod(range(B:=n**n,B+n))//B**3%B`, is 72 bytes with the import.
  The sum over pairs, a(n) = Σ_{1≤j<i<n} (n−1)!/(ij) (the coefficient of
  x² in (x+1)…(x+n−1)), is 84,
  and the recurrence a(n) = (n−3)! + (2n−3)a(n−1) − (n−2)²a(n−2) also
  needs three values of state and longer coefficients.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000399), CC BY-SA 4.0.
