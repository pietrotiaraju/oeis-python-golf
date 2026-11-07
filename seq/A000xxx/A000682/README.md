# A000682

> Semi-meanders: number of ways a semi-infinite directed curve can cross a straight line n times.
> — [OEIS A000682](https://oeis.org/A000682)

Offset 1: 1, 1, 2, 4, 10, 24, 66, 174, 504, 1406, 4210, 12198, …

### Python 3 — 140 bytes

```python
L=[[]],
while[print(len(L))]:L=[(x+[-len(q)],*q)for q in L for x in q if all((x<c)^(x<d)==(q[0]<c)^(q[0]<d)for c,d in zip(q[1::2],q[2::2]))]
```

**How it works**

- Semi-meanders of order n correspond to the foldings of a strip of n
  labeled stamps with leaf 1 on top, which is why
  [A000136](../A000136/)(n) = n·a(n) (OEIS entry; Legendre, *Foldings and
  meanders*, 2014). Turning the pile over, the same number of foldings have
  leaf 1 at the bottom, and those are what the program counts.
- It is the folding generator of [A000136](../A000136/) with the gap below
  the pile taken away: a new stamp goes just above one of the stamps already
  in the pile (`for x in q` instead of `for x in([],*q)`), so leaf 1, which
  starts the pile, stays at the bottom forever. Removing the last stamp of
  such a folding leaves one with a stamp fewer and leaf 1 still at the
  bottom, so every folding is built exactly once.
- A folding is a tuple of heights, newest stamp first. Heights are lists
  compared lexicographically and `x+[-len(q)]` lies just above `x` and below
  everything else above `x`; leaf 1 sits at height `[]`, below all of them.
- The new crease joins `q[0]` and the new stamp; the creases on its edge of
  the pile are `zip(q[1::2],q[2::2])`. Two creases on the same edge must not
  interleave, which is the test `(x<c)^(x<d)==(q[0]<c)^(q[0]<d)` (see
  A000136 for why `x` can stand for the new height).

**Notes**

- Correctness rests on the equivalence between semi-meanders and stamp
  foldings with leaf 1 on top (stated in the OEIS entry, together with
  a(n) = A000136(n)/n; see Legendre 2014) and on the non-interleaving
  criterion for foldings (Koehler 1968, Lunnon 1968).
- The list holds all a(n) foldings, about 3.3 times more per step: 13 terms
  take about a second and 15 about 10 s, but the 16th step needs more than
  300 MB. The b-file has 49 terms.
- The bar is 12 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 140 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000682), CC BY-SA 4.0.
