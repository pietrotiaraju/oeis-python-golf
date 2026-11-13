# A001593

> a(n) = 5^n + n^5.
> — [OEIS A001593](https://oeis.org/A001593)

Offset 0: 1, 6, 57, 368, 1649, 6250, 23401, 94932, 423393, 2012174, 9865625, …

### Python 3 — 32 bytes

```python
n=0
while[print(5**n+n**5)]:n+=1
```

**How it works**

- The definition, written out: `5**n+n**5` is 5ⁿ + n⁵ for n = 0, 1, 2, ….
- At n = 0 Python gives `5**0` = 1 and `0**5` = 0, so a(0) = 1 as in the
  OEIS data.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Exact integers, so every term is right; a(6152) is the first term over
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
Sequences](https://oeis.org/A001593), CC BY-SA 4.0.
