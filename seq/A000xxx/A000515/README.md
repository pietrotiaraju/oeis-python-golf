# A000515

> a(n) = (2n)!(2n+1)!/n!^4, or equally (2n+1)*binomial(2n,n)^2.
> — [OEIS A000515](https://oeis.org/A000515)

Offset 0: 1, 12, 180, 2800, 44100, 698544, 11099088, 176679360, 2815827300, 44914183600, …

### Python 3 — 51 bytes

```python
n=0;a=1
while[print(a)]:n+=1;a=a*4*(4*n*n-1)//(n*n)
```

**How it works**

- From a(n)=(2n+1)·C(2n,n)², consecutive terms satisfy
  a(n)/a(n−1)=4(2n−1)(2n+1)/n².
- The program starts with a(0)=1, prints it in the always-true one-item
  list condition, then increments n and applies that ratio.
- Multiplication precedes division, so all cancellations happen exactly
  in integer arithmetic.

**Notes**

- One sequence value and its index are sufficient; factorials and
  binomial coefficients need not be recomputed.
- Python's integer conversion limit eventually applies.
- The reference file contains 101 terms from the OEIS b-file; the verification
  bar is 101 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000515), CC BY-SA 4.0.
