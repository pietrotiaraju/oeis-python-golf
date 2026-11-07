# A000908

> Atom-rooted polyenoids with n edges with symmetry class C_s.
> — [OEIS A000908](https://oeis.org/A000908)

Offset 0: 0, 0, 1, 4, 14, 47, 164, 565, 1982, 6977, 24850, 89082, 321855, 1169853, 4276923, 15713799, 57998270, 214934984, 799473752, 2983682702, …

A polyenoid is a tree drawn on the honeycomb lattice, standing for a
polyene CₙHₙ₊₂ (Cyvin, Brunvoll, Brendsdal, Cyvin and Lloyd, J. Chem. Inf.
Comput. Sci. 35 (1995) 743–751; see [A000942](../A000942/)); here, as in
the algebraic part of that paper, the drawing may overlap itself. An
atom-rooted one has a marked carbon, and n counts its bonds, so it has
n + 1 carbons. Symmetry class C_s means that no symmetry of the drawing
other than the identity keeps the root in place. These are the C_s column
of Table 3 of the paper.

### Python 3 — 117 bytes

```python
L=[1,1,2];m=1
while[print((L[m+1]-L[m]-3*L[m//2]-m%3%2*(L[m//3]-~m%2*3*L[m//6])+3)//6)]:L+=L[-1]*(4*m+6)//(m+3),;m+=1
```

**How it works**

- Seen from the root, a polyenoid is three branches in cyclic order. A
  branch is either a hydrogen or a carbon carrying a left and a right
  branch, so the branches with k carbons are counted by the Catalan number
  c(k), with generating function U(x) = 1 + xU(x)². The mirror-symmetric
  branches are a hydrogen or a carbon whose right branch is the mirror of
  its left one: V(x) = 1 + xU(x²).
- The symmetries that keep the root form the dihedral group of order 6
  acting on the three branches. The orbits with trivial stabilizer come
  from Möbius inversion over its subgroups (the fixed points of the
  identity, minus those of the three mirrors and of the rotation group,
  plus three times those of the whole group, all over 6):
  a(n) = [xⁿ] (U³ − 3U(x²)V(x) − U(x³) + 3V(x³))/6, the generating
  function in the OEIS entry.
- The coefficients are Catalan numbers: [xⁿ]U³ = c(n+2) − c(n+1) (since
  U³ = (U² − U)/x), [xⁿ]U(x²)V(x) = c(⌈n/2⌉) (the odd part is the Catalan
  convolution), [xⁿ]U(x³) = c(n/3) when 3 | n, and [xⁿ]V(x³) = c((n−3)/6)
  when n ≡ 3 (mod 6), plus 1 at n = 0. With m = n + 1:
  6a(n) = c(m+1) − c(m) − 3c(⌊m/2⌋) − [m ≡ 1 (mod 3)]·(c(⌊m/3⌋) −
  3[m even]·c(⌊m/6⌋)) + 3[n = 0].
- `m%3%2` is 1 exactly when m ≡ 1 (mod 3), and `~m%2` is 1 when m is even.
  The bracket is a multiple of 6 for n ≥ 1 and −3 at n = 0, so `+3)//6`
  is right in both cases and saves the n = 0 term.
- `L` holds c(0)…c(m+1) and gains c(m+2) = c(m+1)(4m+6)/(m+3) each round.

**Notes**

- Checked by brute force over triples of branches (all of them up to
  8 bonds, orbits counted directly) and against the 27 OEIS terms.
- Exact integer arithmetic; the program is instant, and the b-file holds
  the 27 OEIS terms, which is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000908), CC BY-SA 4.0.
