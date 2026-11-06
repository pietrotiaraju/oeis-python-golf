# A000550

> Number of trees of diameter 7.
> — [OEIS A000550](https://oeis.org/A000550)

Offset 8: 1, 3, 14, 42, 128, 334, 850, 2010, 4625, 10201, …

### Python 3 — 315 bytes

```python
L=[[]for _ in range(4)];n=0
while 1:
 n+=1
 for h in range(4):L[h]+=[1 if n==1 else sum(sum(L[h][n-d*j-1]for j in range(1,(n-1)//d+1))*d*L[h-1][d-1]for d in range(1,n))//(n-1)if h else 0]
 if n>=8:
  R=[a-b for a,b in zip(L[3],L[2])]
  print((sum(R[j-1]*R[n-j-1]for j in range(1,n))+(R[n//2-1]if n%2==0 else 0))//2)
```

**How it works**

- Let T_h count rooted unlabeled trees of height at most h, with
  T₀=x. An unordered multiset of T_(h−1) branches gives
  T_h=x·exp(Σₖ≥₁ T_(h−1)(x^k)/k).
- The logarithmic-derivative coefficient recurrence computes each new
  coefficient using earlier sizes. `L[h][m−1]` is [x^m]T_h.
- Removing T₂ from T₃ gives rooted trees of height exactly 3. A tree of
  diameter 7 has a unique central edge whose two halves both have height
  3, so its generating function is (R(x)²+R(x²))/2.
- The last expression is the S₂ cycle index: the convolution counts
  ordered halves and the even-index correction counts the fixed pairs.

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

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000550), CC BY-SA 4.0.
