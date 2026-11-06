# A000347

> Number of partitions into non-integral powers.
> — [OEIS A000347](https://oeis.org/A000347)

Offset 4: 1, 5, 24, 84, 251, 653, 1543, 3341, 6763, 12879, 23446, 40883, …

### Python 3 — 166 bytes

```python
import math
f=lambda b,m,k=4:k<1or sum(f(b+~c,x,k-1)for x in range(1,m+1)if(c:=math.isqrt(M*M*x-1))<b)
n=M=4
while(a:=f(M*n,n*n))<f(M*n+4,n*n)or[print(a),n:=n+1]:M*=2
```

**How it works**

- As the OEIS comment puts it, a(n) counts the quadruples of integers
  1 ≤ w ≤ x ≤ y ≤ z with √w + √x + √y + √z ≤ n: Agarwala and Auluck's
  partitions of n into four parts k^(1/2), counted with ≤.
- This is the floor/ceiling count of [A000333](../A000333/) restricted to
  exactly four parts: f(b, m, k) counts the multisets of k parts ≤ m whose
  costs ⌈M√x⌉ add up to at most b (`c=math.isqrt(M*M*x-1)` is ⌈M√x⌉ − 1,
  `b+~c` the budget left, and `k<1or` counts a finished quadruple).
- L = f(Mn, n²) ≤ a(n) ≤ U = f(Mn + 4, n²) for every M, since four costs
  exceed M·Σ√x by less than 4. When L = U the program prints it, otherwise
  it doubles M. That always ends: a quadruple with Σ√x < n enters L once
  M(n − Σ√x) ≥ 4, one with Σ√x > n leaves U once M(Σ√x − n) > 4, and one with Σ√x = n has only perfect squares as parts
  (square roots of distinct squarefree numbers are linearly independent
  over ℚ, Besicovitch 1940), whose costs are exact.

**Notes**

- Squaring √w + √x + √y + √z ≤ n into an integer test, as
  [A000345](../A000345/) does for three parts, needs three squarings with
  sign cases here and is much longer.
- The program prints 22 terms in about 45 s of the 37 in the b-file (OEIS
  synthesizes it from the entry's terms). The bar is 17 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 166 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000347), CC BY-SA 4.0.
