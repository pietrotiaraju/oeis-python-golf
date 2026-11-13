# A001610

> a(n) = a(n-1) + a(n-2) + 1, with a(0) = 0 and a(1) = 2.
> — [OEIS A001610](https://oeis.org/A001610)

Offset 0: 0, 2, 3, 6, 10, 17, 28, 46, 75, 122, 198, 321, 520, 842, 1363, …

### Python 3 — 32 bytes

```python
a=b=1
while[print(a:=b-a)]:b-=~a
```

**How it works**

- Before a(n) is printed, `a` = a(n−1) and `b` = a(n) + a(n−1). The walrus
  `a:=b-a` turns `a` into a(n) and prints it; then `b-=~a` adds a(n) + 1,
  giving a(n) + a(n−1) + 1 + a(n) = a(n+1) + a(n).
- The start: backwards, a(−1) = a(1) − a(0) − 1 = 1, and
  b = a(0) + a(−1) = 1, so `a=b=1`.

**Notes**

- a(n) = L(n+1) − 1 with L the Lucas numbers.
- The plain window `a,b=0,2` / `a,b=b,a-~b` is 34 bytes; a search over
  two-variable programs (one or two in-place statements, tuple updates,
  walrus prints) found nothing below 32.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (a(0) to a(500)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001610), CC BY-SA 4.0.
