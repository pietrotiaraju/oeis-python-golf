# A000471

> a(n) = floor(sinh(n)).
> — [OEIS A000471](https://oeis.org/A000471)

Offset 0: 0, 1, 3, 10, 27, 74, 201, 548, 1490, 4051, …

### Python 3 — 91 bytes

```python
n=0
while 1:
 N=n;F=d=1
 while -N%F<n**d:d+=2;N=N*d*(d-1)+n**d;F*=d*(d-1)
 print(N//F);n+=1
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
- The verification bar is 201 terms in 60 s; the official b-file contains 201 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000471), CC BY-SA 4.0.
