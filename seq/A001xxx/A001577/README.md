# A001577

> An operational recurrence.
> — [OEIS A001577](https://oeis.org/A001577)

Offset 1: 1, 1, 2, 6, 60, 2880, 2246400, 135862272000, 10376834265907200000, …

### Python 3 — 47 bytes

```python
a=b=f=g=1
while[print(b)]:a,b,f,g=b,a*b*g,g,f+g
```

**How it works**

- The entry's comment (after Gould, Fib. Quart. 1963): u₀ = 1, u₁ = x and
  u_{n+1} = x·(d/dx)(u_n·u_{n−1}); a(n) = u_n(1).
- Every u_n is a single monomial, u_n = c_n·x^(F_n) with F the Fibonacci
  numbers: true for n = 0, 1, and if it holds for n − 1 and n then
  u_n·u_{n−1} = c_n·c_{n−1}·x^(F_n + F_(n−1)), and x·d/dx multiplies a
  monomial by its degree F_(n+1). So **c_(n+1) = F_(n+1)·c_n·c_(n−1)**
  with c₀ = c₁ = 1, and a(n) = c_n. Unrolled, this is the entry's formula
  a(n) = Π_k F_k^(F_(n+1−k)).
- The state (a, b, f, g) is (c_(n−1), c_n, F_n, F_(n+1)), all 1 at n = 1.
  One tuple assignment prints c_n and moves to n + 1: b becomes
  c_(n−1)·c_n·F_(n+1), and (f, g) steps along the Fibonacci numbers.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The number of digits grows like φⁿ: a(20) has 4209 digits and a(21)
  has 6813, past Python's 4300-digit int-to-str limit, so the program
  prints 20 terms and stops there with a ValueError.
- The b-file has 12 terms (up to a(12)); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001577), CC BY-SA 4.0.
