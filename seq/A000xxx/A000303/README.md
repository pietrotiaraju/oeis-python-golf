# A000303

> Number of permutations of [n] in which the longest increasing run has length 2.
> — [OEIS A000303](https://oeis.org/A000303)

Offset 1: 0, 1, 4, 16, 69, 348, 2016, 13357, 99376, 822040, …

### Python 3 — 83 bytes

```python
v=[1,1]
while[print(v[0]-1)]:v=[i*v[i-1]+-~i*sum(v[i:i+2])for i in range(len(v)+1)]
```

**How it works**

- Every increasing run has length at most 2 exactly when the permutation
  has no three consecutive rising entries. Those permutations are counted
  by [A049774](https://oeis.org/A049774)(n); only the decreasing
  permutation has all runs of length 1, so a(n) = A049774(n) − 1.
- By complement, A049774(n) also counts the permutations with no double
  fall (π(k) > π(k+1) > π(k+2)). Pad π with 0 on the left and ∞ on the
  right and insert the values 1, 2, …, n in increasing order (a Laguerre
  history, as in Françon–Viennot). With h gaps still open between placed
  entries plus the gap before ∞, value k is a valley (opens a gap,
  h + 1 choices), a double rise (h + 1 choices), a double fall (h
  choices, now forbidden) or a peak (closes one of the h gaps). So
  A049774(n) is the number of Motzkin paths of length n with level steps
  at height h weighted h + 1 and each up/down pair at heights h, h+1
  weighted (h + 1)², which is (Mⁿ)₀₀ for the tridiagonal matrix with
  1, 2, 3, … on the main and both side diagonals: the J-fraction
  1/(1 − x − x²/(1 − 2x − 4x²/(1 − 3x − …))) in A049774.
- `v[i]` is the weighted number of paths of the current length that end
  at height i, and the update is (Mv)ᵢ = i·v[i−1] + (i+1)·(v[i] + v[i+1]).
  At i = 0 the factor i kills `v[-1]`, and the slice `v[i:i+2]` gives 0
  past the end, so the list needs no padding and grows by one entry per
  step.
- The start `v=[1,1]` is M applied to (1), so the first print is
  A049774(1) − 1 = a(1) = 0.

**Notes**

- Exact integer arithmetic, correct for every n by the bijection above.
  Each term costs one pass over a list of length n. The b-file has
  464 terms (n = 1 to 464) and all of them print in about a second; the
  program stops after about 1600 terms, at the 4300-digit int-to-str
  limit of Python 3.11+. The bar is the whole b-file in 60 s.
- The cluster recurrence from the e.g.f.
  1/Σ(x^(3j)/(3j)! − x^(3j+1)/(3j+1)!),
  `sum(math.comb(n,k)*(-k%3-1)*b[-k]for k in range(n+1))` (the k = 0
  term subtracts the 1), is 104 bytes with the import, and printing after
  the update from `v=[1]` is 83 bytes as well.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000303), CC BY-SA 4.0.
