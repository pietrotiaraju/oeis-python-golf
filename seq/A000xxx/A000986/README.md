# A000986

> Number of n X n symmetric matrices with (0,1) entries and all row sums 2.
> — [OEIS A000986](https://oeis.org/A000986)

Offset 0: 1, 0, 1, 4, 18, 112, 820, 6912, 66178, 708256, 8372754, 108306280, …

### Python 3 — 75 bytes

```python
a=b=c=m=0;d=1
while[print(d)]:m+=1;a,b,c,d=m*b,m*c,m*d,2*~-m*d-(m-3)*c-a//2
```

**How it works**

- E.g.f. G(x) = (1−x)^(−1/2) exp(−x − x²/4 + x/(2(1−x))) (in the entry;
  the off-diagonal part is a simple graph with all degrees 1 or 2, and it
  forces the diagonal). Its logarithmic derivative gives
  2(1−x)²G′ = (2x − x³)G, so

  a(n+1) = 2n·a(n) − n(n−2)a(n−1) − n(n−1)(n−2)a(n−3)/2

  (Kotesovec's recurrence in the entry, shifted).
- The states are kept factorial-scaled: `d` = a(n), `c` = n·a(n−1),
  `b` = n(n−1)a(n−2), `a` = n(n−1)(n−2)a(n−3). With `m` = n+1 the recurrence
  is a(m) = 2(m−1)d − (m−3)c − a/2, and the next states are just `m*b`,
  `m*c`, `m*d`. `b` is not in the formula; it only carries the value two
  steps on into `a`. `a` holds a product of three consecutive integers, so
  `-a//2` is exact.
- Starting at n = 0 with `d` = 1 and the rest 0 is exact: every scaled
  state of index 0 is 0.

**Notes**

- Exact integer arithmetic; it rests on the e.g.f. above.
- The unscaled recurrence, `a,b,c,d=b,c,d,(4*d-(m-2)*(2*c+~-m*a))*m>>1`,
  is 77 bytes. Running (1−x)^(−3/2)·exp(…) and printing `d-c`, as on
  [A000985](../A000985/), is longer here.
- The program stops at Python's 4300-digit `int`-to-`str` limit after
  1552 terms (well under a second); the b-file has 446 terms and the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000986), CC BY-SA 4.0.
