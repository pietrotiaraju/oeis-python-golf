# A000485

> Number of partially labeled trees with n nodes (4 of which are labeled).
> — [OEIS A000485](https://oeis.org/A000485)

Offset 4: 16, 125, 680, 3135, 13155, 51873, 195821, 715614, 2550577, 8911942, …

### Python 3 — 205 bytes

```python
r=[n:=0,1]
while 1:
 m=-n
 if m>3:
  B=1<<(5*m+8);S=sum(r[k]*B**k for k in range(1,m+1))
  print(S**4*(16-19*S+6*S*S)*pow(1-S,-5,B**(m+1))//B**m%B)
 n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
```

**How it works**

Generate the ordinary rooted-tree series T with the
Euler-transform recurrence of [A000081](../A000081/).
The OEIS generating function is T^4*(16-19T+6T²)/(1-T)^5.
Pack the truncated tree series into base B and evaluate this
rational expression modulo B^(m+1). Its m-th base-B digit
is the required coefficient. Begin printing at m=4.

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
- The verification bar is 100 terms in 10 s; the official b-file contains 997 terms.
- Modular integer evaluation grows with m; the 100-term bar is chosen for this direct exact coefficient-extraction method.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 205 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000485), CC BY-SA 4.0.
