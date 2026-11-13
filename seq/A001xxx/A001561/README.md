# A001561

> a(n) = (7*n+3)*(7*n+5)*(7*n+6).
> — [OEIS A001561](https://oeis.org/A001561)

Offset 0: 90, 1560, 6460, 16848, 34782, 62320, 101520, 154440, 223138, …

### Python 3 — 33 bytes

```python
n=5
while[print(n*~n*(2-n))]:n+=7
```

**How it works**

- With m = 7n + 5 the factors are m − 2, m and m + 1, so
  a(n) = (m − 2)m(m + 1). The counter `n` holds m: it starts at 5 and steps
  by 7.
- `~n` is −m − 1 (bitwise not), so `n*~n` is −m(m + 1), and the third factor
  is written 2 − m instead of m − 2 to cancel the sign: `n*~n*(2-n)` is
  10 characters, where `n*-~n*(n-2)` needs 11.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- The offsets 3, 5, 6 are not symmetric, so there is no m³ − cm form as in
  [A001505](../A001505/). Other middles cost more: m = 7n + 6 gives
  `n*~-n*(n-3)` (34 bytes in all), m = 7n + 4 gives `(n*n-1)*(n+2)` (36);
  the expanded `n**3-n*n-2*n` is 35.
- The same sign trick on [A001547](../A001547/)'s (m − 1)m(m + 2) needs a
  falling counter, `n=-2` / `while[print(n*~n*(n-2))]:n-=7`, and only ties its
  34 bytes.
- Exact integers, so every term is right.
- The b-file has 1001 terms (n = 0 to 1000) and all of them print at once; the
  bar is the whole b-file in 60 s.
- Products of terms of one progression: [A001505](../A001505/),
  [A001509](../A001509/), [A001512](../A001512/), [A001520](../A001520/),
  [A001546](../A001546/), [A001547](../A001547/), [A001561](../A001561/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001561), CC BY-SA 4.0.
