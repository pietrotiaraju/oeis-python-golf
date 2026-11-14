# A001725

> a(n) = n!/5!.
> — [OEIS A001725](https://oeis.org/A001725)

Offset 5: 1, 6, 42, 336, 3024, 30240, 332640, 3991680, 51891840, 726485760, …

### Python 3 — 33 bytes

```python
a=1;n=6
while[print(a)]:a*=n;n+=1
```

**How it works**

- a(n) = n!/120 = (k + 1)(k + 2)···n with k = 5, an empty product 1 at the
  offset n = 5.
- `a` starts at a(5) = 1 and `n` at 6; each pass prints a and
  multiplies it by the next factor, `a*=n;n+=1`.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- `a=n=1` with `a*=n+5;n+=1` ties at 33 bytes.
- Exact integers, so every term is right; a(1559) is the first term
  over 4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 296 terms (a(5) to a(300)), kept as
  downloaded (with its leading spaces); the bar is the whole b-file in 60 s,
  which prints instantly.
- Factorial quotients: [A001710](../A001710/) (n!/2), [A001715](../A001715/) (n!/6), [A001720](../A001720/) (n!/24), [A001725](../A001725/) (n!/5!), [A001730](../A001730/) (n!/6!).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001725), CC BY-SA 4.0.
