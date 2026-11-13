# A001579

> a(n) = 3^n + 5^n + 6^n.
> — [OEIS A001579](https://oeis.org/A001579)

Offset 0: 3, 14, 70, 368, 2002, 11144, 63010, 360248, 2076802, 12050504, …

### Python 3 — 37 bytes

```python
n=0
while[print(3**n+5**n+6**n)]:n+=1
```

**How it works**

- The definition, written out: `3**n+5**n+6**n` is 3ⁿ + 5ⁿ + 6ⁿ for
  n = 0, 1, 2, …; a(0) = 3.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- The generator `sum(k**n for k in(3,5,6))` is 48 bytes in all, 11 more.
  Keeping the powers in variables does not pay either: three of them cost
  more to start and update than the three `**n`.
- Exact integers, so every term is right; a(5526) is the first term over
  4300 digits (6ⁿ dominates), so Python's int-to-str limit stops the program
  there.
- The b-file has 301 terms (a(0) to a(300)); the bar is the whole b-file in
  60 s, which prints instantly.
- Sums of powers: [A001550](../A001550/) to [A001557](../A001557/),
  [A001576](../A001576/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001579), CC BY-SA 4.0.
