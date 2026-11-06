# A000425

> Coefficients of ménage hit polynomials.
> — [OEIS A000425](https://oeis.org/A000425)

Offset 1: 2, 0, 0, 8, 30, 192, 1344, 10800, 97434, 976000, …

### Python 3 — 57 bytes

```python
a=b=n=1;c=0
while[print(2*n*b)]:a,b,c=-b,c,n*(b+c)-a;n+=1
```

**How it works**

Let W_m be the straight-table ménage number [A000271](../A000271/).
Taking the coefficient of t in the ménage hit polynomial
U_n(t)=sum(2n/(2n-k)*C(2n-k,k)*(n-k)!*(t-1)^k,k=0..n)
gives 2n*sum((-1)^j*C(2n-j-2,j)*(n-j-1)!,j=0..n-1),
which is exactly 2n*W_(n-1). This proves the shifted identity
used here. The recurrence and state are those of A000271;
its counter n already corresponds to W_(n-1).

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 22 terms in 60 s; the official b-file contains 22 terms.
- The unshifted identity proposed in the OEIS entry is off by one: the identity proved and used here is a(n)=2n*A000271(n-1).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000425), CC BY-SA 4.0.
