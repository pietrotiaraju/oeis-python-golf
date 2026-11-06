# A000314

> Number of mixed Husimi trees with n nodes; or labeled polygonal cacti with bridges.
> — [OEIS A000314](https://oeis.org/A000314)

Offset 0: 1, 1, 1, 4, 31, 362, 5676, 111982, 2666392, 74433564, 2384579440, 86248530296, 3476794472064, …

### Python 3 — 107 bytes

```python
a=b=c=n=1
while[print(c)]:c=1;N=0;exec("a,b,c=b,c,(2*N+n)*c-N*(N-1+n)*b+N*~-N//2*n*a;N+=1;"*~-n);c//=n;n+=1
```

**How it works**

- For n ≥ 1, a(n) = b(n)/n, where b = [A035351](https://oeis.org/A035351)
  counts the same cacti rooted at a node (every labeled cactus has n
  choices of root). The rooted e.g.f. satisfies B = x·exp(φ(B)) with
  φ(y) = (2y − y²)/(2 − 2y) = y/2 + y/(2(1−y)): the root sits on a set of
  bridges (y each) and polygons with k ≥ 2 further nodes (y^k/2 each, a
  polygon read in either direction being the same).
- Lagrange inversion gives b(n) = (n−1)!·[y^(n−1)] exp(n·φ(y)) =
  P_{n−1}(n), with P_N(z) = N!·[y^N] exp(z·φ(y)).
- G = exp(z·φ(y)) solves the linear equation
  2(1−y)²·G′ = z·(1 + (1−y)²)·G, because φ′(y) = (1 + (1−y)^−2)/2.
  Reading off the coefficient of y^N gives a three-term recurrence:

  P_{N+1} = (2N+z)·P_N − N(N−1+z)·P_{N−1} + z·N(N−1)/2·P_{N−2},

  with P_0 = 1. The program runs it with z = n from N = 0 to n−2 in the
  window `a,b,c`, then divides by n. N(N−1)/2 is an integer, so
  `N*~-N//2` is exact.
- The coefficients of `b` and `a` vanish at N = 0 and N = 0, 1, so their
  values from the previous n never matter, and only `c=1;N=0` is reset.
- `c//=n` stores a(n) in `c` and the loop condition prints it; the start
  value `c=1` is a(0). The term for n = 1 runs the recurrence zero times
  (P_0 = 1).

**Notes**

- Each term costs n steps of the recurrence, so the program is quadratic
  per term: it prints about 1290 terms in 60 s, before the 4300-digit
  int-to-str limit of Python 3.11+ is reached.
- Alternatives: a `for N in range(n-1)` loop instead of `exec` is
  2 bytes longer, a walrus comprehension 2 bytes longer, and printing
  `c//n` after the loop with `print(n:=1)` for a(0) is 113 bytes. Summing
  the block formula a(n) = Σ (n−1)!·n^(k−1)·Π c_j^(m_j)/m_j! over the
  numbers m_j of blocks of each size needs `math` and is much longer.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (n = 0 to 100); they print in under a second.
  The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000314), CC BY-SA 4.0.
