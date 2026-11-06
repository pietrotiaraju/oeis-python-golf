# A000524

> Number of rooted trees with n nodes, 2 of which are labeled.
> — [OEIS A000524](https://oeis.org/A000524)

Offset 2: 2, 9, 34, 119, 401, 1316, 4247, 13532, 42712, 133816, …

### Python 3 — 195 bytes

```python
r=[n:=0,1]
while 1:
 m=-n
 if m>=2:
  B=m**m+1;M=B**(m+1);S=sum(r[j]*B**j for j in range(1,m+1))
  print(S*S*(2-S)*pow(1-S,-3,M)//B**m%B)
 n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
```

**How it works**

- Let R(x) count ordinary unlabeled rooted trees, as in
  [A000081](../A000081/). The OEIS generating function is
  R²(2−R)/(1−R)³.
- The last line generates R's coefficients from its Euler-transform
  logarithmic derivative. At m=−n, `r[j]` is [x^j]R(x) through degree m.
- Evaluate R at the integer base B=m^m+1. Because R(0)=0, 1−R(B)
  is coprime to B; Python's negative modular exponent computes the
  truncated inverse power modulo B^(m+1).
- Every coefficient through degree m counts partially labeled trees.
  Labeling all remaining vertices maps the set of fully labeled trees
  onto these classes, so each coefficient is at most j^(j−1)≤m^m<B.
  No carry occurs between base-B digits. Dividing by B^m and reducing
  modulo B therefore extracts the exact requested coefficient.

**Notes**

- Negative terms in the numerator are handled modulo B^(m+1); the final
  coefficients are the nonnegative tree counts in the generating function.
- Large-integer coefficient extraction is costly. The bar is the first
  30 terms, and Python's output conversion limit eventually applies.
- The reference file contains 199 terms from the OEIS b-file; the verification
  bar is 30 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 195 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000524), CC BY-SA 4.0.
