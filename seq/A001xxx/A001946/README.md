# A001946

> a(n) = 11*a(n-1) + a(n-2).
> — [OEIS A001946](https://oeis.org/A001946)

Offset 0: 2, 11, 123, 1364, 15127, 167761, 1860498, 20633239, 228826127, 2537720636, …

### Python 3 — 37 bytes

```python
a,b=2,11
while[print(a)]:a,b=b,a+11*b
```

**How it works**

- The plain pair update: `a`, `b` hold a(n), a(n + 1) and step to
  a(n + 1), a(n) + 11a(n + 1).
- The terms are the Lucas numbers L(5n): every sequence with
  x(m + 1) = x(m) + x(m − 1) has x(m + 5) = L(5)x(m) + x(m − 5), and
  L(0) = 2, L(5) = 11.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The shear updates `a=b-a;b+=11*a` and `b+=11*a;a=b-a` need starts (2, 13)
  or (2, −9) and are 38 bytes; with the walrus in the print, 39.
- Python's 4300-digit int-to-str limit stops the program at about n = 4110.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001946), CC BY-SA 4.0.
