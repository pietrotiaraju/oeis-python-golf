# A000432

> Series-parallel numbers.
> — [OEIS A000432](https://oeis.org/A000432)

Offset 3: 8, 52, 288, 1424, 6648, 29700, 128800, 545600, 2269672, 9303140, …

### Python 3 — 184 bytes

```python
A=[1,n:=1]
while 1:
 B=1<<(5*n+3);S=sum(A[k]*B**k for k in range(1,n))
 print(4*(2+S)*(1+S)*pow(1-S,-5,B**n)//B**(n-1)%B)
 n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
```

**How it works**

Generate the coefficients of S, the A000084 series, with its
established Euler-transform recurrence. The OEIS generating
function is 4*(2+S)*(1+S)/(1-S)^5. Its constant coefficient
is a(3)=8, so degree m corresponds to index m+3. Pack the
truncated S into base B, evaluate that rational expression
modulo B^(m+1), and extract its m-th digit.

For exact digit extraction, the inner series has zero constant
term and its coefficient of x^k is at most 8^k: planar binary
series/parallel expression trees provide this upper bound, and
plane rooted trees give the stronger bound 4^k in the tree cases.
At x=1/32 the inner series is therefore at most 1/3. Replacing
numerator coefficients by their absolute values bounds every
outer expression used here by 128. Consequently every coefficient
through degree m is less than 128*32^m, whereas the chosen
base B=256*32^m is larger. The final coefficients are nonnegative
counts, so no base-B carries corrupt the extraction. Since
1-S is 1 modulo B, it is invertible modulo B^(m+1); Python's
three-argument pow computes the required inverse fifth power.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 38 terms in 60 s; the official b-file contains 38 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 184 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000432), CC BY-SA 4.0.
