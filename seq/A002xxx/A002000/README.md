# A002000

> a(n+1) = a(n)*(a(n)^2 - 3) with a(0) = 7.
> — [OEIS A002000](https://oeis.org/A002000)

Offset 0: 7, 322, 33385282, 37210469265847998489922, …

### Python 3 — 28 bytes

```python
a=7
while[print(a)]:a*=a*a-3
```

**How it works**

- Straight from the definition: `a*=a*a-3` turns a(n) into
  a(n)·(a(n)² − 3) = a(n+1), starting from a(0) = 7.
- `while[print(a)]:` prints before each step; `[None]` is a non-empty
  list, so the loop never ends by itself.

**Notes**

- Exact integer arithmetic, so every printed term is right. The number of
  digits triples at each step: a(n) = r^(3ⁿ) + r^(−3ⁿ) with
  r = (7 + √45)/2 (Peter Bala's formula on the OEIS page), so a(n) has
  about 0.836·3ⁿ digits. a(7), with 1829 digits, still prints; a(8) would
  have 5485, past Python's 4300-digit int-to-str limit, so the program
  stops there with a ValueError (an interpreter limit, not a wrong term).
- The b-file has 7 terms (n = 0 to 6); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002000), CC BY-SA 4.0.
