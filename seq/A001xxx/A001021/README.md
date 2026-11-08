# A001021

> Powers of 12: a(n) = 12^n.
> — [OEIS A001021](https://oeis.org/A001021)

Offset 0: 1, 12, 144, 1728, 20736, 248832, 2985984, 35831808, 429981696, 5159780352, …

### Python 3 — 25 bytes

```python
n=1
while[print(n)]:n*=12
```

**How it works**

- n starts at 12⁰ = 1 and is multiplied by 12 after every print, so the k-th
  print is 12^k. The value is the whole state: no exponent counter.
- `while[print(n)]:` prints in the loop condition: `print` returns `None` and
  the one-element list `[None]` is true. This is [A001020](../A001020/) with
  12 in place of 11.

**Notes**

- `while 1:print(n);n*=12` is 26 bytes and a counter with `print(12**n)` is
  28.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s.
- a(n) has ⌊n·log₁₀ 12⌋ + 1 digits, so a(3985) is the first term with more
  than 4300 digits (4301) and Python's int-to-str limit stops the printing
  there; a(3984) has 4300.
- The same loop with another base: [A000079](../../A000xxx/A000079/) 2ⁿ,
  [A000244](../../A000xxx/A000244/) 3ⁿ, [A000302](../../A000xxx/A000302/) 4ⁿ,
  [A000351](../../A000xxx/A000351/) 5ⁿ, [A000400](../../A000xxx/A000400/) 6ⁿ,
  [A000420](../../A000xxx/A000420/) 7ⁿ, [A001018](../A001018/) 8ⁿ,
  [A001019](../A001019/) 9ⁿ, [A001020](../A001020/) 11ⁿ,
  [A001022](../A001022/) 13ⁿ, [A001023](../A001023/) 14ⁿ,
  [A001024](../A001024/) 15ⁿ, [A001025](../A001025/) 16ⁿ.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 25 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001021), CC BY-SA 4.0.
