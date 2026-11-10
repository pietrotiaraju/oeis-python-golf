# A001441

> Number of inequivalent Costas arrays of order n under dihedral group.
> — [OEIS A001441](https://oeis.org/A001441)

Offset 1: 1, 1, 1, 2, 6, 17, 30, 60, 100, 277, 555, 990, 1616, 2168, 2467, 2648, 2294, 1892, 1283, 810, …

A Costas array of order n is an n × n permutation array (one dot per row
and column) whose dots have pairwise distinct displacement vectors. The
term counts them up to the eight symmetries of the square.

### Python 3 — 199 bytes

```python
g=lambda P,k:k//n*3**({w%K*K+w//K for w in P}=={*P})+sum(g(Q,k+1)for v in range(n)for Q in[P+[K*k+v]]if len({a-b for a in Q for b in Q if(a-b)%K})==k*k+k)
n=1
while[K:=2*n,print((g([],0)+7)//8)]:n+=1
```

**How it works**

- **Costas test.** The dot in column x and row y is the number K·x + y with
  K = 2n. Since |Δy| < n, the difference of two codes, K·Δx + Δy,
  determines the displacement (Δx, Δy). Differences divisible by K are
  exactly those with Δy = 0 (zero, or two dots in one row); the others
  are kept, and k + 1 dots in distinct rows with distinct displacements
  give exactly k(k + 1) of them: `len({…if(a-b)%K})==k*k+k`. A repeated
  row or a repeated displacement makes the set smaller, and a part of a
  Costas array passes too, so `g` places one dot per column (k = column)
  and prunes as it goes.
- **Burnside.** For n ≥ 3 no Costas array is fixed by the half-turn (it
  would give the dot pairs in columns 0, 1 and in columns n − 2, n − 1 the
  same displacement), hence none by a quarter-turn; the reflections in the
  middle row or column fix no permutation array. Only the identity and the
  two diagonal reflections fix any, so with C(n) Costas arrays and S(n)
  symmetric about the main diagonal (as many as about the other one, by a
  quarter-turn), a(n) = (C(n) + 2·S(n))/8. A completed array (k = n, the
  only k with `k//n` = 1) adds 3 if its permutation is an involution and
  1 otherwise, tested by mapping every code K·x + y to K·y + x:
  `3**({w%K*K+w//K for w in P}=={*P})`. A dot in column n would repeat a
  row, so the search stops there.
- `(…+7)//8` is exact for n ≥ 3 and also gives a(1) = 1 (C = S = 1, total
  3) and a(2) = 1 (C = S = 2, total 6).

**Notes**

- Exact integers, no stored terms: a plain search over all Costas arrays,
  counted with Burnside's lemma (the argument above). The symmetric ones
  alone give [A001440](../A001440/) far faster.
- a(10) = 277 comes after about 47 s here, each term taking six to eight
  times as long as the one before. The bar is 10 terms in 120 s (the
  b-file has 29).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 199 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001441), CC BY-SA 4.0.
