# A002065

> a(n+1) = a(n)^2 + a(n) + 1.
> — [OEIS A002065](https://oeis.org/A002065)

Offset 0: 0, 1, 3, 13, 183, 33673, 1133904603, 1285739649838492213, …

### Python 3 — 28 bytes

```python
a=0
while[print(a)]:a+=a*a+1
```

**How it works**

- The recurrence a(n+1) = a(n)² + a(n) + 1 from a(0) = 0, written as
  `a+=a*a+1`.

**Notes**

- The number of digits doubles at each step: a(12) has 580 digits, so
  a(15) would have about 4600 and Python's 4300-digit int-to-str limit
  stops the output after a(14) (an interpreter limit, not a wrong term).
- The b-file has 13 terms (n = 0 to 12); the bar is the whole b-file in
  60 s, a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002065), CC BY-SA 4.0.
