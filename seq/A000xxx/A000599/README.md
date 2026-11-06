# A000599

> Number of secondary alcohols (alkanols or alkyl alcohols C_n H_{2n+1} OH) with n carbon atoms.
> — [OEIS A000599](https://oeis.org/A000599)

Offset 0: 0, 0, 0, 1, 1, 3, 6, 15, 33, 82, …

### Python 3 — 224 bytes

```python
A=[1];C=[];n=0
print(0)
while 1:
 C+=sum(A[j]*A[n-j]for j in range(n+1)),
 A+=(sum(C[j]*A[n-j]for j in range(n+1))+3*sum(A[j]*A[n-2*j]for j in range(n//2+1))+2*(n%3<1)*A[n//3])//6,
 print((C[n]+(n%2<1)*A[n//2])//2-A[n]);n+=1
```

**How it works**

- Let A(x) count rooted alkyl radicals, including A₀=1 for the empty
  branch. Pólya's S₃ cycle index gives
  A(x)=1+x(A(x)³+3A(x)A(x²)+2A(x³))/6.
- `C[n]` is the coefficient of A(x)². The next update uses this cached
  square to obtain Aₙ₊₁ with two one-dimensional convolutions.
- Write H₂(A)=(A(x)²+A(x²))/2 and H₃(A)=(A(x)³+3A(x)A(x²)+2A(x³))/6.
  Two nonempty unordered branches have series H₂(A)−A; three have
  H₃(A)−H₂(A). Adding the central carbon contributes one factor x.
- A000598 prints Aₙ. A000599 and A000600 first print their zero
  constant term, then print respectively [x^n](H₂(A)−A) and
  Aₙ₊₁−[x^n]H₂(A). Removing the empty branch enforces secondary
  and tertiary alcohols rather than primary ones.

**Notes**

- Cycle-index divisions are exact orbit counts. There is no
  stereochemical distinction, matching the OEIS definitions.
- Caching the square reduces the per-term work to O(n) arithmetic
  operations. Large integer output eventually meets Python's limit.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 224 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000599), CC BY-SA 4.0.
