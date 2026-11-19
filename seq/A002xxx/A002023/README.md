# A002023

> a(n) = 6*4^n.
> — [OEIS A002023](https://oeis.org/A002023)

Offset 0: 6, 24, 96, 384, 1536, 6144, 24576, 98304, 393216, 1572864, …

### Python 3 — 24 bytes

```python
a=6
while[print(a)]:a*=4
```

**How it works**

- `a*=4` from a = 6, printing before each step.

**Notes**

- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops the output near n = 7140.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002023), CC BY-SA 4.0.
