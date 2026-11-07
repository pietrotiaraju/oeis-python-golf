# A000655

> a(n) = number of letters in a(n-1), a(1) = 1 (in English).
> — [OEIS A000655](https://oeis.org/A000655)

Offset 1: 1, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, …

### Python 3 — 28 bytes

```python
n=1
while[print(n)]:n=3+41%n
```

**How it works**

- a(1) = 1 ("one", 3 letters), then 3 ("three", 5 letters), then 5 ("five",
  4 letters), then 4 ("four", 4 letters), and "four" is a fixed point: the
  sequence is 1, 3, 5, 4, 4, 4, … (W. I. Hurt's formula in the OEIS entry).
- Only the four values 1, 3, 5, 4 ever occur, so the step needs no English
  names: n → 3 + (41 mod n) maps 1 → 3, 3 → 5, 5 → 4 and 4 → 4, because
  41 mod 1, 3, 5, 4 = 0, 2, 1, 1. It was found by a search over short
  expressions.

**Notes**

- The letter counts of "one", "three", "five" and "four" are worked out above
  rather than computed, which is why no other values appear; every term is
  right.
- Shorter than printing the string `'1\n3\n5'` and then 4 forever (31 bytes).
- The b-file has 80 terms; the bar is all 80, printed instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000655), CC BY-SA 4.0.
