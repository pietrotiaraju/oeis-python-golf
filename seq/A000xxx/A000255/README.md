# A000255

> a(n) = n*a(n-1) + (n-1)*a(n-2), a(0) = 1, a(1) = 1.
> — [OEIS A000255](https://oeis.org/A000255)

Offset 0: 1, 1, 3, 11, 53, 309, 2119, 16687, 148329, 1468457, …

### Python 3 — 39 bytes

```python
a=n=1
while[print(a//n)]:n+=1;a=a*-~n^1
```

**How it works**

- With D(m) the derangement numbers ([A000166](../A000166/)), a(n) =
  D(n+2)/(n+1). Proof: D(m) = (m−1)·(D(m−1) + D(m−2)), so (n+1) divides
  D(n+2), and c(n) = D(n+2)/(n+1) satisfies c(n) = D(n+1) + D(n) =
  n·c(n−1) + (n−1)·c(n−2), with c(0) = D(2)/1 = 1 and c(1) = D(3)/2 = 1.
  That is the defining recurrence with the same start, so c = a.
- One state is enough, then: `a` holds D(n+2) and `n` holds n + 1, so the
  term is `a//n` (an exact division). The loop starts at D(2) = 1 with
  n = 1, so `a=n=1` covers both.
- D(m) = m·D(m−1) + (−1)^m, and m·D(m−1) always has the parity of m (see
  A000166), so the update is m·D(m−1) xor 1. After `n+=1` the next index
  m = n + 2 is `-~n`, and `*` binds tighter than `^`: `a=a*-~n^1`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (101 terms) prints at once, and all 1558 terms it prints match the
  recurrence; it stops after a(1557), when a(1558) passes the
  4300-digit int-to-str limit of Python 3.11+. The bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000255), CC BY-SA 4.0.
