# A002068

> Wilson remainders: a(n) = ((p-1)!+1)/p mod p, where p = prime(n).
> — [OEIS A002068](https://oeis.org/A002068)

Offset 1: 1, 1, 0, 5, 1, 0, 5, 2, 8, 18, 19, 7, …

### Python 3 — 48 bytes

```python
P=k=1
while 1:P*=k;k+=1;-~P%k or print(-~P//k%k)
```

**How it works**

- `P` is (k−1)! and k runs over 2, 3, 4, …. By Wilson's theorem
  (k−1)! + 1 is divisible by k exactly when k is prime (for composite k > 4,
  k divides (k−1)!; for k = 4, 3! + 1 = 7), so `-~P%k` (that is
  (P+1) mod k) is 0 exactly at the primes, and `or` then prints.
- At a prime p, `-~P//k%k` is ((p−1)! + 1)/p mod p, the definition: the
  division is exact, and `//` and `%` share a precedence level and run left
  to right.

**Notes**

- Exact integer arithmetic, so the program is right for every n; (k−1)!
  is kept whole, about 230000 bits at the 2000th prime, 17389.
- The b-file has 2000 terms; the bar is the whole b-file in 60 s, which
  takes under a second here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002068), CC BY-SA 4.0.
