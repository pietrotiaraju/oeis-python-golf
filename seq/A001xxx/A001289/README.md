# A001289

> Number of equivalence classes of Boolean functions modulo linear functions.
> — [OEIS A001289](https://oeis.org/A001289)

Offset 1: 1, 2, 3, 8, 48, 150357, 63379147320777408548, …

Two Boolean functions f, g: F₂ⁿ → F₂ are equivalent when
g(x) = f(Mx ⊕ a) ⊕ b·x ⊕ c for an invertible n×n matrix M over F₂, vectors
a, b and a bit c (the OEIS comment). So a(n) is the number of orbits of the
group G of these maps, the affine group AG(n,2) together with the addition of
affine functions, on the 2^(2ⁿ) functions.

### Python 3 — 193 bytes

```python
N=1
while 1:
 N*=2;s={-1}
 for f in range(a:=2**N):
  a-=f in s;q=[f]
  for g in q:
   if{g}-s:s|={g};q+=g^2**N//3,*(sum((g>>(x**j%2^x%2*N+x>>1)&1)<<x for x in range(N))for j in(0,1))
 print(a)
```

**How it works**

- **Functions as masks.** N = 2ⁿ (`N*=2` steps n), and a function is the
  N-bit integer whose bit x is f(x).
- **One search per orbit.** f runs over all 2^N masks in increasing order.
  The search from f applies three maps to every new mask g (the set `s` holds
  the masks already reached; it starts as {−1}, which is no mask) and so
  marks the whole orbit of f. `a` starts at 2^N and loses 1 for every f that
  was already reached, so it ends as the number of searches: one per orbit,
  started at its smallest member.
- **The three maps.**
  - `g^2**N//3`: 2^N//3 = 0101…01₂ is the mask of the even points, the
    affine function K = 1 ⊕ x₀, so this adds K (b = e₀, c = 1).
  - `sum((g>>P(x)&1)<<x for x in range(N))` is g∘P, with
    P(x) = `x**j%2^x%2*N+x>>1`. Here `x%2*N+x>>1` is R(x), the coordinates
    of x rotated by one place (bit 0 moves to bit n−1), and `x**j%2` is 1
    for j = 0 and x₀ for j = 1. So the two maps are g∘T and g∘B with
    T(x) = R(x) ⊕ e₀ and B(x) = R(x) ⊕ x₀·e₀, both of the form Mx ⊕ a.
- **They generate G** (n ≥ 2).
  - B∘R⁻¹ is the transvection y ↦ y ⊕ y_{n−1}·e₀. Its conjugates by powers
    of R add coordinate i−1 to coordinate i (indices mod n), and commutators
    of these give every elementary transvection, which generate
    GL(n,2) = SL(n,2). So the linear parts of T and B generate GL(n,2).
  - Tⁿ(x) = x ⊕ (e₀ ⊕ e_{n−1} ⊕ … ⊕ e₁) = x ⊕ 11…1₂ is a translation;
    GL(n,2) moves 11…1₂ to every nonzero vector, so every translation is
    generated, and the maps g ↦ g∘P generate all of AG(n,2).
  - Conjugating "add K" by g ↦ g∘σ gives "add K∘σ". As σ runs over
    AG(n,2), K∘σ runs over every non-constant affine function, and these
    span all affine functions b·x ⊕ c. So the three maps generate G.
  - Each map is a permutation of the masks, of finite order, so going
    forward from f reaches exactly the orbit of f.
- **n = 1.** R is the identity and B(x) = x ⊕ x = 0 is not a bijection. But
  every function of one variable is affine, so a(1) = 1, and the search from
  f = 0 reaches 1 (adding K), then 2 (g∘T) and 3 (g∘B): all four masks, so
  the program prints 1.

**Notes**

- Burnside's lemma gives the same numbers: g ↦ g∘σ ⊕ ℓ fixes 2^c(σ)
  functions when ℓ sums to 0 on every cycle of σ and none otherwise, so
  a(n) = (1/|AG(n,2)|)·Σ_σ 2^(c(σ)−r(σ)), where r(σ) is the rank of the
  vectors (⊕ of the points of a cycle, parity of its length). A program
  summing this over the 2^(n²+n) affine maps, with the loop of
  [A000214](../../A000xxx/A000214/) and a doubling multiset for the rank,
  was 237 bytes and took over 30 s for a(4); a version with a span set was
  242.
- Folding the addition of K into one of the point maps (g∘T ⊕ K, two maps
  instead of three) is 3 bytes shorter but prints 5 for n = 2: those two
  maps generate a smaller group.
- a(1)–a(4) take about a second here. a(5) would need all 2^32 masks of
  five variables (and a set of that size), so the bar is the first 4 terms
  in 60 s. After the bar the search for n = 5 keeps growing `s` and `q`:
  about 400 MB after two and a half minutes here. The b-file has 10 terms (a(7) from
  Hou, 1995; a(8)–a(10) from Zeng and Yang, 2019).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 193 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001289), CC BY-SA 4.0.
