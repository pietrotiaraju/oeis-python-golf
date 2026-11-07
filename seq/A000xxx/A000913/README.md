# A000913

> Number of bond-rooted polyenoids with n edges.
> — [OEIS A000913](https://oeis.org/A000913)

Offset 1: 0, 1, 2, 12, 38, 143, 490, 1768, 6268, 22610, 81620, 297160, 1086172, 3991995, 14731290, 54587280, 202992808, 757398510, 2834493948, 10637507400, …

A polyenoid is a tree drawn on the honeycomb lattice, standing for a
polyene (Cyvin, Brunvoll, Brendsdal, Cyvin and Lloyd, J. Chem. Inf.
Comput. Sci. 35 (1995) 743–751; see [A000942](../A000942/)); the drawing
may overlap itself. A bond-rooted one has a marked bond, and n counts its
bonds. Despite the title, the terms count only the bond-rooted polyenoids
of symmetry C_s, those where no symmetry but the identity keeps the root
bond in place: a(1) = 0 although ethylene rooted at its bond is one, and
the terms are the C_s column of Table 4 of the paper (the total column
starts 1, 1, 5, 12, 45). The program follows the data.

### Python 3 — 107 bytes

```python
L=[1,1,2,5];m=2
while[print((L[m+1]-2*L[m]-~m%2*(3*L[m//2]-m%4*L[m//4]))//4)]:L+=L[-1]*(4*m+6)//(m+3),;m+=1
```

**How it works**

- Each end of the root bond carries two branches, in order, and a branch
  is a hydrogen or a carbon carrying two branches, so branches with k
  carbons are counted by the Catalan number c(k) (generating function
  U(x) = 1 + xU(x)²). The bond itself is one of the n edges, so the four
  branches hold n − 1 carbons.
- The symmetries that keep the bond form a group of order 4: the half turn
  about its midpoint and the mirrors along and across it. Each of the
  three swaps the branches in pairs, so its fixed points have generating
  function U(x²)², and the whole group fixes U(x⁴). Möbius inversion
  (1, −1, −1, −1, +2 over 4) leaves the orbits with trivial stabilizer:
  a(n) = [xⁿ⁻¹] (U⁴ − 3U(x²)² + 2U(x⁴))/4, which is Emeric Deutsch's
  formula in the OEIS entry.
- In Catalan numbers, with m = n + 1: [xⁿ⁻¹]U⁴ = c(m+1) − 2c(m) (since
  U⁴ = ((U − 1)/x)²), [xⁿ⁻¹]U(x²)² = c(m/2) for even m, and
  [xⁿ⁻¹]U(x⁴) = c(⌊m/4⌋) for m ≡ 2 (mod 4). So
  4a(n) = c(m+1) − 2c(m) − [m even]·(3c(m/2) − 2[m ≡ 2 (mod 4)]·c(⌊m/4⌋)).
- `~m%2` is 1 for even m, and for even m, `m%4` is 0 or 2, which is
  exactly the coefficient 2[m ≡ 2 (mod 4)].
- `L` holds c(0)…c(m+1) and gains c(m+2) = c(m+1)(4m+6)/(m+3) each round.

**Notes**

- Checked by brute force over quadruples of branches (all of them up to
  8 bonds, orbits counted directly) and against the 25 OEIS terms.
- Exact integer arithmetic; the program is instant, and the b-file holds
  the 25 OEIS terms, which is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000913), CC BY-SA 4.0.
