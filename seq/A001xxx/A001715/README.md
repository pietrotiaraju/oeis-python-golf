# A001715

> a(n) = n!/6.
> — [OEIS A001715](https://oeis.org/A001715)

Offset 3: 1, 4, 20, 120, 840, 6720, 60480, 604800, 6652800, 79833600, 1037836800, …

### Python 3 — 33 bytes

```python
a=1;n=4
while[print(a)]:a*=n;n+=1
```

**How it works**

- a(n) = n!/6 = (k + 1)(k + 2)···n with k = 3, an empty product 1 at the
  offset n = 3.
- `a` starts at a(3) = 1 and `n` at 4; each pass prints a and
  multiplies it by the next factor, `a*=n;n+=1`.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- `a=n=1` with `a*=n+3;n+=1` ties at 33 bytes.
- Exact integers, so every term is right; a(1559) is the first term
  over 4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 198 terms (a(3) to a(200)), kept as
  downloaded (with its leading spaces); the bar is the whole b-file in 60 s,
  which prints instantly.
- Factorial quotients: [A001710](../A001710/) (n!/2), [A001715](../A001715/) (n!/6), [A001720](../A001720/) (n!/24), [A001725](../A001725/) (n!/5!), [A001730](../A001730/) (n!/6!).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001715), CC BY-SA 4.0.
