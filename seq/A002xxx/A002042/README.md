# A002042

> a(n) = 7*4^n.
> — [OEIS A002042](https://oeis.org/A002042)

Offset 0: 7, 28, 112, 448, 1792, 7168, 28672, 114688, 458752, 1835008, …

### Python 3 — 24 bytes

```python
a=7
while[print(a)]:a*=4
```

**How it works**

- `a*=4` from a = 7, printing before each step.

**Notes**

- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops the output near n = 7140.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002042), CC BY-SA 4.0.
