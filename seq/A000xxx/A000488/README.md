# A000488

> Generalized tangent numbers d_(n,3).
> — [OEIS A000488](https://oeis.org/A000488)

Offset 1: 16, 361, 3362, 16384, 55744, 152166, 355688, 739328, 1415232, 2529614, …

### Python 3 — 129 bytes

```python
D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*(5*a*a-u*u)**2-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
```

**How it works**

Apply the Gauss-sum and odd-divisor inversion of
[A000176](../A000176/) to the sixth-power Dirichlet series.
The odd-frequency cosine Fourier series is
sum(cos(pi*k*x)/k⁶,k positive odd)=-pi⁶*E_5(x)/480.
After folding x into [0,1] and writing
u=abs(y² mod 4n-2n)-n, its scaled Euler polynomial is
u*(5n²-u²)². Thus U(n)=sum(u*(5n²-u²)²,y mod 2n)/2
equals sum(d_(n/e,3),e odd dividing n).
As in A000176, D stores twice the formula value and removes
the proper odd-divisor contributions in the same sum.
The n=1 tangent-number normalization is twice the formula
value, so `>>1%n` halves every later value and preserves the first.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1000 terms in 60 s; the official b-file contains 1000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000488), CC BY-SA 4.0.
