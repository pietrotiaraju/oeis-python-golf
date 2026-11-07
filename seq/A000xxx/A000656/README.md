# A000656

> Invertible Boolean functions of n variables with S(n) acting on the domain and GL(n,2) acting on the range.
> — [OEIS A000656](https://oeis.org/A000656)

Offset 1: 2, 3, 56, 43265712, 219289731988435167257927904, …

### Python 3 — 325 bytes

```python
n=1
while 1:
 D={};a=c=0
 for i in range((N:=2**n)**n*2):
  for _ in[m:=[s:=0]]*n:m+=[y^i%N for y in m];s+=i%N;i>>=n
  z=len({*m})>>n;l=[]
  for x in m*z:
   j=-1
   while~x:m[x],x=-1,m[x];j+=1
   if j:l+=j,;z*=j*l.count(j)
  k=(*sorted(l),);D[k]=d=D.get(k,0)+(i<1>s>>n<z);a+=i*d*z;c+=i*z>0
 print(a//c//sum(D.values()));n+=1
```

**What is counted**

- Classes of permutations π of V = {0,1}ⁿ (N = 2ⁿ points) under
  π ↦ A∘π∘σ̂⁻¹, with σ̂ a permutation of the variables and A ∈ GL(n,2).
- Burnside over the pairs (σ, A): π is fixed when π∘σ̂∘π⁻¹ = A, which needs
  the same cycle type T on the N points and then has z_T = Π_j j^(c_j)·c_j!
  solutions. With S_T and G_T the numbers of σ̂ and of A of type T,

  a(n) = Σ_T S_T·G_T·z_T / (n!·|GL(n,2)|).

**How it works**

- i runs over 2·Nⁿ values. The loop of [A000214](../A000214/),
  `for _ in[m:=[s:=0]]*n:m+=[y^i%N for y in m];s+=i%N;i>>=n`, reads the n
  lowest base-N digits of i as the columns of a matrix A, builds m[x] = Ax,
  adds the columns up in s and leaves in i the pass number 0 or 1.
- `z=len({*m})>>n` is 1 when A is invertible and 0 otherwise, so a singular
  A walks nothing (`m*z` is empty) and adds 0 everywhere.
- **Permutation matrices.** For invertible A, every row has a 1 and row b
  adds 2^b to the integer column sum, so s ≥ 2ⁿ − 1, with equality exactly
  when every row has a single 1. So `s>>n<1` picks the n! permutation
  matrices, the copy of S_n inside GL(n,2).
- **Two passes.** In pass 0, `D[k]` counts S_T (the chain `i<1>s>>n<z` is
  i = 0, s < N and A invertible). In pass 1 every invertible A adds
  S_T·z_T to a and 1 to c, so a = Σ_T S_T·G_T·z_T, c = |GL(n,2)|, and
  `sum(D.values())` = n!.
- The walk runs over the copy `m*z`, whose entries are the original images:
  a start already visited takes one step to −1 and, with j starting at −1,
  gives j = 0; a new cycle of length L gives j = L. `z*=j*l.count(j)` then
  turns the flag z = 1 into z_T.

**Notes**

- Every n×n matrix is tried twice: a(4) takes about 2 s here, while a(5)
  needs 2·2²⁵ matrices on 32 points, hours. The OEIS entry notes that
  Harrison's paper gives a(4) = 43265728; the program finds 43265712.
- The bar is 4 terms in 60 s; the b-file has 6.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 325 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000656), CC BY-SA 4.0.
