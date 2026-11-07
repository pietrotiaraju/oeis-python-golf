# A000615

> Number of threshold functions of exactly n variables.
> — [OEIS A000615](https://oeis.org/A000615)

Offset 0: 2, 2, 8, 72, 1536, 86080, 14487040, 8274797440, …

### Python 3 — 258 bytes

```python
import math
n=0
while 1:
 R=range(N:=2**n);V=[[0]];exec('V=[v+[a+c for a in v]for v in V for c in range(math.isqrt((n+1)**-~n)+N>>n)];'*n)
 print(N*sum(len({tuple(f[p^s]for p in R)for s in R})//N for f in{(*map(t.__lt__,v),)for v in V for t in v+[-1]}));n+=1
```

**What is counted**

- Threshold functions f(x) = [w·x > t] on {0,1}ⁿ that depend on all n inputs
  (for n = 0 the two constants). As in [A000609](../A000609/), integer
  weights with |wᵢ| ≤ (n+1)^((n+1)/2)/2ⁿ suffice (Muroga, Toda and Takasu,
  1961), and negating inputs turns every threshold function into a positive
  one, with weights in 0…B.
- For a positive (monotone) f, negating a set S of inputs leaves f unchanged
  only if every input in S is irrelevant. Otherwise take i in S relevant,
  with f(y) = 0 and f(y + eᵢ) = 1; set the other inputs of S to 1 in y + eᵢ
  (giving a with f(a) = 1) and to 0 in y (giving b with f(b) = 0). Negating
  S maps a to b, so f cannot be invariant. Hence the 2ⁿ negations of f are
  pairwise distinct exactly when f is nondegenerate.
- The same argument shows that a positive f with some inputs negated is
  positive again only when those inputs are irrelevant. So each
  nondegenerate threshold function is a nondegenerate positive one with a
  unique mask of negated inputs, and a(n) = 2ⁿ · #(nondegenerate positive
  threshold functions).

**How it works**

- The weight lists `V` and the set of positive threshold functions are built
  as in [A000609](../A000609/): `exec` doubles the list of sums w·x once per
  weight in 0…B, and `(*map(t.__lt__,v),)` is the truth table of [v > t] for
  t among the sums and t = −1.
- `len({…f[p^s]…for s in R})` is the number of distinct input negations of
  f, which is 2^(number of relevant inputs); `//N` makes it 1 exactly when f
  depends on every input, and `N*sum(…)` is a(n).

**Notes**

- Correctness for every n rests on the Muroga–Toda–Takasu weight bound;
  everything else is exhaustive integer enumeration.
- n = 5 enumerates 7⁵ weight vectors (about 4 s); n = 6 would need 15⁶ ≈ 11
  million. The bar is the 6 terms n = 0 to 5 in 60 s; the b-file has 10.
- Testing each single negation (`all(f!=tuple(f[p^1<<i]for p in R)for i in
  R[:n])`) is 6 bytes longer than counting all 2ⁿ negations.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 258 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000615), CC BY-SA 4.0.
