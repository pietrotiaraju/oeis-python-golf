# A001435

> Number of connected graphs with n nodes and n+1 edges.
> — [OEIS A001435](https://oeis.org/A001435)

Offset 1: 0, 0, 0, 1, 5, 19, 67, 236, 797, 2678, 8833, 28908, 93569, 300748, 959374, …

The connected graphs with n nodes and n + 1 edges: all graphs counted by
Pólya's method (as on [A001434](../A001434/)), then the connected ones
split off by the inverse Euler transform in two variables.

### Python 3 — 366 bytes

```python
from math import*
f=lambda r,W,*L:r and sum(f(r-j,W*(1<<B*j|1)**(~-j//2)*(~j%2<<B*j//2|1)*prod((1<<B*lcm(j,l)|1)**gcd(j,l)for l in L)%M//j//-~L.count(j),*L,j)for j in range(1,min(L+(r,))+1))or W
n=1
while 1:
 B=n*n;M=1<<B*(n+2);L=[0];P=[1]
 for i in range(1,n+1):P+=f(i,F:=factorial(i))//F,;L+=i*P[i]-sum(L[j]*P[~j]for j in range(i))%M,
 print((L[n]>>B*-~n)//n);n+=1
```

**How it works**

- **All graphs, by Pólya's method.** `f` is the program of
  [A001434](../A001434/) with B = n²: `P[v]` is Σ_e g(v, e)·yᵉ for v nodes,
  truncated after yᵐ, as one big integer in base X = 2^B (the edge-orbit
  weights of the cycle types of S_v, one leaf per partition of v, weights
  v!/z divided by v! at the end).
- **Connected from all graphs.** Unlabeled graphs are multisets of
  connected ones, so with x marking nodes and y edges,
  G(x, y) = exp Σ_k C(xᵏ, yᵏ)/k. Its logarithmic derivative in x,
  Λ = x·G_x/G, has integer coefficients:
  [xⁿyᵐ] Λ = Σ_{k | gcd(n,m)} (n/k)·c(n/k, m/k), where c(a, b) counts
  connected graphs with a nodes and b edges.
- **Λ by one recurrence.** x·G_x = Λ·G gives
  Λᵢ = i·Pᵢ − Σ_{j<i} Λⱼ·Pᵢ₋ⱼ, where Pᵥ = Σ_e g(v, e)yᵉ is the polynomial of
  graphs with v nodes. Each Pᵥ and Λᵢ is one big integer in base X = 2^(n²),
  so a product of polynomials in y is one multiplication. `L[j]*P[~j]` is
  Λⱼ·Pᵢ₋ⱼ while `P` holds i + 1 entries, and the j = 0 term is 0 because
  Λ₀ = 0. The difference is exact digit by digit: each digit of the result is
  Λᵢ[e] ≥ 0, so no borrow crosses digits.
- **Reading c(n, n + 1).** gcd(n, n + 1) = 1, so [xⁿyⁿ⁺¹] Λ = n·c(n, n + 1).
  M = Xⁿ⁺² keeps y⁰…yⁿ⁺¹ and Λₙ < M, so yⁿ⁺¹ is the top digit:
  `(L[n]>>B*-~n)//n`.
- **No digit overflows.** Inside `f` every kept coefficient is at most
  v!·2^C(v,2) < 2^(n²) for v ≤ n. From i·g(i, e) = Σ Λⱼ[e′]·g(i − j, e − e′)
  (all terms ≥ 0), every digit of Λᵢ and of the sum Σ Λⱼ·Pᵢ₋ⱼ is at most
  i·g(i, e) ≤ n·2^C(n,2) < 2^(n²). Digits above the kept ones can overflow
  before `%M`, but carries only move upwards.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Each term recomputes Pᵥ for every v ≤ n; the partitions of n dominate,
  and each term takes about three times as long as the one before: on the
  PC used a(20) arrives after about 5 s. The bar is 21 terms in 60 s;
  the b-file has 40.

### Python 3, 16 terms — 315 bytes

```python
from math import*
f=lambda r,*L:r<1or sum(f(r-j,*L,j)*(1<<B*j|1)**(~-j//2)*(~j%2<<B*j//2|1)*prod((1<<B*lcm(j,l)|1)**gcd(j,l)for l in L)for j in range(1,r+1))%M//r
n=1
while 1:
 B=n*n;M=1<<B*(n+2);L=[0];P=[1]
 for i in range(1,n+1):P+=f(i),;L+=i*P[i]-sum(L[j]*P[~j]for j in range(i))%M,
 print((L[n]>>B*-~n)//n);n+=1
```

**How it works**

- **All graphs, by Pólya's method.** `f` is the cycle-at-a-time recursion of
  [A000717](../../A000xxx/A000717/) (as in the short record of
  [A001434](../A001434/)): it averages the edge-orbit weights over the
  length of the cycle through a fixed point, and each `//r` is exact. It
  visits all 2ᵛ⁻¹ compositions of v, but needs no n! and no multiplicities,
  and its value is P_v directly.
- The rest is the main record's: Λ from the same recurrence, then the same
  digit read-out.

**Limits**

- Exact for every n, but computing every Pᵥ visits about 2ⁿ compositions in
  all: a(15) arrives after about 5 s on the PC used, so the bar is 16
  terms. The main record reaches 21.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 366 | first entry |

**Python 3, 16 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 315 | first entry: cycle-at-a-time Burnside over all compositions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001435), CC BY-SA 4.0.
