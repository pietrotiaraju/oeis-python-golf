# A000527

> Series-parallel numbers.
> — [OEIS A000527](https://oeis.org/A000527)

Offset 4: 52, 472, 3224, 18888, 101340, 511120, 2465904, 11496144, 52165892, 231557064, …

### Python 3 — 218 bytes

```python
A=[1,n:=1]
while 1:
 if n>3:
  B=1<<((n+2)**2);M=B**(n+1);S=sum(A[j]*B**j for j in range(1,n+1))
  print(4*(13+14*S+3*S*S)*(1+S)*pow(1-S,-7,M)//B**(n-4)%B)
 n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- Generate the series-parallel enumerator S(x) of
  [A000084](../A000084/) with its Euler-transform recurrence.
  The OEIS formula for this entry is
  4(13+14S+3S²)(1+S)/(1−S)⁷, whose constant coefficient is 52.
- The listed offset is 4, so at order n the program extracts degree n−4
  of that expression. Terms beyond that degree cannot affect the result.
- As in the tree records, substitution x=B and inversion modulo B^(n+1)
  turn formal coefficient extraction into exact integer arithmetic.
  The base is chosen above the coefficients needed in the extraction.

**Notes**

- This follows the stated series identity rather than fitting a
  recurrence to the known terms.
- The large integer base makes this a straightforward reference record;
  the verification bar is 15 terms.
- The reference file contains 35 terms from the OEIS b-file; the verification
  bar is 15 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 218 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000527), CC BY-SA 4.0.
