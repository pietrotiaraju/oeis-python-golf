# A000489

> Card matching: Coefficients B[n,3] of t^3 in the reduced hit polynomial A\[n,n,n\](t).
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

- Let B_n be the Baxter number
  [A001181](https://oeis.org/A001181), with B_0=B_1=1.
  Van Hoeij's identity on the OEIS page gives this card-matching
  coefficient as

  a(n)=n²·((27n³+54n²−57n+8)(n+2)B_n
  −(189n³+189n²−30n+16)(n−1)B_(n−1))/96.

- At the print, `a,b` hold B_(n−1), B_n. Substituting them
  into that identity produces the output without computing the
  whole reduced hit polynomial.
- After increasing n, advance the Baxter pair with
  (n+2)(n+3)B_n=(7n²+7n−2)B_(n−1)
  +8(n−1)(n−2)B_(n−2).
  The simultaneous assignment keeps both old values available.
- At n=1 the second part of the output numerator vanishes and
  the first is 32·3·1=96, giving a(1)=1. The pair then advances
  to B_1=1, B_2=2 and produces a(2)=16.

**Notes**

- Both divisions are exact: the first identity expresses an integer
  card-matching coefficient, and the second is the Baxter recurrence.
  Numerators must be assembled before division, since their individual
  contributions need not have the required divisibility.
- Only two auxiliary sequence values and the index are retained.
  The direct recurrence for this sequence on the OEIS page has much
  higher-degree polynomial coefficients; the Baxter representation
  keeps the implementation shorter.
- Exact integers throughout. Exponential growth eventually meets
  Python 3.11+'s default 4300-digit output conversion limit,
  an interpreter limit.
- The b-file has 100 terms (indices 1 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 162 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000489), CC BY-SA 4.0.
