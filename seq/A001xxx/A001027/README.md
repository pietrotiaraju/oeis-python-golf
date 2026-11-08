# A001027

> Powers of 18: a(n) = 18^n.
> — [OEIS A001027](https://oeis.org/A001027)

Offset 0: 1, 18, 324, 5832, 104976, 1889568, 34012224, 612220032, 11019960576, 198359290368, …

### Python 3 — 25 bytes

```python
n=1
while[print(n)]:n*=18
```

**How it works**

- n starts at 18⁰ = 1 and is multiplied by 18 after every print, so the k-th
  print is 18^k. The value is the whole state: no exponent counter.
- `while[print(n)]:` prints in the loop condition: `print` returns `None` and
  the one-element list `[None]` is true. This is [A001026](../A001026/) with
  18 in place of 17.

**Notes**

- `while 1:print(n);n*=18` is 26 bytes and a counter with `print(18**n)` is
  28.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s.
- a(n) has ⌊n·log₁₀ 18⌋ + 1 digits, so a(3426) is the first term with more
  than 4300 digits (4301) and Python's int-to-str limit stops the printing
  there; a(3425) has 4300.
- The same loop with another base: [A000079](../../A000xxx/A000079/) 2ⁿ,
  [A000244](../../A000xxx/A000244/) 3ⁿ, [A000302](../../A000xxx/A000302/) 4ⁿ,
  [A000351](../../A000xxx/A000351/) 5ⁿ, [A000400](../../A000xxx/A000400/) 6ⁿ,
  [A000420](../../A000xxx/A000420/) 7ⁿ, [A001018](../A001018/) 8ⁿ,
  [A001019](../A001019/) 9ⁿ, [A001020](../A001020/) 11ⁿ,
  [A001021](../A001021/) 12ⁿ, [A001022](../A001022/) 13ⁿ,
  [A001023](../A001023/) 14ⁿ, [A001024](../A001024/) 15ⁿ,
  [A001025](../A001025/) 16ⁿ, [A001026](../A001026/) 17ⁿ,
  [A001029](../A001029/) 19ⁿ.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 25 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001027), CC BY-SA 4.0.
