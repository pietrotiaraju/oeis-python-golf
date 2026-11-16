# A001751

> Primes together with primes multiplied by 2.
> — [OEIS A001751](https://oeis.org/A001751)

Offset 1: 2, 3, 4, 5, 6, 7, 10, 11, 13, 14, 17, 19, 22, 23, 26, 29, 31, 34, …

### Python 3 — 66 bytes

```python
P=k=1;s={0}
while[{k*2,k}&s and print(k)]:P*=k;k+=1;s|={k*2>>~P%k}
```

**How it works**

- k is a term when k is prime or k/2 is prime, that is, when 2k or k is
  twice a prime. The set `s` holds 0 and twice each prime found so far,
  so `{k*2,k}&s` is non-empty exactly then: 2k is in s when k is prime,
  and k is in s when k = 2p. An odd k can't equal 2p, and an even
  composite k = 2m with m composite matches neither. Everything stays an
  integer, so the test is exact for every k.
- The primes come from Wilson's theorem, as in [A001747](../A001747/):
  after `P*=k;k+=1`, P is (k − 1)!, and `~P%k`, which is −((k − 1)! + 1)
  mod k, is 0 exactly when k is prime. Then `k*2>>0` adds 2k. For a
  composite k > 4, k divides (k − 1)!, so the shift is k − 1 and
  `2k>>k-1` is 0, already there; k = 4 (3! = 6, shift 1) adds 4 = 2·2,
  which is there anyway. So s stays {0} plus twice the primes up to k.
- Each k is tested after its own update, so 2k is in s by then; the first
  test, k = 1, sees {2, 1} and prints nothing. `while[…]:` is a
  non-empty list, so the loop never ends.

**Notes**

- The first version (64 bytes) tested `{k,k/2}&s` with the primes
  themselves in s. The float k/2 is exact only while k < 2^53, so it was
  replaced by this all-integer test (+2 bytes).
- Squaring the factorial (`P*=k*k`, then `s|={P%k*k*2}` adds 2k or 0) is
  also 66 bytes, but P is twice as long and the program twice as slow.
- P has about k log₂ k bits; the b-file (10000 terms, up to 65123) prints
  in about 12 s here, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 64 | first entry |
| 2026-11-16 | Python 3 | 66 | exact integer test instead of the float k/2 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001751), CC BY-SA 4.0.
