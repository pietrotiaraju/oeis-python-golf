# A001546

> a(n) = (8*n+1)*(8*n+3)*(8*n+5)*(8*n+7).
> — [OEIS A001546](https://oeis.org/A001546)

Offset 0: 105, 19305, 156009, 606825, 1666665, 3728745, 7284585, 12924009, …

### Python 3 — 36 bytes

```python
n=4
while[print((n*n-5)**2-16)]:n+=8
```

**How it works**

- With m = 8n + 4 the factors are m − 3, m − 1, m + 1, m + 3, so
  a(n) = (m² − 9)(m² − 1) = (m² − 5)² − 16. The counter `n` holds m: it starts
  at 4 and steps by 8.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- The expanded m⁴ − 10m² + 9, `n**4-10*n*n+9`, ties; `(n*n-9)*(n*n-1)` is
  2 bytes longer.
- A search over every polynomial expression E of up to 12 characters (n,
  constants up to 16, `+ - * **`, unary `-` and `~`, and a final `//` or `>>`)
  in the loop `n=c` / `while[print(E)]:n+=s`, for every start c and step s,
  found nothing shorter.
- Exact integers, so every term is right.
- The b-file has 10001 terms (n = 0 to 10000) and all of them print at once; the
  bar is the whole b-file in 60 s.
- Products of terms of one progression: [A001505](../A001505/),
  [A001509](../A001509/), [A001512](../A001512/), [A001520](../A001520/),
  [A001546](../A001546/), [A001547](../A001547/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001546), CC BY-SA 4.0.
