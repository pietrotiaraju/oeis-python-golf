# A000282

> Finite automata.
> — [OEIS A000282](https://oeis.org/A000282)

Offset 1: 3, 70, 3783, 338475, 40565585, 6061961733, 1083852977811, 225615988054171, …

### Python 3 — 272 bytes

```python
from math import*
f=lambda m,r,*P:~-m*f(m-1,r+1,*P)+f(m-1,1,r,*P)if m else sum(prod(sum(d*(r*-~(x:=e&r)%d<1)for d in P+P)**(2-x)for r in P)for e in(0,1))
R=1,;E=[n:=0];F=2
while 1:n+=1;F*=n;R=f(n,1)//F,*R;E+=n*R[0]-sum(E[d]*sum(R[d::d])for d in range(1,n)),;print(E[n]//n)
```

**How it works**

- The OEIS formula: a(n) is the inverse Euler transform of
  [A054747](https://oeis.org/A054747)(n), the number of n-state 2-input
  2-output automata up to renaming the states and swapping the inputs. That
  count is Burnside's lemma over S_n × S_2 (Harrison 1965, Theorem 6.2).
- Fixed points: (σ, τ) permutes the (state, input) pairs. An automaton fixed by
  it chooses one (next state, output) per cycle of that action. For a cycle of
  length L, the choice must be fixed by σ^L, and there are
  s(L) = 2·(sum of the σ-cycle lengths that divide L) such choices. In the code
  s(L) is `sum(d*(L%d<1)for d in P+P)`: P lists σ's cycle lengths, and `P+P`
  counts each one twice, once per output.
- A σ-cycle of length r gives the factor s(r)² when τ is the identity. With
  the inputs swapped it gives s(2r) when r is odd and s(r)² when r is even.
  Both cases are s(r·(1+x))^(2−x) with x = `e&r`, where e = 0 for the
  identity and e = 1 for the swap.
- `f` builds σ one element at a time. With m−1 elements still free, the open
  cycle of length r either takes one of them (m−1 ways) or closes, and the next
  cycle starts at the smallest free element. So `f(n,1)` adds up the
  fixed-point counts over all n! state permutations and both τ, which is
  2·n!·A054747(n). `F` holds 2·n!. At m = 1 nothing is free: the extend branch
  is multiplied by 0, and the close branch passes the full cycle list to the
  base case.
- Inverse Euler transform: with E(d) = d·a(d) and A = A054747,
  n·A(n) = Σ_{d=1..n} E(d)·Σ_{j≥1} A(n−dj). This is the log-derivative of
  A(x) = Π(1−x^d)^(−a(d)). `R` is a tuple holding A(n), A(n−1), …, A(0) = 1, so the inner
  sum is `sum(R[d::d])`. The term d = n is E(n)·A(0), so E(n) is
  n·A(n) minus the rest, and a(n) = E(n)/n.

**Notes**

- Exact integer arithmetic. The work grows like 2^n (one leaf per
  composition of n): the whole b-file (16 terms, the data of the entry) takes
  about 12 s. The bar is the whole b-file in 60 s.
- Correct for every n relative to the OEIS formula (inverse Euler transform
  of A054747). That formula reproduces all 16 listed terms. It is not a direct
  count of connected automata under one input swap shared by the whole
  automaton, though. A brute force over all 2-state automata finds 69 weakly
  connected classes instead of 70, and 3726 instead of 3783 for n = 3.
  The Euler step counts two one-state components with outputs 01/01 and
  01/10 as one automaton, but no single swap of the inputs turns one into the
  other. The program follows the OEIS terms.
- Choosing the cycle through the smallest free element in one step
  (`sum(perm(m-1,r)*f(m+~r,r+1,…)for r in range(m))`) is 288 bytes.
  Keeping the open cycle at the front of `P` (`P[0]+1,*P[1:]`) is 278. Looping
  over compositions as bit masks needs an explicit weight for each mask and is
  longer still.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 274 | first entry |
| 2026-11-06 | Python 3 | 272 | keep R as a tuple; prepend without a list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000282), CC BY-SA 4.0.
