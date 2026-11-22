# A002173

> a(n) = Sum_{d|n, d == 1 mod 4} d^2 - Sum_{d|n, d == 3 mod 4} d^2.
> — [OEIS A002173](https://oeis.org/A002173)

Offset 1: 1, 1, -8, 1, 26, -8, -48, 1, 73, 26, -120, -8, …

### Python 3 — 70 bytes

```python
n=1
while[print(sum(d*d*(2-d%4)for d in range(1,n+1,2)if n%d<1))]:n+=1
```

**How it works**

- With χ the non-principal character modulo 4 (χ(d) = 1 for d ≡ 1,
  −1 for d ≡ 3 and 0 for even d), a(n) = Σ_(d|n) χ(d)·d², which is the
  definition read as one sum.
- `range(1,n+1,2)` walks the odd d ≤ n only, since even divisors
  contribute nothing. For odd d, d mod 4 is 1 or 3, so `2-d%4` is
  exactly χ(d).
- `while[print(…)]:n+=1` prints a(n) and moves on: a one-element list is
  always true, so the loop never ends.

**Notes**

- Exact integer arithmetic, right for every n.
- Each term costs n/2 divisibility tests; the whole b-file (10000 terms)
  takes a few seconds, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002173), CC BY-SA 4.0.
