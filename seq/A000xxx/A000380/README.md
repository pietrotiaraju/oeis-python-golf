# A000380

> Number of permutations of an n-sequence discordant with three given permutations (see reference) in n-3 places.
> — [OEIS A000380](https://oeis.org/A000380)

Offset 3: 6, 8, 40, 176, 1421, 10352, 93114, 912920, 9929997, …

### Python 3 — 116 bytes

```python
f=lambda c:c<{0}or sum(f(c-{j})*B**((j+len(c))%n<3)for j in c)
n=2
while n:=n+1:B=n**n;print(f({*range(n)})//B**3%B)
```

**How it works**

- As in [A000183](../A000183/), the three given permutations are the
  identity, the n-cycle s and s², so a position i is a hit when
  p(i) − i ∈ {0, 1, 2} (mod n). a(n) counts the permutations of Z_n
  with exactly 3 hits, that is, discordant in n − 3 places (Margolius'
  formula in the entry is the same count by inclusion–exclusion over the
  rook numbers of this board). A brute-force count over all
  permutations agrees for n ≤ 9.
- `f` fills the rows one at a time with the set `c` of free columns, as
  in A000183: the row is r = len(c), and column j is a hit when
  (j + r) mod n < 3 (r ↦ −r is a bijection of Z_n, so the count is the
  same). Instead of discarding the hits, every placement is weighted by
  B per hit, so f returns Σ_p B^(hits of p).
- Each digit of that sum in base B = nⁿ counts permutations, so it is at
  most n! < nⁿ and the digits never carry: `//B**3%B` reads the number
  of permutations with exactly 3 hits. `c<{0}` is true only for the
  empty set, and a full placement returns `True`, which counts as 1.

**Notes**

- Exhaustive search over all n! permutations, correct for every n. On
  the machine that set the bar a(3) … a(10) come out in 60 s, and a(11)
  would need about 11 times as long as a(10). The bar is 6 terms in
  60 s. The b-file is synthesized from the 21 terms of the entry
  (n = 3 to 23).
- Pruning placements with more than 3 hits by a budget argument,
  `f=lambda c,h:h>-1and(c<{0}and h<1or sum(f(c-{j},h-((j+len(c))%n<3))for j in c))`,
  is 120 bytes and barely faster, since about two thirds of all
  permutations have at most 3 hits. Inclusion–exclusion over the rook
  polynomial (a 4-state transfer matrix, trace of Tⁿ) is fast but over
  190 bytes, and memoizing f over frozensets is about 156.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000380), CC BY-SA 4.0.
