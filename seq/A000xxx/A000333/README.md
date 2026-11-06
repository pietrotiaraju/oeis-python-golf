# A000333

> Number of partitions into non-integral powers.
> — [OEIS A000333](https://oeis.org/A000333)

Offset 1: 1, 5, 15, 40, 98, 237, 534, 1185, 2554, 5391, 11117, 22556, …

### Python 3 — 154 bytes

```python
import math
f=lambda b,m:sum(1+f(b+~c,x)for x in range(1,m+1)if(c:=math.isqrt(M*M*x-1))<b)
n=M=1
while(a:=f(M*n,n*n))<f(M*n+n,n*n)or[print(a),n:=n+1]:M*=2
```

**How it works**

- As the OEIS comment puts it, a(n) counts the nonempty multisets of
  positive integers x₁ ≤ x₂ ≤ … with √x₁ + √x₂ + … ≤ n: Agarwala and
  Auluck's partitions of n into parts k^(1/2), any number of them, counted
  with ≤. For example a(2) = 5: {1}, {2}, {3}, {4}, {1, 1}.
- Square roots are replaced by integer costs ⌈M√x⌉ for a scale M.
  `c=math.isqrt(M*M*x-1)` is ⌈M√x⌉ − 1, so `c<b` says the part fits in the
  budget b and `b+~c` is what is left of it. f(b, m) counts the nonempty
  multisets with parts ≤ m and total cost ≤ b, choosing the largest part
  first (each part is at most the previous one).
- With L = f(Mn, n²) and U = f(Mn + n, n²), L ≤ a(n) ≤ U for every M:
  a multiset counted in L has M·Σ√x ≤ Σ⌈M√x⌉ ≤ Mn; a multiset that
  really fits has at most n parts (each √x ≥ 1), all ≤ n², and total cost
  below MΣ√x + n ≤ Mn + n. So when L = U that is a(n), and the program
  prints it; otherwise it doubles M and tries again.
- Why L = U happens for some M: U only ever counts multisets with
  Σ√x ≤ n + n/M ≤ 2n, a finite set. One with Σ√x > n drops out of U once
  M(Σ√x − n) > n, and one with Σ√x < n enters L once M(n − Σ√x) ≥ its
  number of parts. One with Σ√x = n exactly has only perfect squares as
  parts (the square roots of distinct squarefree numbers are linearly
  independent over ℚ, Besicovitch 1940), so its costs are exact and it is
  in L for every M.
- M is never reset: it only grows, which is harmless and saves the work of
  doubling from 1 again for each term (it also doubles once more after each
  printed term, because the `while` body runs then too).

**Notes**

- The tree has about a(n) nodes and each loops over at most its smallest
  part, so the program prints 20 terms in about 35 s; the b-file has 50.
  The bar is 15 terms in 60 s. The recursion is at most 2n deep.
- Separate floor and ceiling costs with the same budget (an extra argument
  e and `math.isqrt(M*M*x-e)+e`) are 8 bytes longer; starting M again at 1
  for each n prints only 15 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 154 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000333), CC BY-SA 4.0.
