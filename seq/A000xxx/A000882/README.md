# A000882

> Number of twin prime pairs <= product of first n primes.
> — [OEIS A000882](https://oeis.org/A000882)

Offset 1: 0, 1, 4, 15, 69, 468, 4636, 57453, 896062, 18463713, 425177757, …

### Python 3 — 91 bytes

```python
P=k=q=1;h=t=0;T=2
while 1:h=h*2+P%k;t+=h&5>4;q+=T**q%q<1;T*=q**(k==T!=print(t));P*=k*k;k+=1
```

**How it works**

- A pair counts when its larger member is at most p_n# (a(3) = 4 counts the
  pairs up to (17, 19), not (29, 31)). The primorial is even, so it is never
  a member of a pair and the order of counting and printing at k = T does
  not matter.
- The frame is the one of [A000849](../A000849/): Wilson's theorem with
  `P` = ((k−1)!)² gives the 0/1 prime flag `P%k`; `T` is the next primorial
  and `q` the next prime, which `q+=T**q%q<1` walks to without a prime test
  (q moves while all its prime factors divide T); `T*=q**(k==T!=print(t))`
  prints at k = T and moves T on.
- Twin pairs: `h` keeps the prime flags as bits, newest in bit 0
  (`h=h*2+P%k`), so (k−2, k) is a pair exactly when bits 0 and 2 are set,
  `t+=h&5>4`. At k = 4, the flags of 2 and 3 are in bits 2 and 1, so (2, 3)
  is not counted.
- The offset is 1, so `T` starts at 2 (no pair is ≤ 2) and `q` at 1: its
  first step makes it 2, which divides T, so it is 3 when T is first
  multiplied.

**Notes**

- Exact integer arithmetic; the only facts used are Wilson's theorem and
  Bertrand's postulate (see A000849).
- Reaching k costs about k² operations: a(6) (pairs up to 30030) comes
  after about 4 s, a(7) (up to 510510) would take about 20 minutes.
- The b-file has 15 terms; the bar is 6 terms (a(1)–a(6)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000882), CC BY-SA 4.0.
