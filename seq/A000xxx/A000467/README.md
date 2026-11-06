# A000467

> Number of permutations of [n] in which the longest increasing run has length 6.
> — [OEIS A000467](https://oeis.org/A000467)

Offset 1: 0, 0, 0, 0, 0, 1, 12, 137, 1602, 19710, …

### Python 3 — 167 bytes

```python
from math import*
L=[[1],[1]];n=0
while 1:
 n+=1
 for q,a in enumerate(L,6):a+=[sum(comb(n,k)*((k%q==1)-(k%q<1))*a[-k]for k in range(1,n+1))]
 print(L[1][-1]-L[0][-1])
```

**How it works**

- A run is a block of **consecutive positions** whose entries increase;
  it need not be a longest increasing subsequence. Let B_r(n) count
  permutations whose runs all have length at most r. The answer is
  B_6(n) − B_5(n).
- The bounded-run formula (Alekseyev, linked on the OEIS page) gives
  B_r(x) = 1/D_q(x), with q = r + 1 and
  D_q(x) = Σⱼ (x^(qj)/(qj)! − x^(qj+1)/(qj+1)!).
  Multiplying D_q(x)·B_r(x) = 1 and comparing exponential coefficients
  gives, for n ≥ 1,

  B_r(n) = Σₖ C(n,k)·([k ≡ 1 mod q] − [k ≡ 0 mod q])·B_r(n−k),
  where 1 ≤ k ≤ n and brackets are 1 or 0 according to the condition.

- `enumerate(L,6)` supplies q = 6, 7: the first list counts
  maximum run length at most 5, the second at most 6. Both start
  with B_r(0) = 1, the empty permutation. The lists are separate:
  `[[1]]*2` would alias them and give the wrong answer.
- Before appending, each list has length n, so `a[-k]` is its entry
  B_r(n−k). Boolean subtraction supplies the two signs without a
  conditional expression; the residue classes are disjoint.
- The last line subtracts the new entries. For n < 6 it prints 0;
  for n = 6 only the increasing permutation qualifies, giving 1.

**Notes**

- Exact integer arithmetic; the reciprocal-series recurrence determines
  every coefficient, rather than fitting the initial terms.
- This is the [A000402](../A000402/) construction with different
  bounds. It stores two lists of n+1 integers and evaluates two n-term
  sums per output, avoiding enumeration of n! permutations.
- Counts grow at factorial scale. Python 3.11+ eventually stops when a
  printed integer exceeds its default 4300-digit conversion limit;
  this interpreter limit is not a correctness failure.
- The b-file has 450 terms (indices 1 through 450). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 167 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000467), CC BY-SA 4.0.
