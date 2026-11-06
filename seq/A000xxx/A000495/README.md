# A000495

> Nearest integer to sinh(n).
> — [OEIS A000495](https://oeis.org/A000495)

Offset 0: 0, 1, 4, 10, 27, 74, 202, 548, 1490, 4052, …

### Python 3 — 113 bytes

```python
n=0
while 1:
 N=n;F=d=1
 while -(2*N+F)%(2*F)<2*n**d:d+=2;N=N*d*(d-1)+n**d;F*=d*(d-1)
 print((2*N+F)//(2*F));n+=1
```

**How it works**

Sum sinh(n)=sum(n^d/d!,d positive odd) over a common factorial
denominator: N/F is the partial sum through odd degree d.
The loop extends by two degrees using the multiplier d(d-1).
For d<=2n-1 the last term n^d/d! is at least 1, so the test
cannot stop prematurely. For larger d the remaining tail is
strictly smaller than the last term, since successive term ratios
are less than 1/4. Stop only when the gap to the next rounding
boundary is at least that upper bound for the tail.
For n>0, sinh(n) is transcendental: an algebraic value would make
exp(n) a root of a quadratic with algebraic coefficients. Thus
no boundary equality persists, and the loop terminates for every n.
At n=0 it immediately prints 0.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 251 terms in 60 s; the official b-file contains 251 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000495), CC BY-SA 4.0.
