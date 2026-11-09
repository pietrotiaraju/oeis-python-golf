# A001429

> Number of n-node connected unicyclic graphs.
> — [OEIS A001429](https://oeis.org/A001429)

Offset 3: 1, 2, 5, 13, 33, 89, 240, 657, 1806, 5026, 13999, 39260, 110381, 311465, …

A connected graph with n nodes and n edges has exactly one cycle, of some
length k ≥ 3, and a rooted tree hangs from each node of the cycle. So the
graphs are the cycles of k ≥ 3 rooted trees up to rotation and reflection:
a(n) = [xⁿ] Σ_{k≥3} Z(D_k; T), where T = Σ tₙxⁿ counts rooted trees
([A000081](../../A000xxx/A000081/)) and Z(D_k) is the cycle index of the
dihedral group.

### Python 3 — 318 bytes

```python
import math
t=[0,1];u=[0];p=[0];n=1
while 1:q=sum(t[i]*(t[n-i]+(2*i==n))for i in range(n))//2;u+=n*t[n]+sum(t[i]*u[-i]for i in range(n)),;p+=t[n]+q+sum(t[i]*p[-2*i]for i in range(n//2+1)),;n>2==print((sum(u[math.gcd(j,n)]for j in range(n))//n+p[n])//2-t[n]-q);t+=sum(d*t[-d]*sum(t[d::d])for d in range(-n,0))//-n,;n+=1
```

**How it works**

- **Sum over all k first.** Z(D_k) = Z(C_k)/2 + R_k/2, where R_k averages
  the k reflections. Summed over every k ≥ 1:
  - the rotations give the necklaces of trees,
    Σ_k Z(C_k; T) = Σ_d (φ(d)/d) log 1/(1 − T(x^d)). With
    u = xT′/(1 − T) (x times the derivative of log 1/(1 − T)), its n-th
    coefficient is yₙ = (1/n) Σ_{j<n} u_gcd(j,n);
  - the reflections give Σ_k R_k = (T + q)/(1 − T₂) =: ρ, with T₂ = T(x²)
    and q = (T² + T₂)/2 (an odd cycle has one fixed tree and pairs, an even
    one either none or two).
  
  The cycles of length 1 and 2 contribute T and q, so
  a(n) = (yₙ + ρₙ)/2 − tₙ − qₙ.
- **One recurrence per series**, each list filled up to index n in turn:
  - `q` = (Σ tᵢtₙ₋ᵢ + t_{n/2})/2; the `(2*i==n)` term adds t_{n/2} when n
    is even;
  - uₙ = n·tₙ + Σ tᵢuₙ₋ᵢ, from u = xT′ + T·u;
  - ρₙ = tₙ + qₙ + Σ tᵢρₙ₋₂ᵢ, from ρ = T + q + T₂·ρ;
  - tₙ₊₁ = (1/n) Σ_k k·t_k Σ_j tₙ₊₁₋ⱼₖ is the rooted-tree recurrence. It
    runs over negative `d` (as on [A001372](../A001372/)): `t[-d]` is t_k
    and `t[d::d]` walks down from tₙ₊₁₋ₖ in steps of k.
- **Negative indices.** While `u` and `p` hold n entries, `u[-i]` is uₙ₋ᵢ
  and `p[-2*i]` is ρₙ₋₂ᵢ. The i = 0 terms read index 0 but are multiplied by
  t₀ = 0.
- `n>2==print(…)` is a chained comparison, so it prints only from n = 3, the
  offset. a(1) = a(2) = 0 are computed but not printed.

**Notes**

- Exact integer arithmetic for every n; every division is exact.
- About O(n log n) work per term: the whole 498-term b-file (a(500) has 236
  digits) prints in about half a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 318 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001429), CC BY-SA 4.0.
