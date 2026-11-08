# A001018

> Powers of 8: a(n) = 8^n.
> — [OEIS A001018](https://oeis.org/A001018)

Offset 0: 1, 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=8
```

**How it works**

- n starts at 8⁰ = 1 and is multiplied by 8 after every print, so the k-th
  print is 8^k. The value is the whole state: no exponent counter.
- `while[print(n)]:` prints in the loop condition: `print` returns `None` and
  the one-element list `[None]` is true. This is
  [A000420](../../A000xxx/A000420/) with 8 in place of 7.

**Notes**

- `while 1:print(n);n*=8` is 25 bytes, a counter with `print(8**n)` is 27 and
  `n<<=3` in place of `n*=8` is 25.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s.
- a(n) has ⌊n·log₁₀ 8⌋ + 1 digits, so a(4762) is the first term with more than
  4300 digits (4301) and Python's int-to-str limit stops the printing there;
  a(4761) has 4300.
- The same loop with another base: [A000079](../../A000xxx/A000079/) 2ⁿ,
  [A000244](../../A000xxx/A000244/) 3ⁿ, [A000302](../../A000xxx/A000302/) 4ⁿ,
  [A000351](../../A000xxx/A000351/) 5ⁿ, [A000400](../../A000xxx/A000400/) 6ⁿ,
  [A000420](../../A000xxx/A000420/) 7ⁿ, [A001019](../A001019/) 9ⁿ,
  [A001020](../A001020/) 11ⁿ, [A001021](../A001021/) 12ⁿ,
  [A001022](../A001022/) 13ⁿ, [A001023](../A001023/) 14ⁿ,
  [A001024](../A001024/) 15ⁿ, [A001025](../A001025/) 16ⁿ.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001018), CC BY-SA 4.0.
