# A001612

> a(n) = a(n-1) + a(n-2) - 1 for n > 1, a(0)=3, a(1)=2.
> — [OEIS A001612](https://oeis.org/A001612)

Offset 0: 3, 2, 4, 5, 8, 12, 19, 30, 48, 77, 124, 200, 323, 522, 844, 1365, …

### Python 3 — 33 bytes

```python
a=b=3
while[print(a)]:b=a+~b;a+=b
```

**How it works**

- a(n) = L(n) + 1 with L the Lucas numbers (a − 1 satisfies the Fibonacci
  recurrence and starts 2, 1).
- `b` holds L(n−2) when a(n) is printed. `b=a+~b` gives
  a(n) − L(n−2) − 1 = L(n) − L(n−2) = L(n−1), and `a+=b` then gives
  L(n) + 1 + L(n−1) = a(n+1); after it, `b` = L(n−1), one step on.
- The start is a(0) = 3 and b = L(−2) = 3, so `a=b=3`.

**Notes**

- The plain window `a,b=3,2` / `a,b=b,a+b-1` is 35 bytes; a search over
  two-variable programs (one or two in-place statements, tuple updates,
  walrus prints) found nothing below 33.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (a(0) to a(500)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001612), CC BY-SA 4.0.
