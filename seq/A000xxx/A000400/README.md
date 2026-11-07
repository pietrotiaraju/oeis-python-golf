# A000400

> Powers of 6: a(n) = 6^n.
> — [OEIS A000400](https://oeis.org/A000400)

Offset 0: 1, 6, 36, 216, 1296, 7776, 46656, 279936, 1679616, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=6
```

**How it works**

- `n` holds 6ⁿ: it starts at 6⁰ = 1 and the loop body multiplies it by 6.
- `print(n)` sits in the loop condition. It returns `None`, and `[None]` is
  a non-empty list, so the condition is always true and the loop never
  ends. It is the [A000079](../A000079/) and [A000244](../A000244/) loop
  with `n*=6`.

**Notes**

- `n=1` with `while 1:print(n);n*=6` is 25 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s. Here the program prints every term it can in about 1.5 s.
- a(n) has ⌊n·log₁₀ 6⌋ + 1 digits, so a(5526) is the first term with more
  than 4300 digits and printing stops there with Python's int-to-str
  `ValueError`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000400), CC BY-SA 4.0.
