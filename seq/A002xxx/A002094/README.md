# A002094

> Number of unlabeled connected loop-less graphs on n nodes containing exactly one cycle (of length at least 2) and with all nodes of degree <= 4.
> — [OEIS A002094](https://oeis.org/A002094)

Offset 1: 0, 1, 2, 5, 10, 25, 56, 139, 338, 852, 2145, 5513, …

### Python 3 — 294 bytes

```python
from math import*
L=1,;T=[1];u=[0];r=[1];n=0
while 1:L+=(g:=sumprod(L,L[::-1])+L[3*n]>>1)+L[3*n],;L+=*[0]*4,(sumprod(L,L[::-1])+2*L[2*n])//6;n+=1;T+=g,;u+=n*g+sumprod(T[1:],u[::-1]),;r+=sumprod(T,T[::-1])+sumprod(T[1:n//2+1],r[-2::-2]),;print((sum(u[gcd(j,n)]for j in range(n))*2//n+r[n])//4-g)
```

**How it works**

- **Decomposition.** The graph is its cycle, of length k ≥ 2 (k = 2 is a
  double edge), with a tree hanging from each cycle vertex. A cycle vertex
  has two cycle edges, so it keeps at most 2 children; every other node
  has its parent edge and at most 3 children. Let A(x) count rooted trees
  whose nodes have at most 3 children (A₀ = 1 for the empty tree:
  [A000598](../A000598/)), A = 1 + x·S₃(A), and let
  t(x) = x·S₂(A) = x(A(x)² + A(x²))/2 count the hanging trees with their
  cycle vertex (t is x times [A000642](../A000642/)). By Pólya, a(n) is
  [xⁿ] Σ_{k≥2} Z(D_k; t), D_k the dihedral group of the k-gon (for k = 2
  it just swaps the two vertices).
- **Summing over k.** As on [A001429](../A001429/), Z(D_k) is half the
  rotations plus half the reflections:
  - Σ_{k≥1} Z(C_k; t) = Σ_d (φ(d)/d)·log 1/(1 − t(x^d)), whose n-th
    coefficient is yₙ = (1/n) Σ_{j<n} u_gcd(j,n) with u = xt′/(1 − t);
  - the reflections give Σ_{k≥1} R_k = (t + (t² + t(x²))/2)/(1 − t(x²))
    (odd k: one fixed vertex and pairs; even k: two fixed vertices and
    pairs, or only pairs), and twice that is s − 1 with
    s = (1 + t)²/(1 − t(x²)).

  The k = 1 term is t, so a(n) = (2yₙ + sₙ)/4 − tₙ for n ≥ 1.
- **Series, one coefficient per pass** (pass n appends index n):
  - `L` is the interleaved tuple of [A000642](../A000642/): `L[6e]` is
    Aₑ and `L[6e+1]` is (S_e + 3A_{e/2})/2 with S = A², so that one
    `sumprod(L,L[::-1])` gives [xⁿ]A², and right after the second slot
    is appended, 2[xⁿ]A·K; `L[3*n]` and `L[2*n]` read A(x²) and A(x³).
    `g` is ([xⁿ]A² + [xⁿ]A(x²))/2 = tₙ₊₁.
  - `T` = 1, t₁, …, tₙ (the leading 1 makes `sumprod(T,T[::-1])` the
    coefficient of (1 + t)²).
  - uₙ = n·tₙ + Σ_{i≥1} tᵢuₙ₋ᵢ, from u = xt′ + t·u.
  - sₙ = [xⁿ](1 + t)² + Σ_{i≥1} tᵢ·s_{n−2i}, from s = (1 + t)² + t(x²)·s,
    with s₀ = 1; `T[1:n//2+1]` against `r[-2::-2]` = s_{n−2}, s_{n−4}, …
- The print is (2·Σ_{j<n} u_gcd(j,n)/n + sₙ)/4 − tₙ.

**Notes**

- Exact integer arithmetic; every division is exact (the sums are
  orbit counts), so the program is right for every n.
- O(n) big-integer operations per term: the whole b-file (400 terms,
  a(400) has 177 digits) takes about 0.25 s here; the bar is all 400 in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 294 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002094), CC BY-SA 4.0.
