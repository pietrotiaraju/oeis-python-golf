# A000518

> Generalized tangent numbers d_(n,4).
> — [OEIS A000518](https://oeis.org/A000518)

Offset 1: 272, 24611, 515086, 4456448, 23750912, 93241002, 296327464, 806453248, 1951153920, 4300685074, …

### Python 3 — 155 bytes

```python
D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*(427*a**6-175*a**4*u*u+21*a*a*u**4-u**6)-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
```

**How it works**

- Extend [A000488](../A000488/)'s Gauss-sum recurrence to the eighth-power
  Dirichlet series. The odd-frequency cosine series is
  π⁸E₇(t)/(4·7!) on 0≤t≤1, where E₇ is an Euler polynomial.
- In the folded coordinate u=|y² mod 4n−2n|−n, the scaled polynomial is
  u(427n⁶−175n⁴u²+21n²u⁴−u⁶). Its coefficients follow from
  2⁷E₇((z+1)/2)=z⁷−21z⁵+175z³−427z.
- Summation over y modulo 2n gives the desired value plus the proper
  odd-divisor terms. The `D[a//y]` subtraction applies exactly when y
  is an odd divisor, as in A000488.
- `D` stores twice the value except at n=1, whose tangent-number
  normalization is already correct. `>>1%a` preserves the first value
  272 and halves every subsequent sum.

**Notes**

- The finite sums and divisor correction use exact integers throughout.
  Each new term takes O(n) arithmetic operations.
- This is a general recurrence, rather than interpolation from the table.
- The reference file contains 1000 terms from the OEIS b-file; the verification
  bar is 1000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 155 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000518), CC BY-SA 4.0.
