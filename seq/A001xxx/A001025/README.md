# A001025

> Powers of 16: a(n) = 16^n.
> — [OEIS A001025](https://oeis.org/A001025)

Offset 0: 1, 16, 256, 4096, 65536, 1048576, 16777216, 268435456, 4294967296, 68719476736, …

### Python 3 — 25 bytes

```python
n=1
while[print(n)]:n*=16
```

**How it works**

- n starts at 16⁰ = 1 and is multiplied by 16 after every print, so the k-th
  print is 16^k. The value is the whole state: no exponent counter.
- `while[print(n)]:` prints in the loop condition: `print` returns `None` and
  the one-element list `[None]` is true. This is [A001024](../A001024/) with
  16 in place of 15.

**Notes**

- `while 1:print(n);n*=16` is 26 bytes, a counter with `print(16**n)` is 28
  and `n<<=4` in place of `n*=16` is 25 (a tie).
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 821 terms (up to a(820)); the bar is the whole b-file in
  60 s.
- a(n) has ⌊n·log₁₀ 16⌋ + 1 digits, so a(3572) is the first term with more
  than 4300 digits (4302) and Python's int-to-str limit stops the printing
  there; a(3571) has 4300.
- The same loop with another base: [A000079](../../A000xxx/A000079/) 2ⁿ,
  [A000244](../../A000xxx/A000244/) 3ⁿ, [A000302](../../A000xxx/A000302/) 4ⁿ,
  [A000351](../../A000xxx/A000351/) 5ⁿ, [A000400](../../A000xxx/A000400/) 6ⁿ,
  [A000420](../../A000xxx/A000420/) 7ⁿ, [A001018](../A001018/) 8ⁿ,
  [A001019](../A001019/) 9ⁿ, [A001020](../A001020/) 11ⁿ,
  [A001021](../A001021/) 12ⁿ, [A001022](../A001022/) 13ⁿ,
  [A001023](../A001023/) 14ⁿ, [A001024](../A001024/) 15ⁿ.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 25 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001025), CC BY-SA 4.0.
