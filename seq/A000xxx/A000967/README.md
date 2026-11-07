# A000967

> Sum of Fermat coefficients.
> — [OEIS A000967](https://oeis.org/A000967)

Offset 1: 1, 2, 4, 8, 18, 40, 91, 210, 492, 1165, 2786, 6710, 16267, 39650, 97108, 238824, 589521, 1459960, 3626213, 9030450, …

### Python 3 — 56 bytes

```python
u,v,m=1,4,3
while[print((v+m//2-1)//m)]:u,v=v,3*v-u;m+=2
```

**How it works**

- Piza's Fermat coefficients are (n:c) = C(2n−c, c−1)/c. With m = 2n+1
  they are the coefficients of the Lucas polynomial divided by m:
  (n:c) = C(m−c, c)/(m−c) = (1/m)·m/(m−c)·C(m−c, c), and Lucas' formula
  Σ_{c=0..n} m/(m−c)·C(m−c, c) = L(m) gives (the c = 0 term is 1)
  Σ_{c=1..n} (n:c) = (L(m) − 1)/m. So a(n) = round((L(2n+1) − 1)/(2n+1)).
- `u,v` are L(m−2), L(m) for odd m, stepped by L(m+2) = 3L(m) − L(m−2).
- m is odd, so k/m is never a half-integer and
  round(k/m) = ⌊(k + (m−1)/2)/m⌋: `(v+m//2-1)//m`.

**Notes**

- Exact integer arithmetic; the only fact used is Lucas' formula above. The
  closed form was also checked against the defining sum of Fractions for
  n ≤ 200.
- The b-file has 1000 terms and all of them print in under 0.1 s; the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000967), CC BY-SA 4.0.
