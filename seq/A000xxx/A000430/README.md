# A000430

> Primes and squares of primes.
> — [OEIS A000430](https://oeis.org/A000430)

Offset 1: 2, 3, 4, 5, 7, 9, 11, 13, 17, 19, …

### Python 3 — 60 bytes

```python
n=1
while 1:n+=1;sum(n%k<1for k in range(2,n))<2and print(n)
```

**How it works**

- For n ≥ 2 the number of divisors is d(n) = Π (e_i + 1) over the prime
  powers p_i^e_i of n, so d(n) = 2 exactly for primes and d(n) = 3 exactly for
  squares of primes. The terms are therefore the n ≥ 2 with at most one
  divisor strictly between 1 and n.
- `sum(n%k<1for k in range(2,n))` counts those divisors, and `<2and
  print(n)` prints n when there is at most one.

**Notes**

- Collecting primes by Wilson's theorem ((n−1)!² is not divisible by n
  exactly when n is prime, n > 1) together with their squares in a set: 74
  bytes. `>1or print(n)` or counting from k = 1 with `<3`: also 60.
- Exact integer arithmetic, so the program is right for every n.
- Each n costs n − 2 divisions: the 1000 terms of the bar (up to 7699) take
  about 10 s here.
- The b-file has 1000 terms (up to a(1000) = 7699); the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 74 | first entry |
| 2026-11-07 | Python 3 | 60 | at most one divisor strictly between 1 and n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000430), CC BY-SA 4.0.
