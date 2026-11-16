# A001819

> Central factorial numbers: second right-hand column of triangle A008955.
> — [OEIS A001819](https://oeis.org/A001819)

Offset 0: 0, 1, 5, 49, 820, 21076, 773136, 38402064, 2483133696, 202759531776, …

### Python 3 — 47 bytes

```python
a=0;f=n=1
while[print(a)]:a=a*n*n+f;f*=n*n;n+=1
```

**How it works**

- **The triangle.** Row n of [A008955](https://oeis.org/A008955) holds the
  coefficients of (x + 1²)(x + 2²)⋯(x + n²), that is the elementary
  symmetric functions eⱼ(1², 2², …, n²). Its second right-hand column is
  a(n) = eₙ₋₁(1², …, n²), the sum of the n products that leave out one
  square: a(n) = (n!)²·Σₖ₌₁..ₙ 1/k², and a(0) = 0 (no products of −1
  squares).
- **The recurrence.** Multiplying in the factor x + n² gives
  eₙ₋₁(1², …, n²) = n²·eₙ₋₂(1², …, (n−1)²) + eₙ₋₁(1², …, (n−1)²), so
  a(n) = n²·a(n−1) + ((n−1)!)², Pierre CAMI's formula on the OEIS page.
- **The program.** `f` is ((n−1)!)², `a` is a(n−1) while `n` is the next
  index: `a=a*n*n+f` makes a(n), `f*=n*n` makes (n!)². The header
  `while[print(a)]:` prints before each step, starting from a(0) = 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 860.
- The b-file has 254 terms (n = 0 to 253); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001819), CC BY-SA 4.0.
