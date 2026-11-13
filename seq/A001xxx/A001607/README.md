# A001607

> a(n) = -a(n-1) - 2*a(n-2).
> — [OEIS A001607](https://oeis.org/A001607)

Offset 0: 0, 1, −1, −1, 3, −1, −5, 7, 3, −17, 11, 23, −45, −1, 91, −89, −93, …

### Python 3 — 35 bytes

```python
a=b=0
while[print(a)]:a,b=b-~b,~a-b
```

**How it works**

- Every term from a(1) on is odd, because a(n) ≡ a(n−1) (mod 2) and
  a(1) = 1. So `b` can hold (a(n+1) − 1)/2 while a(n) is printed.
- Then `b-~b` = 2b + 1 = a(n+1), and
  `~a-b` = −a(n) − 1 − b = (−2a(n) − a(n+1) − 1)/2 = (a(n+2) − 1)/2,
  which is the next value of `b`; one tuple assignment does both.
- The start: a(0) = 0 and b = (a(1) − 1)/2 = 0, so `a=b=0`.

**Notes**

- The plain window `a,b=0,1` / `a,b=b,-b-2*a` is 36 bytes; a search over
  two-variable programs (one or two in-place statements, tuple updates,
  walrus prints) found nothing below 35.
- The characteristic roots are (−1 ± √−7)/2, of absolute value √2, so the
  terms grow like 2^(n/2) with changing signs.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (a(0) to a(500)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001607), CC BY-SA 4.0.
