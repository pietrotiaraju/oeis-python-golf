# A002067

> a(n) = Sum_{k=0..n-1} binomial(2*n,2*k)*a(k)*a(n-k-1).
> — [OEIS A002067](https://oeis.org/A002067)

Offset 0: 1, 1, 7, 127, 4369, 243649, 20036983, 2280356863, 343141433761, …

### Python 3 — 103 bytes

```python
import math
a=[n:=1]
while[print(a[-1])]:a+=sum(math.comb(2*n,2*k)*a[k]*a[n+~k]for k in range(n)),;n+=1
```

**How it works**

- **Definition.** The name is the recurrence: a(0) = 1 and
  a(n) = Σ_(k=0..n−1) C(2n, 2k)·a(k)·a(n−k−1).
- **Program.** `a` is the list a(0…n−1) and `n` its length (`a=[n:=1]`),
  so `a[n+~k]` is a(n−1−k); the sum is appended as a one-element tuple
  (`a+=…,`) and printed by the next `while` header.

**Notes**

- Other forms in the entry: a(n) = b(2n+1) where B′ = exp(B²/2), and the
  increasing triangular cacti and bilabeled trees counts. Running the
  derivative polynomials of that ODE (P_(k+1) = P_k′ + k·y·P_k) is longer.
- a(n) has about 2n·log₁₀ n digits; the b-file has 51 terms (n = 0 to 50),
  and the bar is the whole b-file in 60 s, which takes a fraction of a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002067), CC BY-SA 4.0.
