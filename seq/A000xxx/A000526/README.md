# A000526

> Number of partially labeled trees with n nodes (5 of which are labeled).
> — [OEIS A000526](https://oeis.org/A000526)

Offset 5: 125, 1296, 8716, 47787, 232154, 1040014, 4395772, 17781210, 69498964, 264248924, …

### Python 3 — 218 bytes

```python
r=[n:=0,1]
while 1:
 m=-n
 if m>=5:
  B=m**m+1;M=B**(m+1);S=sum(r[j]*B**j for j in range(1,m+1))
  print(S**5*(125-204*S+118*S*S-24*S**3)*pow(1-S,-7,M)//B**m%B)
 n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
```

**How it works**

- Let R(x) count ordinary unlabeled rooted trees, as in
  [A000081](../A000081/). The OEIS generating function is
  R⁵(125−204R+118R²−24R³)/(1−R)⁷.
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
- The reference file contains 196 terms from the OEIS b-file; the verification
  bar is 30 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 218 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000526), CC BY-SA 4.0.
