# A001585

> a(n) = 3^n + n^3.
> — [OEIS A001585](https://oeis.org/A001585)

Offset 0: 1, 4, 17, 54, 145, 368, 945, 2530, 7073, 20412, 60049, 178478, …

### Python 3 — 32 bytes

```python
n=0
while[print(3**n+n**3)]:n+=1
```

**How it works**

- The definition, written out: `3**n+n**3` is 3ⁿ + n³ for n = 0, 1, 2, ….
- At n = 0 Python gives `3**0` = 1 and `0**3` = 0, so a(0) = 1 as in the
  OEIS data.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Exact integers, so every term is right; a(9013) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 1001 terms (a(0) to a(1000)); the bar is the whole b-file in
  60 s, which prints instantly.
- The family kⁿ + nᵏ: [A001580](../A001580/), [A001585](../A001585/), [A001589](../A001589/), [A001593](../A001593/), [A001594](../A001594/), [A001596](../A001596/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001585), CC BY-SA 4.0.
