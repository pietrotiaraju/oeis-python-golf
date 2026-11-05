# A000062

> A Beatty sequence: a(n) = floor(n/(e-2)).
> — [OEIS A000062](https://oeis.org/A000062)

Offset 1: 1, 2, 4, 5, 6, 8, 9, 11, 12, 13, 15, 16, 18, 19, 20, 22, …

### Python 3 — 53 bytes

```python
d=1;f=k=2
while 1:k+=1;d=d*k+1;f*=k;print((k-2)*f//d)
```

**How it works**

- With N = `k`, `f` is N! and `d` is Σ_{j=2..N} N!/j!, both integers:
  going from N − 1 to N multiplies every term by N and adds the new
  term N!/N! = 1, so `d=d*k+1;f*=k`. They start at N = 2 (d = 1, f = 2).
  Then d/f = S_N − 2, where S_N = Σ_{j≤N} 1/j! is the partial sum of the
  series for e, just below it.
- The n-th pass has N = n + 2 and prints ⌊n·N!/d⌋ = ⌊n/(S_N − 2)⌋, in
  exact integer arithmetic.
- Since S_N < e, this is never below ⌊n/(e − 2)⌋. It could only be too
  big if some integer m had m·(S_N − 2) ≤ n < m·(e − 2), that is
  0 < m·e − (n + 2m) < m·(e − S_N): e would have to be very close to a
  fraction with denominator m.
- It never is. By Euler's continued fraction e = [2; 1, 2, 1, 1, 4, 1, 1,
  6, …] and the best-approximation property of convergents,
  |q·e − p| ≥ |q_k·e − p_k| > 1/(q_{k+1} + q_k) ≥ 1/((a_{k+1} + 2)·q) for
  q_k ≤ q < q_{k+1}. The partial quotients of e grow linearly while the
  q_k grow at least like Fibonacci numbers, so a_{k+1} ≤ q_k + 1 and
  **|q·e − p| > 1/(q·(q + 3))** for all integers p and q ≥ 1.
- If any m works, the smallest one above n/(e − 2), m = a(n) + 1, does,
  so it is enough that m·(e − S_N) ≤ 1/(m·(m + 3)) for that m. Here
  m < 1.4n + 1 and e − S_N < 1/(N!·N), so the condition holds
  once m²·(m + 3) ≤ (n + 2)!·(n + 2): for n = 2 that is 54 ≤ 96, n = 3
  gives 200 ≤ 600, and the factorial side only pulls further ahead.
  For n = 1 the program computes ⌊1/(2/3)⌋ = 1 directly. The result is
  exact for every n.

**Notes**

- N = n + 2 is as tight as lower approximations allow: with N = n + 1,
  n = 1 gives ⌊1/(1/2)⌋ = 2. The cruder bound from the usual proof that
  e is irrational, |e − p/q| > 1/(q + 1)!, would need N ≥ a(n) + 2,
  about 1.39·n.
- The numbers have about N·log₂N bits; the whole b-file, 1000 terms,
  takes well under a second, and the bar is all of it in 60 s.
- Printing in the loop condition, `while[print((k-2)*f//d)]:`, needs the
  N = 3 start `d=4;f=6;k=3` and is 54 bytes. With sympy,
  `floor(n/(E-2))` after `from sympy import*` is 59 bytes, longer than
  plain Python.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000062), CC BY-SA 4.0.
