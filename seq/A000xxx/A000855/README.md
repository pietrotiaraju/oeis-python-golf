# A000855

> Final two digits of 2^n.
> — [OEIS A000855](https://oeis.org/A000855)

Offset 0: 1, 2, 4, 8, 16, 32, 64, 28, 56, 12, 24, 48, 96, 92, 84, 68, 36, 72, 44, 88, 76, 52, 4, 8, …

### Python 3 — 28 bytes

```python
n=1
while[print(n%100)]:n*=2
```

**How it works**

- `n` holds 2ⁿ itself, doubled at every step, and `n%100` is its last two
  digits read as a number (2²² = 4194304 gives 4, as in the data). Integers
  are exact, so every term is right.
- `print(…)` runs in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- Keeping only the residue, `n=n*2%100` (2ᵏ⁺¹ mod 100 = 2·(2ᵏ mod 100)
  mod 100), stays fast forever but is 29 bytes: `%100` in the print costs 4
  bytes, while `n=n*2%100` in place of `n*=2` costs 5.
- The sequence has period 20 from a(2) on (the OEIS comment), but a table of
  those 20 values is longer than the whole program.
- The price of the big `n` is speed: step k works on a k-bit number, so the
  program slows down as it goes; it prints about 490,000 terms in 60 s here.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000855), CC BY-SA 4.0.
