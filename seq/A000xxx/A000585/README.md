# A000585

> Number of equivalence classes of Boolean functions of n variables under GL(n,2).
> — [OEIS A000585](https://oeis.org/A000585)

Offset 1: 4, 8, 20, 92, 2744, 950998216, 2076795963681989019155896, 21651217007530946175606768762255421159692845640522169779616, …

Two Boolean functions f, g: F₂ⁿ → F₂ are equivalent when g(x) = f(Mx) for
some invertible n×n matrix M over F₂; a(n) counts the classes.

### Python 3 — 193 bytes

```python
n=1
while 1:
 N=1<<n;t=k=0
 for z in range(N**n):
  for _ in[P:=[0]]*n:P+=[x^z%N for x in P];z>>=n
  r=len({*P})>>n;k+=r
  for x in P:
   while~x:P[x],x=-1,P[x];r<<=x<0
  t+=r
 print(t//k);n+=1
```

**How it works**

- **Burnside's lemma.** a(n) = (1/|G|) Σ_{M∈G} fix(M) with G = GL(n, 2). A
  function f is fixed by M (f(Mx) = f(x) for all x) exactly when it is
  constant on every cycle of the permutation x ↦ Mx of the N = 2ⁿ vectors,
  so fix(M) = 2^c(M), where c(M) counts those cycles (the zero vector is
  always a cycle of its own).
- **All matrices.** `z` runs over the Nⁿ integers below `N**n`; its n
  base-N digits are the columns of M. `for _ in[P:=[0]]*n:` resets `P` to
  [0] and runs n times; each pass appends `x^z%N` (the old images XORed with
  the next column, `%` binding tighter than `^`) and drops that column with
  `z>>=n`. After pass j, `P[v]` = Mv for every v < 2^j, so at the end `P` is
  the whole map v ↦ Mv.
- **Invertibility.** M is invertible exactly when the N images are distinct.
  `len({*P})>>n` is 1 then and 0 otherwise (the set has at most N elements),
  so `r` starts at 1 for M ∈ G and at 0 for a singular M, and `k+=r` counts
  |G| on the way.
- **Counting cycles.** `for x in P:` reads the list while it is being
  overwritten. A step `P[x],x=-1,P[x]` marks the entry at x with −1 and moves
  to the image of x. After going once round a cycle the walk is back at its
  first point, whose entry is now −1, so the next step sets x = −1: that is
  the only step with `x<0`, so `r<<=x<0` doubles r once per cycle, and `~x`
  (zero only for −1) ends the walk. Entries of finished cycles read −1 and
  start nothing. For an invertible M, r ends as 2^c(M); a singular M keeps
  r = 0, and its walks still end, since every step marks an entry.
- `t//k` is the Burnside average, an exact division.

**Notes**

- Other versions that print the same terms: adding r one matrix late with
  `t+=r;` in front of the `r=…` line (the [A000214](../A000214/) trick) drops
  the `t+=r` line but needs `t=k=r=0` and `x^~z%N` (so that the last matrix,
  whose contribution is lost, is the zero matrix): 194 bytes. The first
  version of this page, with an explicit invertibility test and a separate
  cycle counter, was 258 bytes.
- Exact integer arithmetic; correctness rests only on Burnside's lemma.
- The program tries all 2^(n²) matrices: a(1)–a(4) print in about 1.5 s here,
  and a(5) needs 2²⁵ matrices, an estimated 20 minutes at that rate.
  The b-file has 8 terms (up to a(8)); the bar is 4 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 258 | first entry |
| 2026-11-07 | Python 3 | 193 | XOR doubling into a walrus loop, `len(set)>>n` as the invertibility flag, destructive cycle walk |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000585), CC BY-SA 4.0.
