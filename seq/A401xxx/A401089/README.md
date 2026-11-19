# A401089

> Number of regular pentagons bounded by the sides and diagonals of a regular
> 5n-gon.
> — [OEIS A401089](https://oeis.org/A401089) (draft when added)

Offset 1: 2, 16, 15, 64, 40, 294, 77, 256, 126, 400, 187, 1116, 260, 784, 345, 1024, 442, 1746, …

### Python 3 — 438 bytes

```python
import math
n=0
while n:=n+1:
 m=5*n;N=2*m;B=2*N;M=(B**N-1)//math.lcm(*[B**d-1for d in range(1,N)if N%d<1]);Z=[(B**e+B**(N-e))%M for e in range(m)];f=1+Z[2*n];S=0
 for r in 1,2:E=range(r,m,2);D={Z[e]:e for e in E};S+=sum(all(abs(u-v)<=2*n<=u+v<=8*n for u,v in zip((a,b,c,d,g),(b,c,d,g,a)))for a in E for b in E for c in E if(d:=D.get(x:=(f*(Z[c]-Z[b])+Z[a])%M))and(g:=D.get((f*(x-Z[c])+Z[b])%M))and((f-1)*Z[b]-Z[a]-Z[c])%M)
 print(n*S//2)
```

**How it works**

- Put the 5n-gon (m = 5n vertices) on the unit circle with vertex i at
  ζ^(2i), where ζ = e^(iπ/m) is a primitive 10n-th root of unity. The chord
  through vertices i and j has unit normal ζ^(i+j) and lies at distance
  cos(π(j−i)/m) from the centre along it. So the chords with normal direction
  ζ^t are the lines at offsets cos(πe/m) for 0 < e < m with e ≡ t (mod 2),
  one line for each such e (taking i and j mod m, and t mod 2m with the sign
  of the offset flipping when t moves by m). Sides of the polygon are the
  chords with e = 1 or m − 1.
- A regular pentagon with centre c and inradius r, whose outward edge
  normals point along t, t+2n, t+4n, t+6n, t+8n (72° apart), has its edges
  on the lines at offsets h_k = r + Re(c·ζ^(−t−2nk)). As a 5-periodic
  sequence, h has only the frequencies 0 and ±1, which is the same as the
  recurrence h(k+3) = φ·(h(k+2) − h(k+1)) + h(k), with characteristic
  polynomial (x − 1)(x² − (ω + ω̄)x + 1), ω = ζ^(2n), and φ = 1 + ω + ω̄
  the golden ratio. Every solution of the recurrence is 5-periodic, so any
  three offsets e₀, e₁, e₂ give exactly one candidate, and the program asks
  whether the forced h₃ and h₄ are chord offsets of the same parity. The
  inradius r vanishes (five lines through one point, no pentagon) exactly
  when h₂ = (φ − 1)·h₁ − h₀; those are thrown away.
- t enters only through its parity (`r`): turning the polygon by one vertex
  adds 2 to t and changes nothing else, so each of the n values of t of a
  parity class gives the same count, hence the factor n. With r ≠ 0 the same
  five lines also appear with inward normals (t + n, r < 0), so every
  pentagon is counted twice, hence the `//2`.
- Each edge must lie on a side or a diagonal, not only on its line: vertex k
  is where the lines of chords k and k+1 meet, and the edges lie on the
  chords exactly when every such meeting point is in the polygon, that is,
  when the two chords meet (cross or share an end). In units of half a
  vertex step, chord k covers the arc of half-width u = e_k around t and
  chord k+1 the arc of half-width v = e_(k+1) around t + 2n, on a circle of
  length 10n. They meet when one end of chord k+1 is on the closed arc of
  chord k and the other is not strictly inside it, that is,
  |2n − v| ≤ u ≤ min(2n + v, 8n − v), which rearranges to the chain
  `abs(u-v)<=2*n<=u+v<=8*n`.

**Exact arithmetic**

- Every offset is 2cos(πe/m) = ζ^e + ζ^(−e) (the factor 2 cancels in the
  linear tests), and φ = 1 + ζ^(2n) + ζ^(−2n), so each test asks whether a
  sum of at most 16 signed powers of ζ is zero. The program computes in
  Z/M with ζ ↦ B = 20n and M = Φ_{10n}(B), the cyclotomic polynomial at B,
  in which `Z[e]` is the image of ζ^e + ζ^(−e).
- M is (B^N − 1)/lcm(B^d − 1 : d | N, d < N) with N = 10n. B is divisible
  by every prime factor of N, so no such prime divides any B^d − 1. A prime
  dividing Φ_a(B) and Φ_b(B) for divisors a ≠ b of N would have to divide
  N, so the Φ_d(B) are pairwise coprime and the lcm is the product of
  Φ_d(B) over d | N, d < N.
- No false zeros: the kernel of Z[ζ] → Z/M is the ideal (M, ζ − B), whose
  norm is M ≥ (B − 1)^φ(N) > 16^φ(N). A nonzero sum α of at most 16 roots of
  unity has 1 ≤ |Norm(α)| ≤ 16^φ(N), so it cannot lie in that ideal. The
  same argument shows that different e give different residues, so the
  dictionary `D` (residue → e) loses nothing. Python integers do the rest
  exactly.

**Notes**

- The work is about 31n³ dictionary lookups for each n. The 30th term
  arrives after about 15 reference seconds and 38 terms fit in the 60 s
  limit, so the bar is 30 terms.
- The draft's own program does the same search in floating point with
  numpy, with tolerance 1e-9. This program gives the draft's 40 terms
  exactly, with no tolerance.
- The b-file holds the draft's 40 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 438 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A401089), CC BY-SA 4.0.
