# A000591

> Number of n-state 2-input 1-output automata with one initial and one terminal state.
> — [OEIS A000591](https://oeis.org/A000591)

Offset 1: 10, 378, 16576, 819470, 45660051, 2846339383, 196946930215, 15006717613499, 1250005718758059, 113076157328915784, …

### Python 3 — 378 bytes

```python
from math import*
def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1)for p in P(n-j,j)]
def f(p):return prod(sum(d for d in p if j%d<1)for j in p)
n=0
while 1:
 H=factorial(n);T=0
 for p in P(n):
  q=p+(1,1);r=tuple(j//gcd(j,2)for j in q for _ in range(gcd(j,2)))
  T+=H//prod(j**p.count(j)*factorial(p.count(j))for j in set(p))*(f(q)**2+f(r))
 print(T//(2*H));n+=1
```

**How it works**

- Apply Burnside's lemma to two state-transition maps, allowing the
  two input symbols to be interchanged. The initial and terminal states
  are distinct and fixed; the remaining `n` states may be permuted.
  A partition `p` represents their cycle type; `q=p+(1,1)` includes
  the two marked states.
- A map commuting with a permutation of cycle type q has
  f(q)=∏_{j in q} Σ_{d in q,d|j} d choices: the image of a j-cycle
  may start at any point fixed by the j-th power of the permutation.
- With the input symbols fixed there are f(q)² pairs of maps. If the
  inputs are exchanged, one map determines the other and must commute
  with the square of the state permutation; its cycle type is `r`.
  This contributes f(r).
- Weight each type by its conjugacy-class size and divide by 2n!.
  With no unmarked states the count is (4²+4)/2=10. The published
  sequence indexes this two-marked-state case at 1, so its index is n+1.

**Notes**

- The calculation follows the automaton orbit model of Harary and Palmer,
  [*Enumeration of finite automata* (1967), formula (19)](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/33337/0000734.pdf?isAllowed=y&sequence=1), the OEIS reference. The index
  convention is stated explicitly because the two marked states are
  already present when the internal counter is zero.
- All divisions are exact group averages; no finite automaton counts or
  fitted recurrence are embedded in the program.
- The reference file contains 13 published OEIS terms; the verification
  bar is 13 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 378 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000591), CC BY-SA 4.0.
