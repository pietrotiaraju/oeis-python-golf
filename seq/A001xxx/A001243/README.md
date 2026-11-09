# A001243

> Eulerian numbers (Euler's triangle: column k=7 of A008292, column k=6 of A173018).
> — [OEIS A001243](https://oeis.org/A001243)

Offset 7: 1, 247, 14608, 455192, 9738114, 162512286, 2275172004, 27971176092, …

a(n) is the number of permutations of 1, …, n with exactly 6 descents
(positions i with π(i) > π(i+1)), that is, with 7 ascending runs.

### Python 3 — 83 bytes

```python
n=7
while[c:=1,print(sum((c:=c*(j+~n)//-~j)*(6-j)**n for j in range(6))+7**n)]:n+=1
```

**How it works**

- The number of permutations of n elements with m descents is
  A(n, m) = Σ_{i=0}^{m+1} (−1)^i·C(n+1, i)·(m+1−i)^n (Graham, Knuth and
  Patashnik, *Concrete Mathematics*, eq. 6.38), the inverse of Worpitzky's
  identity. With m = 6 the i = 7 term is C(n+1, 7)·0^n = 0, so
  a(n) = 7^n + Σ_{i=1}^{6} (−1)^i·C(n+1, i)·(7−i)^n.
- `c` walks through the signed binomials (−1)^i·C(n+1, i) with
  c_i = c_{i−1}·(i − n − 2)/i. The loop index is j = i − 1, so the factor
  is `(j+~n)` = j − n − 1 over `-~j` = j + 1, and the power is (6 − j)^n.
  The division is exact: c_{i−1}·(i − n − 2) = (−1)^i·(n + 2 − i)·C(n+1, i−1)
  = (−1)^i·i·C(n+1, i), and `//` of an exact multiple is exact for either
  sign.
- The i = 0 term, 7^n, is added outside the sum. `c:=1` inside the
  `while` list resets `c` before every term; the list `[1, None]` is
  truthy, so the loop never ends.
- The loop starts at the offset n = 7, where the formula gives 1 (the
  decreasing permutation). Exact integers throughout, so it is right for
  every n.

**Notes**

- Indexing by i itself (`(c:=c*(j+~n-1)//j)*(7-j)**n for j in range(1,7)`)
  is 3 bytes longer. The [A000514](../../A000xxx/A000514/) form with
  `import math` and `math.comb` is 91 bytes; the column-by-column triangle
  recurrence of [A000505](../../A000xxx/A000505/) needs six state values
  here and is about 120 bytes.
- The whole b-file prints in about 0.1 s. Python's 4300-digit int-to-str
  limit stops the program at a(5089), the first term with 4301 digits,
  after printing a(7) to a(5088).
- The b-file has 994 terms (a(7) to a(1000)); the bar is the whole b-file
  in 60 s.

## First 700 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(7)…a(706) have to arrive in time.

### Python 3, 700 terms — 82 bytes

```python
n=7
while[print((1-(x:=8**n))**-~n*sum(j**n*x**j for j in range(8))//x**7%x)]:n+=1
```

**How it works**

- The Eulerian numbers come from the generating function
  Σ_{j≥1} j^n·t^j = Σ_k A(n, k)·t^k / (1 − t)^{n+1} (n ≥ 1, k counting
  ascending runs as in A008292). Multiplying by (1 − t)^{n+1} and keeping
  only j ≤ 7 on the left changes nothing below t^8: the dropped terms are
  multiples of t^8.
- So with x = 8^n, the integer N = (1 − x)^{n+1}·Σ_{j=0}^{7} j^n·x^j is
  Σ_{k=1}^{7} A(n, k)·x^k + x^8·Q for some integer Q (negative for odd n,
  among others). The j = 0 term is 0^n = 0.
- The digits do not overlap: 0 ≤ A(n, k) < x for k ≤ 7. Worpitzky's
  identity k^n = Σ_i A(n, i)·C(k+i−1, n) has non-negative terms, and the
  one with i = n + 1 − k is A(n, n+1−k)·1 = A(n, k) (by symmetry), so
  A(n, k) ≤ k^n ≤ 7^n < 8^n.
- Then `N//x**7%x` is A(n, 7): Python's `//` and `%` floor, so the
  possibly negative x^8·Q contributes x·Q to N//x^7 and disappears mod x.

**Limits**

- (1 − x)^{n+1} has about 3n² bits, so the terms slow down like a power of
  n: here the 700th term, a(706), arrives after about 28 s (about
  17 reference seconds), and a(806) after about 27 reference seconds,
  too close to the limit of 30 for an 800-term bar. Far short of the main
  bar of 994 terms.
- `pow(1-x,-~n,x**8)` would keep only the low eight digits and print the
  whole b-file at once, but costs 7 bytes (89).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 83 | first entry |
| 2026-11-09 | Python 3, 700 terms | 82 | first entry: generating function at t = 8ⁿ |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001243), CC BY-SA 4.0.
