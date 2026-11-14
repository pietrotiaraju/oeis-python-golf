# A001730

> a(n) = n!/6!.
> — [OEIS A001730](https://oeis.org/A001730)

Offset 6: 1, 7, 56, 504, 5040, 55440, 665280, 8648640, 121080960, 1816214400, …

### Python 3 — 33 bytes

```python
a=1;n=7
while[print(a)]:a*=n;n+=1
```

**How it works**

- a(n) = n!/720 = (k + 1)(k + 2)···n with k = 6, an empty product 1 at the
  offset n = 6.
- `a` starts at a(6) = 1 and `n` at 7; each pass prints a and
  multiplies it by the next factor, `a*=n;n+=1`.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- `a=n=1` with `a*=n+6;n+=1` ties at 33 bytes.
- Exact integers, so every term is right; a(1560) is the first term
  over 4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 295 terms (a(6) to a(300)), kept as
  downloaded (with its leading spaces); the bar is the whole b-file in 60 s,
  which prints instantly.
- Factorial quotients: [A001710](../A001710/) (n!/2), [A001715](../A001715/) (n!/6), [A001720](../A001720/) (n!/24), [A001725](../A001725/) (n!/5!), [A001730](../A001730/) (n!/6!).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001730), CC BY-SA 4.0.
