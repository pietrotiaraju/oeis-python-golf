# A001751

> Primes together with primes multiplied by 2.
> — [OEIS A001751](https://oeis.org/A001751)

Offset 1: 2, 3, 4, 5, 6, 7, 10, 11, 13, 14, 17, 19, 22, 23, 26, 29, 31, 34, …

### Python 3 — 64 bytes

```python
P=k=1;s={0}
while[{k,k/2}&s and print(k)]:P*=k;k+=1;s|={k>>~P%k}
```

**How it works**

- k is a term when k is prime or k/2 is prime. The set `s` holds 0 and
  the primes found so far, and `{k,k/2}&s` is non-empty exactly then: a
  float such as 7.0 equals and hashes like the int 7, so `k/2` finds 7 in
  the set when k = 14, while an odd k gives a fraction such as 7.5 that
  matches nothing.
- The primes come from Wilson's theorem, as in [A001747](../A001747/):
  after `P*=k;k+=1`, P is (k − 1)!, and `~P%k`, which is −((k − 1)! + 1)
  mod k, is 0 exactly when k is prime. Then `k>>0` adds k itself. For a
  composite k > 4, k divides (k − 1)!, so the shift is k − 1 and
  `k>>k-1` adds 0, already there; k = 4 (3! = 6, shift 1) adds 2, which is
  prime anyway. So s stays {0} plus the primes up to k.
- Each k is tested before the update, so k is in s by then; the first
  test, k = 1, sees {1, 0.5} and prints nothing. `while[…]:` is a
  non-empty list, so the loop never ends.

**Notes**

- Squaring the factorial (`P*=k*k`, then `s|={P%k*k}` adds k or 0) is
  also 64 bytes, but P is twice as long and the program twice as slow.
- Exact integer arithmetic, so the program is right for every n. P has
  about k log₂ k bits; the b-file (10000 terms, up to 65123) prints in
  about 14 s here, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001751), CC BY-SA 4.0.
