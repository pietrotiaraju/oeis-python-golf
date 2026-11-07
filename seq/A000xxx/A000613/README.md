# A000613

> Number of Boolean functions of n variables.
> — [OEIS A000613](https://oeis.org/A000613)

Offset 1: 2, 4, 10, 46, 1372, 475499108, 1038397981840994509577948, …

### Python 3 — 192 bytes

```python
n=r=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^~i%2**n for y in m];i>>=n;t+=r;r=len({*m})>>n;k+=2*r
  for x in m:
   while~x:m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
```

**What is counted**

- The OEIS formula a(n) = [A000585](../A000585/)(n)/2, where A000585 counts
  the classes of Boolean functions of n variables under GL(n,2), the linear
  substitutions of the inputs. Every linear map fixes the zero vector, so the
  value f(0) splits those classes into two equal halves: a(n) is also the
  number of GL(n,2)-classes of functions with f(0) = 0.
- By Burnside's lemma a(n) = Σ_A 2^c(A) / (2·|GL(n,2)|), with c(A) the number
  of cycles of A on the 2ⁿ vectors.

**How it works**

- This is the [A000214](../A000214/) loop without the translation. `i` runs
  over all n×n matrices; its n-bit digits, complemented, are the columns, and
  the doubling `m+=[y^col for y in m]` makes `m[x]` the image of x.
- `len({*m})>>n` is 1 after the last column when the matrix is invertible and
  0 otherwise (and 0 after every earlier column), so `k` grows by 2 per
  element of GL(n,2), and `r` is 0 for a singular matrix.
- The walk marks visited points −1 and doubles `r` each time a cycle
  closes, so `r` ends at 2^c(A). It is added to `t` one matrix late, at the
  first column of the next one; the last matrix of each n is the zero matrix
  (all digits 1), whose r = 0 is the one left over. The initial r = 1 adds a
  spurious 1 only at n = 1, where t = 4 + 1 and k = 2, so `t//k` is still 2.

**Notes**

- The loop visits all 2^(n²) matrices: n = 4 takes about 2 s, n = 5 would
  need 2²⁵ matrices on 32 points (many minutes). The bar is the 4 terms
  n = 1 to 4 in 60 s; the b-file has 8.
- It is the A000585 count with `k+=2*r` instead of `k+=r`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 192 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000613), CC BY-SA 4.0.
