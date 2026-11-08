# A001010

> Number of symmetric foldings of a strip of n labeled stamps.
> — [OEIS A001010](https://oeis.org/A001010)

Offset 1: 1, 2, 2, 4, 6, 8, 18, 20, 56, 48, 178, 132, 574, 348, 1870, 1008, 6144, 2812, 20314, 8420, …

A folding is symmetric when it does not change if the pile is turned upside
down and the stamps are renumbered from the other end: the height h(j) of
stamp j satisfies h(j) + h(n+1−j) = n+1 (OEIS comment; Legendre, *Foldings
and meanders*, 2014, Definition 3.1).

### Python 3 — 185 bytes

```python
A=[()];B=[[0]]
while[print(len(B))]:A,B=B,[(a-~a,*[w*2for w in q],~a-a)for q in A for a in{0,*q,-len(A)}for p,*r in[(*q,-a)]if all((a<c)^(a<d)==(p<c)^(p<d)for c,d in zip(*[iter(r)]*2))]
```

**How it works**

- An order of heights is a folding exactly when no two creases on the same
  edge of the pile interleave; crease i joins stamps i and i + 1 and the
  creases alternate between the two edges (Koehler 1968, Lunnon 1968; see
  [A000136](../A000136/)).
- The program grows symmetric foldings from the middle out. Taking the end
  stamps off a symmetric folding of k + 2 stamps leaves a symmetric folding
  of the middle k, so each step adds a new first stamp and its mirror image
  as the new last stamp. `A` holds the symmetric foldings of k stamps and
  `B` those of k + 1: odd lengths grow from the single stamp `[0]`, even
  ones from the empty strip `()`, and `A,B=B,…` takes turns.
- A folding is a tuple of integer heights, stamp 1 first, centred on 0 so
  that the mirror of height h is −h: symmetry is q[i] = −q[−1−i].
- The new first stamp goes just above some height `a`; then all heights
  are doubled, the new stamp gets 2a + 1 (`a-~a`) and its mirror −2a − 1
  (`~a-a`). The choices of `a` are the heights in the pile, 0, and a
  height below everything: `{0,*q,-len(A)}`. Each gap of the pile, with
  the new stamp above or below the centre, is met exactly once. In an even
  pile 0 is not a height but the middle of the central gap, so the central
  gap gets both orders of the new pair (above −s₁ and above 0, with ±s₁ the
  heights next to the centre); in an odd pile 0 is the middle stamp.
- `-len(A)` is below every height: by induction every height is smaller
  than the number of foldings in its list in absolute value. Putting the
  new stamp right above or right below the old first stamp never breaks
  the rule (nothing lies between them, and for even k the two new creases
  then lie on one side of the centre), so a(k + 2) ≥ 2a(k), while heights
  at most double and the bottom choice gives 2·len(A) − 1.
- Only the new creases can break the rule, and the new last crease is the
  mirror image of the new first one, so checking the first is enough. Its
  edge partners are the creases (q[1], q[2]), (q[3], q[4]), …, which
  `zip(*[iter(r)]*2)` pairs up; for even k the list ends with the mirror
  crease (q[−1], new last stamp).
- The test runs on the old heights, before doubling: the new stamp sits at
  a + ½, so for an integer c, "new < c" is `a<c`; the mirror sits at
  −a − ½, and it is stored as `-a`, because p < −a − ½ is p < −a for an
  integer p, and a + ½ < −a − ½ is a < −a. A crease (c, d) does not
  interleave with (new, p) when `(a<c)^(a<d)==(p<c)^(p<d)`.

**Notes**

- Exact integers throughout; correctness rests on the folding criterion
  above. a(n) is 2·A007822 or 2·A000682 of about n/2 (OEIS formulas), but
  the program does not use them.
- The heights double every step and soon stop being small cached ints,
  so a tuple of n heights costs about 30n bytes more than one of small
  ints. The program prints 22 terms in about 3.5 s here, a(23) at about
  10 s with about 280 MB in use, and the next steps need more than that.
  So the bar is 17 terms in 5 s (the b-file has 52).
- Renumbering the heights to stay small, `w+(w>a)-(w<-a)` with
  `for y in(a+1,~a)` and `-y`, costs 205 bytes; it prints 24 terms in
  about 22 s but needs 300 MB by about 43 s. Filtering all foldings of
  [A000136](../A000136/) for symmetry has to build about 3.5ⁿ foldings
  instead of about 1.8ⁿ, so it is far slower.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 185 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001010), CC BY-SA 4.0.
