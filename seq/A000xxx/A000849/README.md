# A000849

> Number of primes <= product of first n primes, A002110(n).
> — [OEIS A000849](https://oeis.org/A000849)

Offset 0: 0, 1, 3, 10, 46, 343, 3248, 42331, 646029, 12283531, 300369796, …

### Python 3 — 75 bytes

```python
P=k=T=q=1;c=0
while 1:c+=P%k;q+=T**q%q<1;T*=q**(k==T!=print(c));P*=k*k;k+=1
```

**How it works**

- The loop walks k = 1, 2, 3, … with `P` = ((k−1)!)²; by Wilson's theorem
  `P%k` is 1 at primes and 0 otherwise, so `c+=P%k` keeps c = π(k).
- `T` is the next primorial to reach. When k = T, `print(c)` gives π(T),
  and `T*=q` moves to the next primorial, where `q` is the next prime.
- `q` is found without a prime test: `q+=T**q%q<1` moves it on by one per
  step while q divides a power of T, i.e. while every prime factor of q is
  among the first n primes (a prime power dividing q has exponent < q).
  Right after `T*=q`, q divides T, so it moves; every number between two
  consecutive primes is composite with smaller prime factors, all in T, so q
  stops at the first new prime. From k = T to the next target there are
  T·(q − 1) steps, more than the gap to the next prime (Bertrand's
  postulate), so q is ready in time.
- `T*=q**(k==T!=print(c))`: the chained comparison calls `print` only when
  k == T, and then `T!=None` is True, so the exponent is 1 exactly at the
  targets.
- Start: T = 1 gives a(0) = π(1) = 0. q starts at 1, and its first step
  (`T**1%1` is 0) makes it 2 before `T` is multiplied.
- `c+=P%k` comes before the print, so the prime target T = 2 counts itself:
  a(1) = 1.

**Notes**

- Exact integer arithmetic; the only facts used are Wilson's theorem and
  Bertrand's postulate.
- Reaching k costs about k² operations: a(6) = π(30030) comes after about
  4 s, but a(7) = π(510510) would need 17² times as long, about 20 minutes.
- The b-file has 20 terms; the bar is 7 terms (a(0)–a(6)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000849), CC BY-SA 4.0.
