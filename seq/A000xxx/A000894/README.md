# A000894

> a(n) = (2*n)!*(2*n+1)! / ((n+1)! * n!^3).
> — [OEIS A000894](https://oeis.org/A000894)

Offset 0: 1, 6, 60, 700, 8820, 116424, 1585584, 22084920, 312869700, …

### Python 3 — 45 bytes

```python
b=n=1
while[print(b*(b:=4*b-2*b//n)//2)]:n+=1
```

**How it works**

- a(n) = C(2n,n)·C(2n+1,n) (an OEIS formula), and C(2n+1,n) =
  C(2n+2,n+1)/2, so a(n) is the product of two consecutive central
  binomial coefficients, halved.
- `b` is C(2k,k) with k = n − 1 the index (the counter `n` runs one ahead).
  In `b*(b:=4*b-2*b//n)` the left `b` is read before the walrus, so the
  product is C(2k,k)·C(2k+2,k+1), and `//2` gives a(k); the walrus has
  already moved `b` on for the next term.
- Next binomial: C(2k+2,k+1) = C(2k,k)·(4k+2)/(k+1) = 4b − 2b/n, where
  2b/n = 2·C(2k,k)/(k+1) is twice a Catalan number, so `//n` is exact.
- The ratio form n(n+1)a(n) = 4(2n−1)(2n+1)a(n−1) (R. J. Mathar) is longer:
  `a=m=1` / `while[print(a)]:m+=2;a=a*16*m*(m-2)//(m*m-1)` is 50 bytes.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 181 terms (up to a(180)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 3575, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000894), CC BY-SA 4.0.
