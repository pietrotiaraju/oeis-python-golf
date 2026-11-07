# A000776

> a(n) = n! * (1 + 2*Sum_{k=1..n} 1/k).
> — [OEIS A000776](https://oeis.org/A000776)

Offset 0: 1, 3, 8, 28, 124, 668, 4248, 31176, 259488, 2416032, 24886080, 281004480, …

### Python 3 — 43 bytes

```python
a=f=n=1
while[print(a)]:a=a*n+2*f;f*=n;n+=1
```

**How it works**

- With H_n = 1 + 1/2 + ··· + 1/n, a(n) = n!·(1 + 2H_n), and
  H_n = H_{n−1} + 1/n gives a(n) = n·a(n−1) + 2·(n−1)!, valid from n = 1.
- At the top of each round `a` = a(n−1) and `f` = (n−1)!, so `a=a*n+2*f`
  gives a(n), `f*=n` gives n!, and `n+=1` moves on: the loop of
  [A000254](../A000254/) and [A000774](../A000774/) with the factorial
  counted twice.

**Notes**

- A tie at 43 bytes: keep `f` = 2·(n−1)! instead, `a=n=1;f=2` with
  `a=a*n+f`; the longer start eats the saved `2*`.
- a(n) is also 2·A000774(n) − n!, but printing `2*a-f` costs 4 bytes.
- Exact integer arithmetic, correct for every n.
- The b-file has 251 terms (up to a(250)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 1558, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000776), CC BY-SA 4.0.
