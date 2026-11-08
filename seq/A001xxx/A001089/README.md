# A001089

> Number of permutations of [n] containing exactly 2 increasing subsequences of length 3.
> — [OEIS A001089](https://oeis.org/A001089)

Offset 0: 0, 0, 0, 0, 3, 24, 133, 635, 2807, 11864, 48756, 196707, 783750, …

### Python 3 — 92 bytes

```python
from math import*
n=0
while[print((59*n*n+117*n+100)*comb(2*n-2%-~n,n+2)//perm(n+5,3))]:n+=1
```

**Why the formula**

- Noonan and Zeilberger conjectured, and Markus Fulmek proved ("Enumeration
  of permutations containing a prescribed number of occurrences of a
  pattern of length three", 2003; in the entry), that

  a(n) = (59n² + 117n + 100)·C(2n, n−4) / (2n(2n−1)(n+5)).

- C(2n, n−4)/(2n(2n−1)) = (2n−2)!/((n−4)!(n+4)!) =
  C(2n−2, n−4)/((n+3)(n+4)), so for n ≥ 1

  **a(n) = (59n² + 117n + 100)·C(2n−2, n+2) / ((n+3)(n+4)(n+5)).**

**How it works**

- `perm(n+5,3)` is (n+3)(n+4)(n+5); the division is exact because the
  result is the integer a(n).
- For n < 4 the binomial is 0 (n + 2 > 2n − 2), as it should be. Only
  n = 0 needs care: `comb` refuses a negative top. `2*n-2%-~n` is
  2n − (2 mod (n+1)): 0 at n = 0 (comb(0, 2) = 0), 2 at n = 1
  (comb(2, 3) = 0), and 2n − 2 for n ≥ 2. That is 2 bytes under
  `n and 2*n-2` and 9 under a separate `print(0)`.

**Notes**

- Exact integer arithmetic; correct for every n by Fulmek's theorem.
- Thousands of terms in 10 s; the bar is the whole b-file (1001 terms) in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001089), CC BY-SA 4.0.
