# A000466

> a(n) = 4*n^2 - 1.
> — [OEIS A000466](https://oeis.org/A000466)

Offset 0: -1, 3, 15, 35, 63, 99, 143, 195, 255, 323, …

### Python 3 — 31 bytes

```python
n=0
while 1:print(4*n*n-1);n+=1
```

**How it works**

- The loop substitutes n=0,1,2,… directly into 4n²−1.
  Starting at zero supplies the exceptional negative first value −1;
  incrementing afterwards gives 3,15,35,… .
- Factoring gives (2n−1)(2n+1), the product of two consecutive odd
  integers. Expanding it as `4*n*n-1` avoids storing both factors
  or adding parentheses around them.
- The first difference is a(n+1)−a(n)=8n+4, and the second
  difference is 8. These identities explain the quadratic growth,
  but the program needs only the defining polynomial and its counter.

**Notes**

- Exact integer arithmetic at every index. Python integers grow as
  needed, so there is no fixed-width overflow or square-root test.
- Apart from the initial −1, every term is positive and odd.
  For example a(3)=4·9−1=35=5·7.
- A finite-difference loop would need both a running value and a
  running increment. Direct evaluation retains just n and keeps
  the implementation short.
- [A000447](../A000447/) uses n(4n²−1)/3 for partial sums of
  odd squares, a related polynomial with different output values.
- The b-file has 901 terms (indices 0 through 900). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000466), CC BY-SA 4.0.
