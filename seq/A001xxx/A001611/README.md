# A001611

> a(n) = Fibonacci(n) + 1.
> — [OEIS A001611](https://oeis.org/A001611)

Offset 0: 1, 2, 2, 3, 4, 6, 9, 14, 22, 35, 56, 90, 145, 234, 378, 611, 988, …

### Python 3 — 33 bytes

```python
a=b=1
while[print(a)]:a,b=a+b,a-1
```

**How it works**

- `b` holds F(n−1) = a(n−1) − 1 when a(n) = F(n) + 1 is printed. Then
  `a+b` = F(n) + 1 + F(n−1) = F(n+1) + 1 = a(n+1), and the new `b` is
  a(n) − 1 = F(n), both in one tuple assignment.
- The start is a(0) = F(0) + 1 = 1 and b = F(−1) = 1, so `a=b=1`.

**Notes**

- The terms satisfy a(n) = a(n−1) + a(n−2) − 1; the plain window
  `a,b=1,2` / `a,b=b,a+b-1` and the Fibonacci walrus
  `a=b=1` / `while[print(1+(a:=b-a))]:b+=a` are 35 bytes. A search over
  two-variable programs (one or two in-place statements, tuple updates,
  walrus prints) found nothing below 33.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 251 terms (a(0) to a(250)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001611), CC BY-SA 4.0.
