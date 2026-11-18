# A401765

> Largest m such that an n X m rectangle can be tiled with Culik's 13 Wang
> tiles so that every column wraps around (its bottom edge matches its top
> edge).
> — [OEIS A401765](https://oeis.org/A401765)

Offset 1: 1, 5, 9, 5, 19, 9, 6, 17, 9, 19, 11, 9, 63, 9, 19, 17, 9, 69, …

### Python 3 — 312 bytes

```python
T="GGGRRRYBGGYBGgbbrrgyykkkkyrrggbbyyyykkkBGBGBGRGRYRGG"
h=lambda l,x,c,r="":[z for i in range(13)if c+l[0]in T[i::26]for z in h(l[1:],x or T[i],T[i+39],r+T[i+13])]if l else[r][x!=c:]
n=0
while 1:
 n+=1;S={('',)*n};m=-1
 while S:S={min(z[i:]+z[:i]for i in range(n))for l in S for z in h(l,'','')};m+=1
 print(m)
```

**How it works**

- `T` holds the 13 tiles column by column: tile i has top `T[i]`, right
  `T[i+13]`, left `T[i+26]` and bottom `T[i+39]`, in the order T1–T13 of the
  OEIS entry. Top and bottom colors are upper case (R, Y, G, B) and side
  colors lower case (r, g, b on T1–T6, y, k on T7–T13), so a top color never
  equals a side color.
- A column of height n is a cycle of n tiles: each bottom is the next top,
  and the last bottom is the first top. `h(l,x,c,r)` lays the column down
  row by row against the left edges `l` and returns the right edges `r` of
  every column that closes. `T[i::26]` is the pair top+left of tile i, so
  `c+l[0]in T[i::26]` asks for top `c` and left `l[0]`. An empty string
  stands for "any": on the first row there is no top yet, and on the first
  step there is no left edge yet. `x` keeps the first top, and the column
  closes when the last bottom `c` equals it.
- An n × m rectangle whose columns wrap is a path of m such columns, each
  one's right edges being the next one's left edges. `S` is the set of right
  edges that end a strip of k columns: the first step starts from the
  all-blank state `('',)*n` and so gets the right edges of every closed
  column, and each later step keeps only columns whose left edges are in
  `S`. a(n) is the last k with `S` not empty, which `m` counts.
- Moving every row of a strip down by one gives another strip, because the
  columns wrap. So a state and its rotations end strips of the same lengths,
  and `S` keeps each state as its least rotation, which makes it about n
  times smaller.
- `S` always empties: a column that could follow itself, after any number of
  steps, would tile the plane periodically, and Culik's tiles admit no
  periodic tiling (K. Culik II, An aperiodic set of 13 Wang tiles, Discrete
  Math. 160 (1996)). The search covers every closed column of every
  arrangement of rows, so the value is right for every n.

**Notes**

- The first step goes through all closed columns, about 3.96ⁿ of them
  (951,536 for n = 10, 3,769,328 for n = 11), so each term takes about four
  times as long as the one before: a(10) after 18 s on a desktop PC (12.5
  reference seconds) and a(11) after about a minute. The bar is 10 terms in
  60 s. The lists of the first step stay under 300 MB in that time.
- The OEIS program is much faster because it uses a lemma from the author's
  paper: the rows of a strip with 6 or more columns form a cyclic word in
  the blocks UL and ULL (U for rows of T1–T6, L for rows of T7–T13). This
  program does not use it.
- Keeping every open column in one set and extending it by a row per term is
  248 bytes and reaches a(10) in 7.4 reference seconds, but the set holds
  about 4ⁿ strings (50 million at n = 12) and passed 4 GB within the 60 s
  run, so it is not used here.
- `h` recurses n deep, well inside Python's default limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 312 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A401765), CC BY-SA 4.0.
