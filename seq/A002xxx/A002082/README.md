# A002082

> 2nd differences are periodic.
> — [OEIS A002082](https://oeis.org/A002082)

Offset 0: 2, 2, 4, 10, 16, 28, 48, 76, 110, 144, 182, 222, 264, 310, 356, 408, …

### Python 3 — 53 bytes

```python
n=0
while[print(2*n*~-n+50-b'0024:>>:42'[n%10])]:n+=1
```

**What the sequence is**

- The title only says that the second differences are periodic. The data
  and the entry's generating function (Ralf Stephan, 2003) fix them: from
  a(0) = a(1) = 2 the second differences repeat
  2, 4, 0, 6, 8, 8, 6, 0, 4, 2 with period 10.

**How it works**

- **Closed form.** The second differences add up to 40 over a period, an
  average of 4, which is the second difference of 2n². Indeed
  a(n) − (2n² − 2n + 2) is periodic with period 10, equal to
  −c(n mod 10) with c = 0, 0, 2, 4, 10, 14, 14, 10, 4, 2. So
  a(n) = 2n(n−1) + 2 − c(n mod 10).
- **Code.** `b'0024:>>:42'[n%10]` is c(n mod 10) + 48 (the byte values 48,
  48, 50, 52, 58, 62, 62, 58, 52, 50), so `2*n*~-n+50-…` is
  2n(n−1) + 2 − c; `~-n` is n − 1.
- **Every n.** The denominator of the entry's generating function,
  (x⁴−x³+x²−x+1)(x⁴+x³+x²+x+1)(x−1)³, divides (x¹⁰−1)(x−1)², so the
  entry's sequence satisfies the linear recurrence of order 12 with that
  characteristic polynomial. So does the closed form (a quadratic plus a
  10-periodic term). Two solutions of an order-12 recurrence that agree on
  12 consecutive terms agree everywhere, and these agree on all 36 terms
  of the b-file (300 terms of the generating function were also compared).

**Notes**

- Walking the second differences (`a=2;d=0` / `while 1:` /
  `for c in b'2406886042':print(a);a+=d;d+=c-48`) is 62 bytes.
- Exact integer arithmetic. The b-file has 36 terms (n = 0 to 35); the bar
  is the whole b-file in 60 s, a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002082), CC BY-SA 4.0.
