# A001244

> Eulerian numbers (Euler's triangle: column k=8 of A008292, column k=7 of A173018).
> — [OEIS A001244](https://oeis.org/A001244)

Offset 8: 1, 502, 47840, 2203488, 66318474, 1505621508, 27971176092, …

a(n) is the number of permutations of 1, …, n with exactly 7 descents
(positions i with π(i) > π(i+1)), that is, with 8 ascending runs.

### Python 3 — 83 bytes

```python
n=8
while[c:=1,print(sum((c:=c*(j+~n)//-~j)*(7-j)**n for j in range(7))+8**n)]:n+=1
```

**How it works**

- The number of permutations of n elements with m descents is
  A(n, m) = Σ_{i=0}^{m+1} (−1)^i·C(n+1, i)·(m+1−i)^n (Graham, Knuth and
  Patashnik, *Concrete Mathematics*, eq. 6.38), the inverse of Worpitzky's
  identity. With m = 7 the i = 8 term is C(n+1, 8)·0^n = 0, so
  a(n) = 8^n + Σ_{i=1}^{7} (−1)^i·C(n+1, i)·(8−i)^n.
- `c` walks through the signed binomials (−1)^i·C(n+1, i) with
  c_i = c_{i−1}·(i − n − 2)/i. The loop index is j = i − 1, so the factor
  is `(j+~n)` = j − n − 1 over `-~j` = j + 1, and the power is (7 − j)^n.
  The division is exact: c_{i−1}·(i − n − 2) = (−1)^i·(n + 2 − i)·C(n+1, i−1)
  = (−1)^i·i·C(n+1, i), and `//` of an exact multiple is exact for either
  sign.
- The i = 0 term, 8^n, is added outside the sum. `c:=1` inside the
  `while` list resets `c` before every term; the list `[1, None]` is
  truthy, so the loop never ends.
- The loop starts at the offset n = 8, where the formula gives 1 (the
  decreasing permutation). Exact integers throughout, so it is right for
  every n.

**Notes**

- Same program as [A001243](../A001243/) (column 7) with every constant
  one higher. Indexing by i itself
  (`(c:=c*(j+~n-1)//j)*(8-j)**n for j in range(1,8)`) is 3 bytes longer,
  and the [A000514](../../A000xxx/A000514/) form with `import math` and
  `math.comb` is 91 bytes.
- The whole b-file prints in about 0.1 s. Python's 4300-digit int-to-str
  limit stops the program at a(4762), the first term with 4301 digits,
  after printing a(8) to a(4761).
- The b-file has 993 terms (a(8) to a(1000)); the bar is the whole b-file
  in 60 s.

## First 700 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(8)…a(707) have to arrive in time.

### Python 3, 700 terms — 82 bytes

```python
n=8
while[print((1-(x:=8**n))**-~n*sum(j**n*x**j for j in range(9))//x**8%x)]:n+=1
```

**How it works**

- The Eulerian numbers come from the generating function
  Σ_{j≥1} j^n·t^j = Σ_k A(n, k)·t^k / (1 − t)^{n+1} (n ≥ 1, k counting
  ascending runs as in A008292). Multiplying by (1 − t)^{n+1} and keeping
  only j ≤ 8 on the left changes nothing below t^9: the dropped terms are
  multiples of t^9.
- So with x = 8^n, the integer N = (1 − x)^{n+1}·Σ_{j=0}^{8} j^n·x^j is
  Σ_{k=1}^{8} A(n, k)·x^k + x^9·Q for some integer Q (negative for odd n,
  among others). The j = 0 term is 0^n = 0.
- The digits do not overlap: 0 ≤ A(n, k) < x for k ≤ 8. Worpitzky's
  identity k^n = Σ_i A(n, i)·C(k+i−1, n) has non-negative terms, and the
  one with i = n + 1 − k is A(n, n+1−k)·1 = A(n, k) (by symmetry), so
  A(n, k) ≤ k^n < 8^n for k ≤ 7. For k = 8 the sum also holds the term
  i = n + 2 − 8, which is A(n, 7)·(n + 1) > 0 for n ≥ 7, so
  A(n, 8) < 8^n as well; base 8^n is enough even though column 8 is the
  one read.
- Then `N//x**8%x` is A(n, 8): Python's `//` and `%` floor, so the
  possibly negative x^9·Q contributes x·Q to N//x^8 and disappears mod x.

**Limits**

- (1 − x)^{n+1} has about 3n² bits, so the terms slow down like a power of
  n: here the 700th term, a(707), arrives after about 24 s (about
  15 reference seconds), as for [A001243](../A001243/), where 800 terms
  took about 27 of the 30 reference seconds allowed. Far short of the
  main bar of 993 terms.
- `pow(1-x,-~n,x**9)` would keep only the low nine digits and print the
  whole b-file at once, but costs 7 bytes (89).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 83 | first entry |
| 2026-11-09 | Python 3, 700 terms | 82 | first entry: generating function at t = 8ⁿ |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001244), CC BY-SA 4.0.
