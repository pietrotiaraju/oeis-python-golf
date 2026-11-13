# A001589

> a(n) = 4^n + n^4.
> — [OEIS A001589](https://oeis.org/A001589)

Offset 0: 1, 5, 32, 145, 512, 1649, 5392, 18785, 69632, 268705, 1058576, …

### Python 3 — 32 bytes

```python
n=0
while[print(4**n+n**4)]:n+=1
```

**How it works**

- The definition, written out: `4**n+n**4` is 4ⁿ + n⁴ for n = 0, 1, 2, ….
- At n = 0 Python gives `4**0` = 1 and `0**4` = 0, so a(0) = 1 as in the
  OEIS data.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Exact integers, so every term is right; a(7143) is the first term over
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
Sequences](https://oeis.org/A001589), CC BY-SA 4.0.
