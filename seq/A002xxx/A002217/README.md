# A002217

> Starting with n, repeatedly calculate the sum of prime factors (with repetition) of the previous term, until reaching 0 or a fixed point: a(n) is the number of terms in the resulting sequence.
> — [OEIS A002217](https://oeis.org/A002217)

Offset 1: 2, 1, 1, 1, 1, 2, 1, 3, 3, 2, 1, 2, …

### Python 3 — 96 bytes

```python
S=[0,0];A=[0,2];n=1
while[print(A[n])]:
 n+=1;d=2
 while n%d:d+=1
 S+=d+S[n//d],;A+=A[S[n]%n]+1,
```

**How it works**

- **The walk.** Let s(m) be the sum of the prime factors of m with
  repetition ([A001414](https://oeis.org/A001414)), with s(1) = 0. For
  m = xy with x, y ≥ 2, x + y ≤ xy with equality only at x = y = 2, so
  s(m) < m for every composite m except 4, while s(p) = p for a prime p
  and s(4) = 4. So the walk n, s(n), s(s(n)), … goes down until it stops
  at a prime or at 4 (or at 0, which only 1 reaches: 1 → 0). The term
  counts the distinct values: a(m) = 1 when s(m) = m, otherwise
  a(m) = 1 + a(s(m)).
- **Both lists grow together.** `S[m]` = s(m) and `A[m]` = a(m). For
  n ≥ 2, `while n%d:d+=1` finds the smallest prime factor d, and
  s(n) = d + s(n/d) reads the earlier entry. Then
  `A+=A[S[n]%n]+1,`: if s(n) < n, the index is s(n) and the term is
  a(s(n)) + 1; if s(n) = n, the index wraps to 0, and `A[0]` = 0 makes
  the term 1. (No later m has s(m) = 0, so the slot of a(0) is free for
  this.)
- **Start.** `S=[0,0]` holds s(0), s(1) and `A=[0,2]` holds the free slot
  and a(1) = 2 (the walk 1, 0). `while[print(A[n])]:` prints a(n) in the
  loop test (a one-element list is true) and then builds entry n + 1.

**Notes**

- Exact integers: right for every n.
- The smallest-factor search is at most n steps and runs once per n:
  the whole b-file (10000 terms) comes in about a second. The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 96 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002217), CC BY-SA 4.0.
