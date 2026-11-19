# A002001

> a(n) = 3*4^(n-1), n>0; a(0)=1.
> — [OEIS A002001](https://oeis.org/A002001)

Offset 0: 1, 3, 12, 48, 192, 768, 3072, 12288, 49152, 196608, 786432, …

### Python 3 — 29 bytes

```python
a=1
while[print(a)]:a*=4-1//a
```

**How it works**

- After a(0) = 1 the sequence is 3, 12, 48, …: every step multiplies by 4
  except the first, which multiplies by 3.
- `a*=4-1//a` multiplies by 4 − ⌊1/a⌋. That is 3 when a = 1, which happens
  only at the start, and 4 once a ≥ 3.

**Notes**

- `a*=4-a%3` (3 when a = 1, 4 for the multiples of 3 after it) is the
  same length; `a*=4-(a<2)` is one byte longer.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops the output near n = 7140.
- The b-file has 301 terms (n = 0 to 300); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002001), CC BY-SA 4.0.
