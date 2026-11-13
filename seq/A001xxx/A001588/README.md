# A001588

> a(n) = a(n-1) + a(n-2) - 1.
> — [OEIS A001588](https://oeis.org/A001588)

Offset 0: 1, 3, 3, 5, 7, 11, 17, 27, 43, 69, 111, 179, 289, 467, 755, 1221, …

### Python 3 — 34 bytes

```python
a=b=1
while[print(a)]:a,b=a-~b,a-2
```

**How it works**

- `b` holds a(n−1) − 2 when a(n) is printed. Then `a-~b` = a + b + 1 =
  a(n) + a(n−1) − 1 = a(n+1), and the new `b` is a(n) − 2, both in one
  tuple assignment.
- The start: running the recurrence backwards, a(−1) = a(1) − a(0) + 1 = 3,
  so b = 1 = a(0) and the start is `a=b=1`.

**Notes**

- a(n) = 2F(n) + 1 with F the Fibonacci numbers.
- The plain window `a,b=1,3` / `a,b=b,a+b-1` and the walrus form
  `a,b=3,4` / `while[print(a:=b-a)]:b+=a-1` are 35 bytes; a search over
  two-variable programs (one or two in-place statements, tuple updates,
  walrus prints) found nothing below 34.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (a(0) to a(500)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001588), CC BY-SA 4.0.
