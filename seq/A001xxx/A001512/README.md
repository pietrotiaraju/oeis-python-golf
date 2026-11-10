# A001512

> a(n) = (5*n+1)*(5*n+2)*(5*n+3)*(5*n+4).
> — [OEIS A001512](https://oeis.org/A001512)

Offset 0: 24, 3024, 24024, 93024, 255024, 570024, 1113024, 1974024, 3258024, …

### Python 3 — 36 bytes

```python
n=2
while[print(~-(n*~n+1)**2)]:n+=5
```

**How it works**

- With m = 5n + 2 the factors are m − 1, m, m + 1, m + 2. Pair the outer and
  the inner ones: (m − 1)(m + 2) = m² + m − 2 and m(m + 1) = m² + m, so with
  t = m² + m − 1, a(n) = (t − 1)(t + 1) = t² − 1.
- `n*~n` is −m(m + 1), so `n*~n+1` is −t, and its square is t². `~-x**2` is
  x² − 1: `**` binds before the unary `-` and `~`, and `~-y` is y − 1.
- The counter `n` holds m: it starts at 2 and steps by 5.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- `(n*n+n-1)**2-1` is 1 byte longer. The doubled counter x = 10n + 5 gives
  a(n) = (x² − 9)(x² − 1)/16 = ((x² − 5)/4)² − 1, `~-(n*n-5>>2)**2` (step 10),
  3 bytes longer, and so is a running t (`t=5;d=50`, `t+=d;d+=50`).
- A search over every polynomial expression E of up to 12 characters (n,
  constants up to 16, `+ - * **`, unary `-` and `~`, and a final `//` or `>>`)
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
| 2026-11-10 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001512), CC BY-SA 4.0.
