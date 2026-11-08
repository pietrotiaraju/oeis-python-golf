# A001004

> Number of nonequivalent dissections of an (n+2)-gon by nonintersecting diagonals up to rotation and reflection.
> — [OEIS A001004](https://oeis.org/A001004)

Offset 0: 1, 1, 2, 3, 9, 20, 75, 262, 1117, 4783, 21971, 102249, 489077, …

### Python 3 — 168 bytes

```python
import math
t=[4];E=[-1,N:=1]
while 1:N+=1;E+=(e:=6*E[-1]-E[-2]-t[-1]),;t+=(3*e-E[-2])//N,;print((sum(4*E[math.gcd(k,N)]+t[N-k%2>>1]for k in range(N))+t[-2]-4*e)//8//N)
```

**Why the formula**

Burnside's lemma over the dihedral group of the N-gon, N = n + 2. Write
s(m) for the little Schröder numbers (A001003: dissections of an
(m+2)-gon) and D(m) for the central Delannoy numbers (A001850: 1, 3, 13,
63, …). W(x) = Σ_(L≥1) s(L−1)xᴸ counts the "caps" cut off by a chord
spanning L edges (W = x + W²/(1−W)).

- **Identity:** all s(N−2) dissections.
- **Rotation by k ≠ 0**, g = gcd(k, N): if its order is at least 3 the
  centre must lie inside a cell (a diagonal through the centre would cross
  its own images), and that cell is invariant: its vertices form an
  r-subset of a g-cycle, and each gap of L edges is closed by a cap,
  copied around. Summing over subsets gives g·[x^g] log 1/(1−W). For order
  2 the cell needs r ≥ 2, and the missing r = 1 term, g·s(g−1), is exactly
  the other case: a diameter (g choices) with one half dissected freely. So
  every rotation fixes g·[x^g] log 1/(1−W) dissections, and since
  W′/(1−W) = 1/√(1−6x+x²) this is **D(g−1)**.
- **Reflections:** chords crossing the axis must be perpendicular to it.
  They cut the polygon into pieces in each of which the axis runs through
  one symmetric cell, whose sides on one side of the axis are caps; with H
  boundary edges on one side the count is [y^H] W/(1−2W) = [y^(H+1)] W
  = **s(H)**, using y = W(1−2W)/(1−W). Axes through two vertices have
  H = N/2, through two edge midpoints N/2 − 1, through a vertex and a
  midpoint (N odd) (N−1)/2: for the N reflections, H = ⌊(N − k mod 2)/2⌋,
  k = 0..N−1.

**2N·a(n) = s(N−2) + Σ_(k=1..N−1) D(gcd(k,N) − 1) + Σ_(k=0..N−1) s(⌊(N − k mod 2)/2⌋)**,
which matches all 201 terms of the b-file.

**How it works**

- Two lists: `E[j]` = D(j−1) (so `E[gcd]` needs no −1, and E[0] = −1 is a
  virtual D(−1)) and `t[j]` = 4s(j).
- From (1−6x+x²)F′ = (3−x)F for F = Σ D(m)xᵐ, and R′ = (x−3)F for
  R = √(1−6x+x²) = 1 + x − 4xσ (σ = Σ s(m)xᵐ), one gets
  3D(m) − D(m−1) = 4(m+1)s(m) and mD(m) = (6m−3)D(m−1) − (m−1)D(m−2);
  together

  D(m) = 6D(m−1) − D(m−2) − 4s(m−1),  4s(m) = (3D(m) − D(m−1))/(m+1),

  the two appends in each pass (`e` is the new D(N−1)). Keeping 4s
  instead of s drops a `4*` and a `//4` there and costs two `4*` in the
  print: 1 byte net.
- The program computes 8N·a(n) and divides by 8N. The sum runs over k in range(N) for
  both parts; k = 0 adds 4E[N] = `4*e` instead of the identity term, so
  it adds `t[-2]-4*e` (t[-2] = 4s(N−2)).
- `t[N-k%2>>1]` is 4s(⌊(N − k mod 2)/2⌋): `-` binds tighter than `>>`.

**Notes**

- Exact integer arithmetic; correct for every n by the Burnside count
  above.
- Thousands of terms in 10 s; the bar is the whole b-file (201 terms) in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 168 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001004), CC BY-SA 4.0.
