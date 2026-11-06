# A000388

> Number of permutations of an n-sequence discordant with three given permutations (see reference) in n-2 places.
> — [OEIS A000388](https://oeis.org/A000388)

Offset 4: 6, 20, 180, 1106, 9292, 82980, 831545, 9139482, 109595496, …

### Python 3 — 116 bytes

```python
f=lambda c:c<{0}or sum(f(c-{j})*B**((j+len(c))%n<3)for j in c)
n=3
while n:=n+1:B=n**n;print(f({*range(n)})//B**2%B)
```

**How it works**

- As in [A000183](../A000183/) and [A000380](../A000380/), the three
  given permutations are the identity, the n-cycle s and s², so a
  position i is a hit when p(i) − i ∈ {0, 1, 2} (mod n). a(n) counts the
  permutations of Z_n with exactly 2 hits, that is, discordant in n − 2
  places. A brute-force count over all permutations agrees for n ≤ 9.
- `f` fills the rows one at a time with the set `c` of free columns: the
  row is r = len(c), and column j is a hit when (j + r) mod n < 3 (r ↦ −r
  is a bijection of Z_n, so the count is the same). Every placement is
  weighted by B per hit, so f returns Σ_p B^(hits of p).
- Each digit of that sum in base B = nⁿ counts permutations, so it is at
  most n! < nⁿ and the digits never carry: `//B**2%B` reads the number
  of permutations with exactly 2 hits. `c<{0}` is true only for the
  empty set, and a full placement returns `True`, which counts as 1.

**Notes**

- Exhaustive search over all n! permutations, correct for every n. On
  the machine that set the bar a(4) … a(10) come out in 60 s, and a(11)
  would need about 11 times as long as a(10). The bar is 5 terms in
  60 s. The b-file is synthesized from the 20 terms of the entry
  (n = 4 to 23).
- The same alternatives as for A000380 apply: a hit budget with pruning
  is 120 bytes and not much faster (about 40% of all permutations have at
  most 2 hits), and the rook-polynomial transfer matrix is fast but
  much longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000388), CC BY-SA 4.0.
