# A000591

> Number of n-state 2-input 1-output automata with one initial and one terminal state.
> — [OEIS A000591](https://oeis.org/A000591)

Offset 1: 10, 378, 16576, 819470, 45660051, 2846339383, 196946930215, 15006717613499, 1250005718758059, 113076157328915784, …

With one output letter the output map carries no information, so such an
automaton is a pair of transition maps δ_a, δ_b: S → S on a state set with a
marked initial state and a marked terminal state. The program counts these
up to renaming the unmarked states and swapping the two input letters, on
n + 1 states with initial ≠ terminal: that model gives all 13 published
terms (a brute-force orbit count over all pairs of maps confirms
a(1)–a(3) = 10, 378, 16576 on 2, 3 and 4 states), so the index n is one less
than the number of states.

### Python 3 — 189 bytes

```python
import math
f=lambda r,*L:r<1and sum(math.prod(sum(d>>(j<<j%e)%d*d for d in L)**(2-j%e)for j in L)for e in(1,2))or sum(f(r+~k,*L,k+1)for k in range(r))//r
n=0
while[print(f(n,1,1)//2)]:n+=1
```

**How it works**

- **Burnside's lemma.** The group is S_u × S₂: a permutation σ of the
  u = n − 1 unmarked states (the two marked states stay fixed) and a
  permutation of the inputs. If σ has cycle lengths L (the two marked states
  counted as two cycles of length 1), the number of maps g: S → S with
  σ∘g = g∘σ is h(L) = Π_{j∈L} Σ_{d∈L, d|j} d: the image of one point of a
  j-cycle must be a point fixed by σ^j, that is a point on a cycle whose
  length divides j, and it fixes the images of the rest of the cycle. With
  the inputs kept, a pair (δ_a, δ_b) is fixed when both maps commute with σ:
  h(L)² pairs. With the inputs swapped, δ_b = σδ_aσ⁻¹ and δ_a must commute
  with σ²: h(L′) pairs, where L′ is the cycle type of σ² (a j-cycle becomes
  one j-cycle for odd j and two j/2-cycles for even j). So

  a(n) = (1/(2·u!)) Σ_σ (h(L)² + h(L′)).
- **One formula for both terms.** For e = 1, 2 the program computes
  Π_{j∈L} (Σ_{d∈L, d | j·2^(j mod e)} d)^(2 − j mod e). For e = 1 that is
  h(L)². For e = 2 it is h(L′), counted on the cycles of σ²: an odd j-cycle
  stays one cycle of σ² of length j, and the image of one of its points must
  be fixed by σ^(2j), which gives Σ_{d|2j} d; an even j-cycle splits into two
  cycles of length j/2, each with Σ_{d|j} d choices (points fixed by σ^j),
  which gives the square. In the code `j<<j%e` is j·2^(j mod e), and
  `d>>X%d*d` is d when d | X and 0 otherwise (a shift by at least d clears
  d).
- **Summing over σ.** `f(r,*L)` is (1/r!) Σ over the permutations of r
  further states of that e-sum, given the cycles L already chosen. The cycle
  through one fixed point of the r states has length k + 1 in
  (r−1)!/(r−k−1)! ways, and the other r − k − 1 points are permuted freely,
  so f(r, L) = (1/r) Σ_{k=0}^{r−1} f(r−k−1, L + [k+1]) (`r+~k` is r − k − 1).
  The loop variable `n` is u: `f(n,1,1)` starts L with the two marked
  states, and `f(n,1,1)//2` is a(u+1), so the output starts at a(1).
- **Exact `//r`.** Every f(r, L) is an integer: by de Bruijn's form of
  Burnside's lemma, for a group H normal in G and g ∈ G,
  (1/|H|) Σ_{h∈H} fix(hg) is the number of H-orbits that g maps to
  themselves. Here H = S_r acts on the r new states, and g is a fixed
  permutation of cycle type L on the other states (with the input swap for
  e = 2), which commutes with H. So the sum over k is r times an integer.

**Notes**

- The first version of this page enumerated partitions with explicit
  class sizes and built the cycle type of σ² as a list: 353 bytes.
- Exact integer arithmetic; correctness rests on Burnside's lemma and the
  model above, which matches all 13 published terms.
- The recursion visits all 2^(u−1) compositions of u, so time doubles per
  term: 19 terms in 60 s here. The b-file has 13 terms (up to a(13)); the
  bar is the whole b-file in 60 s.
- a(n) is below (n+1)^(2n+2), the number of pairs of maps, so the 4300-digit
  int-to-str limit would need n above 700, far beyond reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 378 | first entry |
| 2026-11-06 | Python 3 | 353 | occurrence-index class factors and compact cycle lists |
| 2026-11-07 | Python 3 | 189 | composition recursion with exact `//r`, one e-indexed formula for σ and σ² |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000591), CC BY-SA 4.0.
