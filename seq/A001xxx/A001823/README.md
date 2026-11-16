# A001823

> Central factorial numbers: column 2 in triangle A008956.
> — [OEIS A001823](https://oeis.org/A001823)

Offset 1: 0, 9, 259, 1974, 8778, 28743, 77077, 179452, 375972, 725781, 1312311, …

### Python 3 — 46 bytes

```python
a=0;b=k=1
while[print(a)]:k+=2;a+=k*k*b;b+=k*k
```

**How it works**

- **The triangle.** Row n of [A008956](https://oeis.org/A008956) holds the
  elementary symmetric functions of the odd squares 1², 3², …, (2n − 1)².
  Column 2 is a(n) = e₂(1², 3², …, (2n − 1)²), the sum of the products of
  two distinct odd squares below (2n)²: a(1) = 0, a(2) = 1·9,
  a(3) = 9 + 25 + 225 = 259.
- **The recurrence.** Adding the square k² = (2n + 1)² turns e₂ into
  e₂ + k²·e₁ and e₁ into e₁ + k². The program keeps `a` = e₂ and `b` = e₁,
  starting at n = 1 with a = 0, b = 1 and k = 1; each pass steps k by 2
  first.
- The closed form n(n − 1)(2n + 1)(2n − 1)(2n − 3)(10n + 7)/90 from the
  OEIS page is 67 bytes as a program.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n) is a
  polynomial of degree 6 in n.
- The b-file has 1000 terms (n = 1 to 1000); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001823), CC BY-SA 4.0.
