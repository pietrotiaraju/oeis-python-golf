# A001547

> a(n) = (7*n+1)*(7*n+2)*(7*n+4).
> — [OEIS A001547](https://oeis.org/A001547)

Offset 0: 8, 792, 4320, 12650, 27840, 51948, 87032, 135150, 198360, 278720, …

### Python 3 — 34 bytes

```python
n=2
while[print(n*~-n*(n+2))]:n+=7
```

**How it works**

- With m = 7n + 2 the factors are m − 1, m and m + 2, so
  a(n) = (m − 1)m(m + 2). The counter `n` holds m: it starts at 2 and steps by
  7, and `n*~-n*(n+2)` is printed (`~-n` is n − 1: bitwise not of −n).
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- The offsets 1, 2, 4 are not symmetric (their mean is 7/3), so there is no
  m³ − cm form as in [A001505](../A001505/) or [A001520](../A001520/). The
  expanded m(m² + m − 2), `n*(n*n+n-2)`, ties at 11 characters, and so does
  `n*-~n*(n+3)` from m = 7n + 1; `n**3+n*n-2*n` is 2 bytes longer.
- A search over every polynomial expression E of up to 12 characters (n,
  constants up to 12, `+ - * **`, unary `-` and `~`, and a final `//` or `>>`)
  in the loop `n=c` / `while[print(E)]:n+=s`, for every start c and step s,
  found nothing shorter.
- Exact integers, so every term is right.
- The b-file has 1001 terms (n = 0 to 1000) and all of them print at once; the
  bar is the whole b-file in 60 s.
- Products of terms of one progression: [A001505](../A001505/),
  [A001509](../A001509/), [A001512](../A001512/), [A001520](../A001520/),
  [A001546](../A001546/), [A001547](../A001547/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001547), CC BY-SA 4.0.
