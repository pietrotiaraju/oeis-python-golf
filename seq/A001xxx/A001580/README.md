# A001580

> a(n) = 2^n + n^2.
> — [OEIS A001580](https://oeis.org/A001580)

Offset 0: 1, 3, 8, 17, 32, 57, 100, 177, 320, 593, 1124, 2169, 4240, 8361, …

### Python 3 — 31 bytes

```python
n=0
while[print(2**n+n*n)]:n+=1
```

**How it works**

- The definition, written out: `2**n+n*n` is 2ⁿ + n² for n = 0, 1, 2, ….
  (`n*n` is a byte under `n**2`.)
- At n = 0 Python gives `2**0` = 1 and `0*0` = 0, so a(0) = 1 as in the
  OEIS data.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- `1<<n|n*n`, the same length, is wrong: `|` adds only when the bits are
  disjoint, and for n = 2 it gives 4 | 4 = 4 instead of 8. The shift
  with a sum, `(1<<n)+n*n`, is 2 bytes longer.
- Exact integers, so every term is right; a(14285) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 1001 terms (a(0) to a(1000)); the bar is the whole b-file in
  60 s, which prints instantly.
- The family kⁿ + nᵏ: [A001580](../A001580/), [A001585](../A001585/), [A001589](../A001589/), [A001593](../A001593/), [A001594](../A001594/), [A001596](../A001596/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001580), CC BY-SA 4.0.
