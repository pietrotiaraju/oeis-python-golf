# A000787

> Strobogrammatic numbers: the same upside down.
> — [OEIS A000787](https://oeis.org/A000787)

Offset 1: 0, 1, 8, 11, 69, 88, 96, 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, …

### Python 3 — 72 bytes

```python
k=0
while 1:s=str(k);k+=1;s==s[::-1].translate('    9 8601'*6)==print(s)
```

**How it works**

- Turning a number upside down reverses its digits and maps 0, 1, 8 to
  themselves and 6 ↔ 9; 2, 3, 4, 5 and 7 have no upside-down digit.
- `str.translate` accepts any table indexed by code point, and a string
  works: `'    9 8601'*6` has period 10, so its characters 48–57 (the code
  points of '0'–'9') are `01    9 86`. The bad digits turn into spaces,
  so a number containing one can never equal its own rotation.
- The chained comparison `s==…==print(s)` only calls `print` when the
  first comparison holds.

**Notes**

- A plain scan of all integers: 674 terms (up to about 1.1·10⁷) in 60 s
  here. Building the numbers from the outside in reaches the whole b-file
  but is longer.
- The b-file has 10000 terms (up to 8.8·10¹⁰); the bar is 510 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 72 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000787), CC BY-SA 4.0.
