# A000769

> No-3-in-line problem: number of inequivalent ways of placing 2n points on an n X n grid so that no 3 are in a line.
> — [OEIS A000769](https://oeis.org/A000769)

Offset 1: 0, 1, 1, 4, 5, 11, 22, 57, 51, 156, 158, 566, 499, 1366, 3978, 5900, 7094, 19204, 32577, 118057, …

### Python 3 — 256 bytes

```python
f=lambda P,r=0:r==n!=(Q:=P)and sum({*(Q:=[[(y,x),(n+~x,y)][i%2]for x,y in Q])}=={*P}for i in b'01'*4)or sum(f(P+[(r,a),(r,b)],r+1)for a in range(n)for b in range(a)if len({(c,(y-c<<n)//(r-x))for c in(a,b)for x,y in P})==4*r)
n=1
while[print(f([])//8)]:n+=1
```

**How it works**

- **The search** is the one of [A000755](../A000755/): two points per row,
  rows filled in order, and a new point w is allowed when the slopes from w
  to the earlier points are distinct, each slope (y−c)/(r−x) compared
  exactly as the floor `(y-c<<n)//(r-x)` (2ⁿ ≥ (n−1)² separates any two
  different slopes with denominators below n).
- **Burnside's lemma.** The number of classes under the dihedral group D4 of
  the square is (1/8)·Σ over solutions P of the number of symmetries g with
  g(P) = P, so each completed grid adds its stabilizer size and the total is
  divided by 8.
- **All 8 symmetries from two reflections.** Q starts at P and is replaced
  alternately by its transpose (x, y) → (y, x) and its mirror
  (x, y) → (n−1−x, y); the product of the two is a quarter turn, so the 8
  partial products are the 4 rotations and the 4 reflections, and the
  eighth brings Q back to P. Iterating over the bytes `b'01'*4` gives the
  parities 0, 1, 0, 1, … in a byte less than `range(8)`.
- `r==n!=(Q:=P)and …` sets Q only at a leaf: the chain stops at `r==n` on
  inner nodes, and n != a list is always True. The stabilizer is at least 1,
  so `and … or` never falls through to the search at a leaf.

**Speed**

As for A000755: a(7) after about 6 s here, a(8) after about two minutes. The
bar is the first 7 terms within 60 s.

**Notes**

- Keeping the 8 maps explicit, `((x^p)%n,(y^q)%n)[::s]` over p, q in
  (0, −1) and s in (1, −1), is 12 bytes longer; counting minimal
  representatives (`min(sorted(…))`) is longer still.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 256 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000769), CC BY-SA 4.0.
