# A401762

> Number of distinct traces of length n of Wolfram's 2-state 3-symbol Turing
> machine, i.e., sequences of n (state, symbol read) pairs produced from an
> arbitrary tape and starting state.
> — [OEIS A401762](https://oeis.org/A401762) (draft when added)

Offset 1: 6, 18, 40, 90, 184, 376, 752, 1494, 2942, 5788, 11338, 22220, …

### Python 3 — 144 bytes

```python
f=lambda n,Q=0,t={},p=0,U=b';<<E2@':n<1or sum(f(n-1,c&1,t|{p:U[c&6:][:2]},p+c%5-2)for c in t.get(p,U)[Q::2])
n=1
while 1:print(f(n)+f(n,1));n+=1
```

**How it works**

- The machine is A0→1RB, A1→2LA, A2→1LA, B0→2LA, B1→2RB, B2→0RA. A trace is
  fixed by the starting state and by the symbols met on fresh cells, so a(n)
  is the number of leaves at depth n of the tree of runs in which a fresh cell
  may hold 0, 1 or 2. `f(n)` starts in state A (Q = 0), `f(n,1)` in state B.
- Each transition is one byte c: `c&1` is the new state, `c&6` is twice the
  symbol written and `c%5-2` is the move, ±2 (the head stays on even
  positions, which changes nothing).
- The six bytes are interleaved: `U[2*s+q]` is the transition for state q
  reading s, so `U[Q::2]` is the row of state Q, the three transitions a fresh
  cell allows. A written cell stores the pair `U[2*w:2*w+2]`, the transitions
  of A and of B reading w, and the same `[Q::2]` picks the one that applies.
  `t.get(p,U)[Q::2]` therefore reads fresh and written cells alike.
- `t|{p:…}` is a new dict with the cell written, so no branch has to undo
  anything.

**Notes**

- The tree is rebuilt for every n and has about 3.8·2ⁿ leaves (the entropy of
  the trace shift is log 2), so each term takes about twice as long as the one
  before: 20 terms in 30 s and 21 in 60 s on a desktop PC. The bar is 18 terms
  in 60 s. Memory stays at a few MB.
- Keeping each level's runs in a list instead of recounting is 128 bytes
  (`while L:=[…for Q,t,p in L for c in t.get(p,U)[Q::2]]:print(len(L))`), but
  every run carries its own copy of the tape: it passes 3 GB at n = 19 and
  about 12 GB at n = 21, inside the 60 s run, so it is not used here.
- The b-file's first 32 terms are the draft's DATA; terms 33 to 47 come from a
  separate crossing-sequence count that agrees with brute force for n ≤ 22.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 144 | first entry |
