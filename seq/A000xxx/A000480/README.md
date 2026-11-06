# A000480

> a(n) = floor(cos(n)).
> — [OEIS A000480](https://oeis.org/A000480)

Offset 0: 1, 0, -1, -1, -1, 0, 0, 0, -1, -1, …

### Python 3 — 225 bytes

```python
n=S=1
print(1)
while 1:
 S*=2;K=S.bit_length();E=20*K+20
 p=sum((-1)**k*S*16//((2*k+1)*5**(2*k+1))-(-1)**k*S*4//((2*k+1)*239**(2*k+1))for k in range(K))
 while p>E and(q:=2*n*S//(p+E))==2*n*S//(p-E):print(-(q%4 in(1,2)));n+=1
```

**How it works**

Use Machin's identity π=16*atan(1/5)-4*atan(1/239).
At scale S, take K alternating-series terms for each arctangent.
The two integer divisions per term contribute less than 2K total
rounding error, and the two omitted tails contribute less than 1
because K=S.bit_length(). The deliberately larger E=20K+20
therefore guarantees p-E < S*π < p+E.
For the needed multiple c*n/π, compute its integer part using both
endpoints. Output only when the two integer quotients agree.
Otherwise double S and recompute the bounds. For n>0 this quotient
never lies on an integer boundary, by irrationality of π, so every
term eventually resolves. Quadrant or sector membership determines
the exact requested rounded trigonometric value.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 80 terms in 60 s; the official b-file contains 80 terms.
- No floating-point approximation or fixed precision is used. For A000480, cos(0)=1 is printed separately because all later cosine floors are 0 or -1.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 225 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000480), CC BY-SA 4.0.
