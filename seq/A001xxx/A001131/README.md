# A001131

> Number of red-black rooted trees with n-1 internal nodes.
> — [OEIS A001131](https://oeis.org/A001131)

Offset 0: 0, 1, 2, 2, 3, 8, 14, 20, 35, 64, 122, 260, 586, 1296, 2708, 5400, 10468, 19888, …

### Python 3 — 82 bytes

```python
n=0
while 1:B=X=3**n;s=0;exec('B=(B+B*B)%X**-~n;s+=B;B*=B;'*n);print(s//X**n);n+=1
```

**How it works**

- Red-black trees with n leaves (n − 1 internal nodes), either root
  colour; for n = 1 the lone leaf counts. With B_h(x) the black-rooted
  trees of black height h counted by leaves, B₀ = x and
  B_{h+1} = (B_h + B_h²)² (each child of a black node is a black tree or a
  red node over two black trees of the same height), and a red root sits on
  two black trees of equal height, so
  a(n) = [xⁿ] Σ_h C_h with C_h = B_h + B_h². The siblings
  [A001137](../A001137/) (black roots, Σ B_h) and [A001138](../A001138/)
  (red roots, Σ B_h²) count by internal nodes, so
  a(n) = A001137(n−1) + A001138(n−1) for n ≥ 2.
- Same Kronecker substitution as on the [A001137](../A001137/) page: x = X
  = 3ⁿ, reduce mod X^(n+1), every coefficient is a tree count below 3ⁿ (the
  proof there is for exactly these numbers), and since the digits of `s`
  are a(0)…a(n), all below X, `s//X**n` is a(n).
- The round `B=(B+B*B)%X**-~n;s+=B;B*=B` adds the reduced C_h to the sum
  and leaves B_{h+1} = C_h² unreduced: the next round's `%` cleans it up,
  and the digits up to xⁿ are right all along, because carries only go
  upward. This beats `s+=B+B*B;B=(B+B*B)**2%X**-~n` by 2 bytes, and that one
  would also need `%X` in the print, since B² is not reduced when it is
  added.
- `s=0` cannot be merged into `s=B=X=3**n` here as it is on the A001137
  page: the extra x would make a(1) print 2. For n = 0, X = 1 and the
  program prints 0.

**Notes**

- Moon's recurrence a(n) = Σ_k C(2k, n−2k)·a(k) for n ≥ 3 (from Hanna's
  A(x) = x + x² + A((x+x²)²)) as a list program,
  `from math import*` / `a=[0,1,n:=2]` /
  `for x in a:print(x);n+=1;a+=sum(comb(2*m,n-2*m)*a[m]for m in range(n//2+1)),`,
  is 107 bytes.
- Each term is computed from scratch with numbers of about 1.6·n² bits:
  278 terms in 60 s here.
- The b-file has 34 terms (a(0) to a(33), synthesized from the entry); the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001131), CC BY-SA 4.0.
