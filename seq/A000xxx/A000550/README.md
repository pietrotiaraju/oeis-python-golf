# A000550

> Number of trees of diameter 7.
> — [OEIS A000550](https://oeis.org/A000550)

Offset 8: 1, 3, 14, 42, 128, 334, 850, 2010, 4625, 10201, …

### Python 3 — 187 bytes

```python
*L,n=1,1,0;R=0,0
while[n>-14or print((sum(map(int.__mul__,R,R[::-1]))+n//2%2*R[-n//4+1])//2)]:
 n-=2
 for h in 1,0:L+=sum(d*L[~d*h]*sum(L[d::d])for d in range(n,0,2))//n,
 R+=L[-2]-L[-1],
```

**How it works**

- Trees of rooted height at most 2 are counted by p(N−1), where p is
  the partition function. Trees of height at most 3 are counted by
  c(N−1), where ∑c(m)x^m=∏ₖ≥₁(1−xᵏ)^(−p(k−1)). Their difference
  counts rooted trees of height exactly 3, as in [A000235](../A000235/).
- `L` interleaves c(0),p(0),c(1),p(1),… . At n=−2m the two passes
  append c(m) and p(m), using their exact Euler-transform recurrences:
  m·c(m)=∑ₖ k·p(k−1)∑ⱼ≥₁c(m−jk) and
  m·p(m)=∑ₖ k∑ⱼ≥₁p(m−jk). The negative even slice indices read
  earlier coefficients; the factors of 2 cancel in the division by n.
- `R` holds R₀,…,R_N, with R₀=0 and R_N=c(N−1)−p(N−1).
  Its initial pair supplies the zeros R₀=R₁=0. Every tree of diameter 7
  has a unique central edge with two rooted halves of height exactly 3.
  Thus its generating function is (R(x)²+R(x²))/2.
- The scalar product of `R` and its reverse is [x^N]R(x)². Here N=m+1,
  so `n//2%2` is 1 exactly when N is even, and `-n//4+1` then indexes
  R_(N/2). This supplies the fixed pairs in the unordered-pair count.
  Printing begins at n=−14, or N=8, the minimum possible size.

**Notes**

- This is an exact multiset decomposition for unlabeled trees. The
  minimum size is 8, so printing begins there.
- All divisions follow formal-series identities and are exact.
- The reference file contains 50 terms from the published OEIS entry; the verification
  bar is 50 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 315 | first entry |
| 2026-11-06 | Python 3 | 187 | interleaved Euler transforms and central-edge convolution |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000550), CC BY-SA 4.0.
