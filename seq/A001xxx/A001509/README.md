# A001509

> a(n) = (5*n + 1)*(5*n + 2)*(5*n + 3).
> — [OEIS A001509](https://oeis.org/A001509)

Offset 0: 6, 336, 1716, 4896, 10626, 19656, 32736, 50616, 74046, 103776, …

### Python 3 — 29 bytes

```python
n=2
while[print(n**3-n)]:n+=5
```

**How it works**

- With m = 5n + 2, the middle factor, the factors are m − 1, m and m + 1,
  so a(n) = (m − 1)m(m + 1) = m³ − m. The counter `n` holds m: it starts at
  2 and steps by 5, and `n**3-n` is printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- `n*~-n**2` (`~-x` is x − 1, and `**` binds before the unary operators) is
  2 bytes longer, the product `~-n*n*-~n` 3. The expanded cubic in a plain
  counter costs far more.
- A search over every polynomial expression E of up to 9 characters (n,
  constants up to 99, `+ - * **`, unary `-` and `~`, and a final `//` or `>>`)
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
| 2026-11-10 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001509), CC BY-SA 4.0.
