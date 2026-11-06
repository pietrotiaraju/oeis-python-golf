# A000457

> Exponential generating function: (1+3*x)/(1-2*x)^(7/2).
> — [OEIS A000457](https://oeis.org/A000457)

Offset 0: 1, 10, 105, 1260, 17325, 270270, 4729725, 91891800, 1964187225, 45831035250, …

### Python 3 — 37 bytes

```python
n=a=1
while[print(n*a)]:n+=1;a*=2*n+1
```

**How it works**

The factorial ratio is a(m)=(m+1)*(2m+3)!!/3.
The state n=m+1 and a=(2n+1)!!/3 starts at n=a=1.
Increment n and multiply a by the next odd factor 2n+1
after each output; the printed product is the required term.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 201 terms in 60 s; the official b-file contains 201 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000457), CC BY-SA 4.0.
