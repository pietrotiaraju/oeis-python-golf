# A001716

> Generalized Stirling numbers, [n+5,5]_4.
> — [OEIS A001716](https://oeis.org/A001716)

Offset 0: 1, 9, 74, 638, 5944, 60216, 662640, 7893840, 101378880, 1397759040, 20606463360, 323626665600, …

### Python 3 — 44 bytes

```python
a=0;f=1;c=4
while[print(a:=a*c+f)]:f*=c;c+=1
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). Here r = 4 and K = r + 1, so a(n) is the coefficient of x in
  Pₙ(x) = (x+4)(x+5)⋯(x+n+4), n + 1 factors.
- Multiplying a polynomial P by x + c turns its coefficient of x into
  c·[x]P + P(0) and its constant term into c·P(0). The program keeps a = [x]P
  and f = P(0) for the product so far and starts from the empty product
  (a = 0, f = 1) with c = 4. The walrus in `print` multiplies in x + c and
  prints the new coefficient of x; `f*=c` and `c+=1` finish the step. The
  first print is [x](x+4) = 1 = a(0).

**Notes**

- Exact integer arithmetic, correct for every n. It prints up to a(1554); the next term passes the 4300-digit int-to-str limit of Python 3.11+ and stops it. The whole b-file (101 terms, n = 0 to 100) prints in well under a second; the bar is the whole b-file in 60 s.
- For r = 2 ([A001705](../A001705/)) the loop can start one step earlier with
  a = −1 and `f=c=1`; here that step would need f = 1/3.
- The same template gives [A001705](../A001705/) (r = 2), [A001711](../A001711/) (r = 3), [A001721](../A001721/) (r = 5); [A001717](../A001717/) is the coefficient of
  x² for r = 4.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001716), CC BY-SA 4.0.
