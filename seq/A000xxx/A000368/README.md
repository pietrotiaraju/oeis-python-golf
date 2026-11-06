# A000368

> Number of connected graphs with one cycle of length 4.
> — [OEIS A000368](https://oeis.org/A000368)

Offset 4: 1, 1, 4, 9, 28, 71, 202, 542, 1507, 4114, 11381, 31349, 86845, …

Cut the four edges of the square and each corner keeps a rooted tree, so
a(n) counts 4-tuples of rooted trees with n nodes in all, up to the
symmetries of the square. With t(x) the g.f. of rooted trees
([A000081](../A000081/)), the OEIS g.f. is the cycle index of the dihedral
group D₄: (t(x)⁴ + 2·t(x)²·t(x²) + 3·t(x²)² + 2·t(x⁴))/8.

### Python 3 — 170 bytes

```python
r=[n:=0,1];P=[0]
Q=lambda L:sum(L[-i]*(L[i-n]+(i+i==n))for i in range(n,1))//2
while[n>-4or print(Q(P))]:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;P+=Q(r),
```

**How it works**

- **D₄ is S₂ ≀ S₂.** The symmetries of the square are exactly the
  permutations of its corners that keep the two diagonals as a pair of
  pairs (both groups have order 8), so a decorated square is an unordered
  pair of unordered pairs of rooted trees. Accordingly, with
  Z(S₂)[f] = (f(x)² + f(x²))/2, the cycle index above is
  Z(S₂)[Z(S₂)[t]]: P(x) = (t(x)² + t(x²))/2 counts unordered pairs of
  rooted trees, and the answer is (P(x)² + P(x²))/2.
- `Q(L)` is one application of Z(S₂) at the current size N = −n:
  Σ_{a+b=N} L(a)·(L(b) + [a = b])/2, which is
  (Σ L(a)·L(N − a) + [N even]·L(N/2))/2, exact. With i running over
  −N…0, `L[-i]` is L(a) for a = −i and `L[i-n]` is L(N − a); `(i+i==n)`
  adds the diagonal term.
- `r` is t(0), t(1), … with t(0) = 0: the [A000081](../A000081/) record's
  loop, which keeps r one term ahead (r has t(0)…t(N + 1) at size N).
  After each new tree count, `P+=Q(r),` appends P(N), and the loop
  condition evaluates `Q(P)` = a(N) from P(0)…P(N).
- a(N) = 0 for N < 4, and `n>-4or` skips those sizes, so printing starts
  at a(4) = 1 (the bare square).

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(n) has about 0.47·n digits (936 at n = 2000), so the
  4300-digit int-to-str limit is near n = 9100, beyond what the program
  reaches.
- About 2600 terms in 60 s here; the bar is the whole b-file (1997 terms,
  n ≤ 2000), which takes about 27 s.
- Doing both Z(S₂) steps in one loop, `for L in r,P:P+=…,` with the second
  result popped off P and printed, is 179 bytes. Writing the diagonal term
  outside the sum, `+L[-n//2]*(~n%2)` after a `map(int.__mul__,…)` dot
  product, is longer than `(i+i==n)` inside it, and so is running a over
  0…N with `range(1-n)`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 170 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000368), CC BY-SA 4.0.
