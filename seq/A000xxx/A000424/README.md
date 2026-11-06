# A000424

> Differences of reciprocals of unity.
> — [OEIS A000424](https://oeis.org/A000424)

Offset 1: 7, 85, 1660, 48076, 1942416, 104587344, 7245893376, 628308907776, 66687811660800, 8506654697548800, …

### Python 3 — 86 bytes

```python
a=0;b=1;c=7;n=1
while[print(c)]:n+=1;a,b,c=b,c,(3*n*n+3*n+1)*c-3*n**4*b+((n-1)*n)**3*a
```

**How it works**

- Use the third-order recurrence attributed to Kotesovec on the OEIS
  page, with the auxiliary initial values a(−1)=0 and a(0)=1:

  a(n)=(3n²+3n+1)a(n−1)−3n⁴a(n−2)+(n−1)³n³a(n−3).

- When the condition prints, `a,b,c` hold a(n−2), a(n−1), a(n).
  Thus the initial `a=0;b=1;c=7;n=1` supplies the first output
  a(1)=7, while retaining the two values needed for the recurrence.
- Increment n before evaluating the new term. The simultaneous
  assignment then shifts the old b and c to the first two positions
  and computes the new c using all three old values.
- At n=2 the update is 19·7−48·1+8·0=85; at n=3 it is
  37·85−243·7+216·1=1660. These checks also locate the index
  of the recurrence relative to the printed term.

**Notes**

- Exact integer arithmetic: the recurrence has polynomial integer
  coefficients and requires no rational intermediates or rounding.
  Only three sequence values and the counter are retained.
- `((n-1)*n)**3` is (n−1)³n³; cubing the product avoids writing
  both cubes separately. `[print(c)]` makes the print serve as the
  always-true loop condition.
- The sequence grows beyond the short b-file. Python 3.11+ eventually
  reaches its default 4300-digit integer-to-string limit, which is an
  interpreter limit and does not change the recurrence's correctness.
- The b-file has 16 terms (indices 1 through 16). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000424), CC BY-SA 4.0.
