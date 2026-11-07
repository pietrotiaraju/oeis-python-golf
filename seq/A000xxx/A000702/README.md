# A000702

> a(n) is the number of conjugacy classes in the alternating group A_n.
> — [OEIS A000702](https://oeis.org/A000702)

Offset 1: 1, 1, 3, 4, 5, 7, 9, 14, 18, 24, 31, 43, 55, 72, 94, 123, 156, 200, 254, 324, …

### Python 3 — 92 bytes

```python
L=[[1]]
while 1:k=0;L=[r:=[sum(r[:(k:=k+1)])for r in L]]+L;print(3*sum(r[::-2])-sum(r)-1//k)
```

**How it works**

- A conjugacy class of S_n is a cycle type, a partition of n. It lies in
  A_n when the permutation is even, i.e. when n − (number of parts) is
  even. For n ≥ 2 such a class splits into two A_n classes exactly when
  its parts are distinct and odd (its centralizer is then inside A_n), and
  every such partition is even. So a(n) = E + Q, where E counts the even
  cycle types and Q the partitions into distinct odd parts.
- With p(n,k) the partitions of n into exactly k parts and O = p(n) − E
  the odd types, Q = E − O: the signed sum Σ (−1)ⁿ⁻ᵏ p(n,k) is the
  coefficient of xⁿ in ∏ 1/(1+(−x)ʲ) = ∏ (1+x²ʲ⁻¹) (see
  [A000701](../A000701/)). Hence a(n) = 2E − O = 3E − p(n), the
  Dénes–Erdős–Turán formula (p(n) + 3Q(n))/2.
- The triangle p(n,k) is built as in [A000701](../A000701/): `L` holds the
  rows newest first, and p(n,k) is the sum of the first k entries of row
  n−k, which is the k-th row met when walking `L`; the walrus counter `k`
  gives the prefix length.
- `r[::-2]` takes k = n, n−2, …, the even types, so `3*sum(r[::-2])-sum(r)`
  is 3E − p(n).
- n = 1 is the one exception: A_1 = S_1 is trivial and its only class does
  not split, while the formula gives 2. After the walk `k` equals n, so
  `-1//k` (parsed as −(1//k)) subtracts 1 exactly when n = 1.

**Notes**

- Exact integer additions; row n costs about n²/4 additions and all rows
  are kept (about n²/2 integers).
- About 2200 terms in 60 s on the PC used; the b-file has 1000 terms
  (5 s), which is the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000702), CC BY-SA 4.0.
