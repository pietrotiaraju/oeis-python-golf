# A002188

> Sprague-Grundy value for Grundy's game when starting with n tokens.
> — [OEIS A002188](https://oeis.org/A002188)

Offset 0: 0, 0, 0, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 3, 2, 1, 3, 2, 4, 3, …

### Python 3 — 95 bytes

```python
g=[]
while 1:print(x:=min({*range(len(g)+1)}-{*map(int.__xor__,g[1:],g[:len(g)//2:-1])}));g+=x,
```

**How it works**

- **The game.** A move splits one heap into two nonempty heaps of
  different sizes. By the Sprague–Grundy theorem
  G(n) = mex{G(i) ⊕ G(n − i) : 1 ≤ i < n − i}.
- **Only the unequal splits.** With `g` = G(0), …, G(n − 1),
  `g[:len(g)//2:-1]` is G(n − 1), G(n − 2), …, G(⌊n/2⌋ + 1), which has
  ⌊(n − 1)/2⌋ entries, so zipping it with `g[1:]` = G(1), G(2), … gives
  exactly the pairs (G(i), G(n − i)) for 1 ≤ i ≤ ⌊(n − 1)/2⌋, that is
  i < n − i; the equal split of an even heap is left out.
  `map(int.__xor__,…)` stops at the shorter list.
- **The mex.** Heap n has fewer than n options, so its mex is at most
  n and `min({*range(len(g)+1)}-S)` finds it. No bound is known to
  hold for all n (the values are not known to be periodic), so the
  range grows with n.

**Notes**

- About n²/4 XORs for the first n terms; the 20001 terms of the b-file
  (n = 0 to 20000) take about 25 s here (1.5–2.6 times slower than the
  reference). A two-line mex, `x=0` and `while x in s:x+=1`, is 3 bytes
  longer and 2.5 times faster. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002188), CC BY-SA 4.0.
