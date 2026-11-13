# A001566

> a(0) = 3; thereafter, a(n) = a(n-1)^2 - 2.
> — [OEIS A001566](https://oeis.org/A001566)

Offset 0: 3, 7, 47, 2207, 4870847, 23725150497407, …

### Python 3 — 27 bytes

```python
a=3
while[print(a)]:a=a*a-2
```

**How it works**

- The definition itself: `a` starts at a(0) = 3 and `a=a*a-2` is the
  recurrence a(n) = a(n−1)² − 2.

**Notes**

- a(n) = L(2ⁿ⁺¹) = φ^(2ⁿ⁺¹) + φ^(−2ⁿ⁺¹), the Lucas numbers at powers of 2,
  since L(2m) = L(m)² − 2 for even m; so a(n) has about 0.42·2ⁿ digits.
- Exact integer arithmetic, so the program is right for every n. a(13) has
  3425 digits; a(14) has 6849, past Python's 4300-digit int-to-str limit, so
  the program stops there with a ValueError after 14 terms.
- The b-file has 13 terms (a(0) to a(12)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001566), CC BY-SA 4.0.
