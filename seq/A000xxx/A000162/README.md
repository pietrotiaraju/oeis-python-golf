# A000162

> Number of 3-dimensional polyominoes (or polycubes) with n cells.
> — [OEIS A000162](https://oeis.org/A000162)

Offset 1: 1, 1, 2, 8, 29, 166, 1023, 6922, 48311, 346543, …

### Python 3 — 273 bytes

```python
F=lambda o:(t:=o|{r for q in o for r in zip(*[((y,z,x),(-y,x,z))for x,y,z in q])})>o and F(t)or o
s={((0,)*3,)}
while[print(len(s))]:s={(*min(sorted((x-a,y-b,z-c)for x,y,z in r)for r in F({q+(u,)})for a,b,c in[min(r)]),)for q in F(s)for x,y,z in q if(u:=(x+1,y,z))not in q}
```

**How it works**

- `s` holds one canonical form per polycube with n cells, counted up to
  rotations only (mirror images are different).
- `F` closes a set of shapes under the rotation group: it adds the images
  of every shape under (x,y,z) → (y,z,x) and (x,y,z) → (−y,x,z), which
  generate all 24 rotations, until nothing new appears (`t>o` is a proper
  superset test). The `zip(*[…])` turns the list of cell pairs into the two
  rotated shapes. Shapes are ordered tuples rotated about the origin, so
  the orbit is finite without normalizing on the way.
- Growth: `F(s)` is every orientation of every polycube in `s`, and a new
  cell is only ever attached on the +x side of a cell. That is enough: in
  any polycube with n+1 cells some cell can be removed leaving a connected
  polycube, and rotating that cell's attachment direction to +x puts the
  rest in one of the orientations of `F(s)`.
- Canonical form: for each of the 24 orientations r of a candidate,
  subtract its lexicographically smallest cell and sort; the smallest of
  these 24 sorted lists names the polycube. `(*…,)` turns it into a tuple
  three bytes under `tuple(…)`.
- `((0,)*3,)` is the one-cell start, a byte under `((0,0,0),)`.

**Notes**

- Exhaustive enumeration, correct for every n. Growing from every
  orientation makes about 24·n candidates per polycube, each with its own
  orbit, so time and memory grow about seven-fold per term: on the machine
  that set the bar, a(1)…a(8) take about 39 s and a(9) is out of reach in
  60 s (and would need about 24 × 48311 stored orientations). Attaching
  cells in all six directions to the canonical forms only is four times
  faster but about 30 bytes longer. The bar is 7 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 273 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000162), CC BY-SA 4.0.
