# A001520

> a(n) = (6*n+1)*(6*n+3)*(6*n+5).
> — [OEIS A001520](https://oeis.org/A001520)

Offset 0: 15, 693, 3315, 9177, 19575, 35805, 59163, 90945, 132447, 184965, …

### Python 3 — 31 bytes

```python
n=3
while[print(n**3-4*n)]:n+=6
```

**How it works**

- With m = 6n + 3, the middle factor, the factors are m − 2, m and m + 2,
  so a(n) = (m − 2)m(m + 2) = m³ − 4m. The counter `n` holds m: it starts at
  3 and steps by 6, and `n**3-4*n` is printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- `n*(n*n-4)` is 1 byte longer, and the product `(n-2)*n*(n+2)` 5. The
  expanded cubic in a plain counter costs far more.
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
| 2026-11-10 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001520), CC BY-SA 4.0.
