# A000786

> Number of inequivalent planar partitions of n, when considering them as 3D objects.
> — [OEIS A000786](https://oeis.org/A000786)

Offset 0: 1, 1, 1, 2, 4, 6, 11, 19, 33, 55, 95, 158, 267, 442, 731, 1193, 1947, 3137, 5039, 8026, …

### Python 3 — 153 bytes

```python
L=[1,3,2];n=0
while[print(sum(L[-3:])//6)]:
 n-=1
 for t in 0,1,2:L+=sum(d*[-d,d%2or-d//4,-~-d%3-1or(3-d)//9][t]*sum(L[3*d::3*d])for d in range(n,0))//n,
```

**How it works**

- **Burnside.** As 3-D objects, plane partitions of n are stacks of n unit
  cubes in the corner of space, closed downward; two are the same object when
  a permutation of the three axes (the group S₃) maps one to the other.
  Write P(n) for all plane partitions ([A000219](../A000219/)), S(n) for the
  ones fixed by the swap x↔y (symmetric plane partitions,
  [A005987](https://oeis.org/A005987)), C(n) for the ones fixed by the
  3-cycle x→y→z→x (cyclically symmetric, [A096419](https://oeis.org/A096419))
  and T(n) for the ones fixed by all of S₃ (totally symmetric,
  [A048141](https://oeis.org/A048141)).
- Burnside's lemma over the six permutations: the identity fixes P(n), each
  of the three swaps fixes S(n) of them, each of the two 3-cycles fixes
  C(n), so 6·a(n) = P(n) + 3·S(n) + 2·C(n).
- **Three Euler products.** P, S and C have product generating functions
  Π_k (1 − x^k)^(−b(k)):
  - P: b(k) = k (MacMahon);
  - S: Π_i 1/(1 − x^(2i−1)) · Π_{i<j} 1/(1 − x^(2(i+j−1))) (Andrews,
    Gordon; Stanley 1971, Prop. 14.3), so b(k) = 1 for odd k and ⌊k/4⌋ for
    even k;
  - C: the Mills–Robbins–Rumsey theorem (Macdonald's conjecture, 1982)
    gives the size generating function of the cyclically symmetric plane
    partitions in an m×m×m box as
    Π_{i=1..m} (1 − x^(3i−1))/(1 − x^(3i−2)) · Π_{j=i..m} (1 − x^(3(m+i+j−1)))/(1 − x^(3(2i+j−1))).
    A cyclically symmetric partition that reaches coordinate m contains
    (m,0,0), (0,m,0), (0,0,m) and everything below them, so at least 3m+1
    cubes; below degree 3m+1 the box does not matter and the factors that
    change with m have degree above 3m, so the limit m → ∞ is
    Π_i (1 − x^(3i−1))/(1 − x^(3i−2)) · Π_{i≤j} 1/(1 − x^(3(2i+j−1))):
    b(k) = 1 and −1 for k ≡ 1, 2 (mod 3) and ⌊(k+3)/9⌋ for k ≡ 0 (the
    number of i ≤ j with 2i+j−1 = k/3).
- **Euler transform.** For F = Π (1 − x^k)^(−b(k)) the logarithmic
  derivative gives m·f(m) = Σ_k k·b(k)·(f(m−k) + f(m−2k) + …), an exact
  division. The three series live interleaved in one list
  `L = [P(0), 3·S(0), 2·C(0), P(1), …]`, each pre-scaled by its Burnside
  weight (the recurrence is linear, so scaling the start scales the whole
  series). With d = −k the slice `L[3*d::3*d]` steps back 3k places, i.e.
  k terms of the series being computed, whichever it is.
  Then `sum(L[-3:])//6` is a(n); `L=[1,3,2]` holds P(0), 3·S(0), 2·C(0).
- **Weights in d = −k.** `-d` is k; `d%2or-d//4` is 1 for odd k, else
  ⌊k/4⌋ (`-d//4` floors −d = k); `-~-d%3-1` is (k+1) mod 3 − 1, i.e. 1, −1, 0
  for k ≡ 1, 2, 0 (mod 3), and the `or` falls through to `(3-d)//9` =
  ⌊(k+3)/9⌋ exactly when it is 0.
- `for t in 0,1,2:` picks the weight by `[t]`; the one-line
  `exec("…;"*3)` form with `[len(L)%3]` is 1 byte longer.

**Notes**

- Exact integer arithmetic. Correctness for every n rests on the product
  formulas for S (Andrews–Gordon/Stanley) and C (Mills–Robbins–Rumsey);
  the program matches the whole b-file.
- 4184 terms in 60 s here. The b-file has 151 terms; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 153 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000786), CC BY-SA 4.0.
