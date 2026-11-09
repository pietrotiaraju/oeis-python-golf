# A001183

> Number of nontrivial Baxter permutations of length 2n-1.
> — [OEIS A001183](https://oeis.org/A001183)

Offset 1: 0, 2, 2, 18, 66, 374, 1694, 9822, 51698, …

### Python 3 — 148 bytes

```python
f=lambda p,u,i=0:sum(f([v]+p,u-{v},i+1)for v in u-{i}if min((p[0]-x)*(v-x)for x in[p,u][i%2])>=v-i&1)+i//n
n=3
while[print(f([n],{*range(n)}))]:n+=2
```

**How it works**

- The definition is W. M. Boyce's (Math. Algorithms 2, 1967, scanned in
  [A001181](https://oeis.org/A001181)): for odd N, a permutation P of
  {1, …, N} is a Baxter permutation of order N when
  (1) P maps odd numbers to odd ones and even to even;
  (2) if P(n) lies strictly between P(2i) and P(2i+1), then n > 2i+1;
  (3) if P(n) lies strictly between P(2i−1) and P(2i), then n < 2i−1.
  They come from commuting maps f, g of [0, 1]: f permutes the points where
  f∘g crosses the diagonal. A fixed point of P is a common fixed point of f
  and g, so Boyce calls those permutations trivial; nontrivial means
  fixed-point free.
- Indexing: the terms are Boyce's counts for N = 3, 5, …, 19, so a(n)
  counts order N = 2n+1, not the 2n−1 of the title (order 3 has only 123
  and 321, both with a fixed point, so it cannot be a(2) = 2). The program
  follows the data. The 1967 table printed 22 for N = 9; the OEIS has 18,
  which is what the definition gives.
- The search fills positions left to right, numbered from 0, with values
  0 … N−1 (shifting both by one keeps the parities). Conditions (2) and (3)
  only look at adjacent pairs, so each is checked when its second value v
  goes to position i after the value a = `p[0]`:
  for even i (a pair [2k, 2k+1] counted from 1) every value strictly
  between a and v must come later, so no *used* value may lie between;
  for odd i (a pair [2k−1, 2k]) they must all come earlier, so no *unused*
  value may lie between.
- x lies strictly between a and v exactly when (a−x)(v−x) < 0, so the test
  is `min((p[0]-x)*(v-x)for x in[p,u][i%2])`, the used list `p` or the
  unused set `u`, compared with 0. The minimum is never positive, since `p`
  holds a and `u` holds v; so `>=v-i&1` also enforces (1): it asks for ≥ 0
  when v and i have the same parity and for the impossible ≥ 1 otherwise.
  `u-{i}` leaves out fixed points.
- `p` keeps the used values newest first, after the sentinel N: at i = 0
  the check over `[N]` gives 0, and N never lies between two values, so it
  never blocks later.
- `i//n` is 1 exactly when all N positions are filled (i = N = n), so `f`
  counts the complete permutations below a prefix.

**Notes**

- Exact integers; the program is the definition, checked pair by pair as
  the permutation grows. Without the `u-{i}` filter the same search counts
  every Baxter permutation of order N and gives 2, 6, 22, 92, … (A001181),
  Boyce's first column.
- The parity test is only a speed-up: (2) and (3) already force (1) when N
  is odd, and `>-1` in place of `>=v-i&1` (144 bytes) prints the same
  terms, but it then explores the wrong-parity prefixes and a(9) takes 96 s
  instead of 6 s here.
- All 9 terms take about 6 s here; the next one, a(10) = 306164 (beyond the
  OEIS data), comes after about 37 s.
- The b-file is the OEIS entry's 9 terms; the bar is all of them in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 148 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001183), CC BY-SA 4.0.
