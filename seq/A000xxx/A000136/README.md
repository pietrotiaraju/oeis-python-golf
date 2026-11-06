# A000136

> Number of ways of folding a strip of n labeled stamps.
> — [OEIS A000136](https://oeis.org/A000136)

Offset 1: 1, 2, 6, 16, 50, 144, 462, 1392, 4536, 14060, 46310, 146376, …

### Python 3 — 145 bytes

```python
L=[[0]],
while[print(len(L))]:L=[(x+[-len(q)],*q)for q in L for x in([],*q)if all((x<c)^(x<d)==(q[0]<c)^(q[0]<d)for c,d in zip(q[1::2],q[2::2]))]
```

**How it works**

- Fold the strip flat and note the height of each stamp in the pile.
  Crease i joins stamps i and i + 1, and the creases alternate between the
  two edges of the pile. An order of heights is a folding exactly when no two
  creases on the same edge interleave, where {a, b} and {c, d} interleave if
  exactly one of c, d lies between a and b (Koehler 1968 and Lunnon 1968,
  both in the OEIS references).
- `L` holds every folding of the current number of stamps. A folding of
  k + 1 stamps is a folding of k stamps with the new last stamp slid into one
  of the k + 1 gaps of the pile, and only the new crease can break the rule.
  So each step tries all k + 1 gaps and keeps the ones that pass;
  `print(len(L))` prints the count before each step.
- A folding is a tuple `q` of heights, newest stamp first: `q[0]` is the last
  stamp, `q[1]` the one before it, and so on. The creases on the same edge as
  the new crease (`q[0]`, new) are (`q[1]`, `q[2]`), (`q[3]`, `q[4]`), …,
  which is `zip(q[1::2],q[2::2])`.
- Heights are lists, compared lexicographically, so nothing is ever
  renumbered. `[]` is below every height, and `x+[-len(q)]` lies just above
  `x`. A height above `x` that does not start with `x` is also above
  `x+[-len(q)]`. A height that does start with `x` was made at an earlier
  step, when `len(q)` was smaller, so the number after `x` in it is larger
  (or it is the starting `[0]`). So `x` running over `[]` and the k heights
  in `q` gives each of the k + 1 gaps once.
- Nothing lies between `x` and the new height, so comparing a crease end `c`
  with the new height gives the same answer as `x<c`. The new crease and
  (`c`, `d`) interleave when an odd number of `x<c`, `x<d`, `q[0]<c`,
  `q[0]<d` hold, so a gap is kept when
  `(x<c)^(x<d)==(q[0]<c)^(q[0]<d)` for every crease on that edge.
- `L=[[0]],` is a one-element tuple: the single folding of one stamp, at
  height `[0]`.

**Notes**

- Every term needs a step over all foldings of the previous length, and
  a(n) grows about 3.5 times per step. The program prints 13 terms in about
  12 s and 14 in about 40 s, using about 0.7 GB by the end of a minute. The
  b-file has 45 terms.
- The bar is 10 terms in 60 s, which is what the straightforward program
  manages: trying all n! orders (175 bytes) prints 10 terms in about 41 s.

  ```python
  from itertools import*
  n=1
  while[print(sum(all((a-c)*(a-d)*(b-c)*(b-d)>-1for m in range(n)for a,b,c,d in zip(p,p[1:],p[m*2:],p[m*2+1:]))for p in permutations(range(n))))]:n+=1
  ```

- The same search depth-first, as a recursive `lambda` that needs almost no
  memory, came out at 159 bytes. Integer heights renumbered with
  `[v+(v>x)for v in q]` cost 153 bytes, and unpacking `for b,*p in L` to
  write `b` for `q[0]` ties at 145.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 145 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000136), CC BY-SA 4.0.
