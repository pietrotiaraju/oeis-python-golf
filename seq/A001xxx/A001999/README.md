# A001999

> a(n) = a(n-1)*(a(n-1)^2 - 3).
> — [OEIS A001999](https://oeis.org/A001999)

Offset 0: 3, 18, 5778, 192900153618, 7177905237579946589743592924684178, …

### Python 3 — 28 bytes

```python
a=3
while[print(a)]:a*=a*a-3
```

**How it works**

- The recurrence itself: `a*=a*a-3` replaces a(n − 1) by
  a(n − 1)(a(n − 1)² − 3), from a(0) = 3.
- Exact integer arithmetic, so the program is right for every n. The
  number of digits triples each step: a(7) has 915 digits, a(8) 2745, and
  printing a(9) (8235 digits) stops the program at Python's 4300-digit
  int-to-str limit.

**Notes**

- a(n) = L(2·3ⁿ), a Lucas number: x³ − 3x is how L(2k) becomes L(6k).
- The b-file has 8 terms (n = 0 to 7); the bar is the whole b-file in 60 s,
  which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001999), CC BY-SA 4.0.
