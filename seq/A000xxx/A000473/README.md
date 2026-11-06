# A000473

> Number of genus 0 rooted maps with 5 faces and n vertices.
> — [OEIS A000473](https://oeis.org/A000473)

Offset 4: 14, 386, 5868, 65954, 614404, 5030004, 37460376, 259477218, 1697186964, 10596579708, …

### Python 3 — 104 bytes

```python
from math import*
n=4
while 1:print(comb(n,3)*((4*n*n+14*n+3)*comb(2*n,n)-15*(8*n+3)*4**(n-2))//60);n+=1
```

**How it works**

Put s=sqrt(1-4x). Expanding the OEIS generating function gives
x³*((27-20x-16x²)*(1-4x)^(-11/2)
-(27+20x)*(1-4x)^(-5)). Extract the binomial coefficients
and simplify to
a(n)=C(n,3)*((4n²+14n+3)*C(2n,n)-15*(8n+3)*4^(n-2))/60.
The loop evaluates this closed form starting at n=4.
All divisions are exact because the expression is the coefficient
of the specified integer generating series.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 497 terms in 60 s; the official b-file contains 497 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 104 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000473), CC BY-SA 4.0.
