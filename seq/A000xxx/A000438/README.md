# A000438

> Number of 1-factorizations of complete graph K_{2n}.
> — [OEIS A000438](https://oeis.org/A000438)

Offset 1: 1, 1, 6, 6240, 1225566720, 252282619805368320, 98758655816833727741338583040, …

A 1-factorization splits the edges of K_{2n} into 2n − 1 perfect matchings;
a(n) counts the splittings, with the matchings unordered.

### Python 3 — 169 bytes

```python
f=lambda c,e=0,*E:e<1or sum(f(c|e<<k,*E)for k in range(m)if c&e<<k<1)
m=1
while[print(+f(int(('0'*m+'1')*m,2),*[1<<a*m|1<<b*m for b in range(m)for a in range(b)]))]:m+=2
```

**How it works**

- Put m = 2n − 1 and call the vertices 0, …, m − 1 and ∞. Each matching
  has exactly one edge at ∞; name it v when that edge is {v, ∞}. A
  factorization is then the same as a colouring of the edges with colours
  0, …, m − 1 in which {v, ∞} has colour v and the edges at each vertex
  have distinct colours.
- On the remaining K_m this says: give each edge {a, b} a colour that a
  and b do not hold yet, where vertex v starts out holding colour v. Each
  vertex has m − 1 edges in K_m and m − 1 colours other than its own, so
  a full colouring uses each of them once there, and each colour class
  with its ∞ edge is a perfect matching. So a(n) is the number of complete
  colourings, with no division by symmetries.
- c is an m·m-bit mask: bit v·m + k says that vertex v holds colour k.
  The 1s of `int(('0'*m+'1')*m,2)` sit at bits 0, m + 1, 2(m + 1), …,
  that is at v·m + v: the starting colours.
- Edge {a, b} is `1<<a*m|1<<b*m`, colour 0 at both ends, so `e<<k` is
  colour k at both ends. `c&e<<k<1` (shift before `&` before `<`) says
  that neither end holds k yet, and the recursion goes on with `c|e<<k`.
- f takes the edges as separate arguments: e is the next one and E the
  rest. When none is left, e keeps its default 0 and `e<1` returns True,
  one complete colouring, so `sum` counts them. For m = 1 (K₂, no edges)
  f returns True itself, and `+` prints it as 1.
- `while[print(…)]:m+=2` runs m = 1, 3, 5, … The edges are listed b by b
  with a < b; the order only affects the speed.

**Notes**

- Measured alternatives: the edges as a list argument,
  `f=lambda E,c:E==[]or …f(E[1:],c|x)…` with a walrus for the shifted
  edge, 177 bytes. The previous program (262 bytes) generated the perfect
  matchings and ran a cached exact cover over them.
- The search is complete, so the program is right for every n. It counts
  the colourings one at a time, though: a(5) = 1225566720 is out of reach
  at the few thousand per second seen for a(4).
- [A000474](../A000474/) also identifies factorizations under relabeling
  the vertices: K₆ has 6 factorizations in one class, K₈ has 6240 in six.
- The first four terms print in about 1 s here. The b-file has 7 terms
  (up to a(7)); the bar is the first 4 terms in 10 s.
- The 4300-digit int-to-str limit is far beyond any term that can be
  printed.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 311 | first entry |
| 2026-11-06 | Python 3 | 278 | cache the exact-cover lambda and inline the least-edge test |
| 2026-11-06 | Python 3 | 262 | express the lazy matching generator as a lambda |
| 2026-11-07 | Python 3 | 169 | colour K_{2n-1} with the star at the extra vertex fixed, edges as star-arguments |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000438), CC BY-SA 4.0.
