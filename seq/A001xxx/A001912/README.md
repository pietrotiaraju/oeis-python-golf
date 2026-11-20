# A001912

> Numbers k such that 4*k^2 + 1 is prime.
> — [OEIS A001912](https://oeis.org/A001912)

Offset 1: 1, 2, 3, 5, 7, 8, 10, 12, 13, 18, 20, 27, 28, 33, 37, 42, 45, 47, 55, …

### Python 3 — 64 bytes

```python
n=2
while[all(~(n*n)%d for d in range(2,n))and print(n//2)]:n+=2
```

**How it works**

- `n` runs over the even numbers 2, 4, 6, …, so n = 2k and n² + 1 =
  4k² + 1; the program prints k = `n//2` when n² + 1 is prime.
- Trial division: a composite m = n² + 1 has a prime factor d ≤ √m <
  n + 1, and d = n never divides it (n² + 1 ≡ 1 mod n), so trying
  d = 2, …, n − 1 decides primality. For n = 2 the range is empty and
  `all` is true: 5 is prime and a(1) = 1.
- `~(n*n)` is −(n² + 1), which d divides exactly when it divides n² + 1;
  it saves the parentheses of `(n*n+1)`.
- `all` stops at the first divisor, so composites are cheap; a prime costs
  n − 2 divisions.

**Notes**

- Deterministic and exact, so the program is right for every n.
- Looping over k with `~(4*k*k)%d for d in range(2,2*k)` and `print(k)` is
  65 bytes, one more.
- Each prime n² + 1 costs about n divisions, so the time grows like the
  square of the terms: about 3100 terms (k = 21347) in 24 s here. The
  b-file has 10000 terms; the bar is 3000 terms (a(3000) = 20350) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001912), CC BY-SA 4.0.
