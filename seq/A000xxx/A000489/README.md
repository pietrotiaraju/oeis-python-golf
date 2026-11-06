# A000489

> Card matching: Coefficients B[n,3] of t^3 in the reduced hit polynomial A[n,n,n](t).
> — [OEIS A000489](https://oeis.org/A000489)

Offset 1: 1, 16, 435, 7136, 99350, 1234032, 14219212, 155251840, 1628202762, 16550991200, …

### Python 3 — 162 bytes

```python
a=b=n=1
while 1:
 print(n*n*((27*n**3+54*n*n-57*n+8)*(n+2)*b-(189*n**3+189*n*n-30*n+16)*(n-1)*a)//96)
 n+=1;a,b=b,((7*n*n+7*n-2)*b+8*(n-1)*(n-2)*a)//((n+2)*(n+3))
```

**How it works**

Let B_n be the Baxter number A001181(n). Use van Hoeij's identity
listed by the OEIS for this sequence:
a(n)=n²*((27n³+54n²-57n+8)(n+2)B_n
-(189n³+189n²-30n+16)(n-1)B_(n-1))/96.
Baxter numbers satisfy (n+2)(n+3)B_n=(7n²+7n-2)B_(n-1)
+8(n-1)(n-2)B_(n-2), with B_0=B_1=1.
The state keeps consecutive Baxter numbers and evaluates the
identity before advancing them. All divisions are exact.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 100 terms in 60 s; the official b-file contains 100 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 162 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000489), CC BY-SA 4.0.
