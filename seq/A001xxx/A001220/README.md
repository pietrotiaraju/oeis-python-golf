# A001220

> Wieferich primes: primes p such that p^2 divides 2^(p-1) - 1.
> — [OEIS A001220](https://oeis.org/A001220)

Offset 1: 1093, 3511

### Python 3 — 55 bytes

```python
P=k=1
while 1:P*=k*k;k+=1;P%k*pow(2,k,k*k)==2==print(k)
```

**How it works**

- `P` is ((k−1)!)². By Wilson's theorem P mod k is 1 when k is prime;
  for composite k it is 0 (k = 4: 36 mod 4 = 0; k ≥ 6 divides (k−1)!).
- For an odd prime p, p² | 2^(p−1) − 1 ⟺ 2^p ≡ 2 (mod p²), tested as
  `pow(2,k,k*k)==2`; for p = 2 it gives 0, and 2 is not a term.
- `P%k*pow(2,k,k*k)==2==print(k)` is a chained comparison: `print(k)` runs
  only when the product is 2, that is, k is prime and Wieferich.
- The primality test is needed: composite k with k² | 2^(k−1) − 1 are not
  excluded by any theorem (the Wieferich numbers, A077816, are those k,
  and the primes among them are this sequence).

**Notes**

- Only 1093 and 3511 are known; there is no other below 4.97·10¹⁷
  (PrimeGrid, per the OEIS entry). The program keeps searching forever
  and prints any further term in order, so it is correct for every n
  whether the sequence is finite or not.
- `P` grows like k·log k bits, so the search slows down as k grows;
  3511 arrives in a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001220), CC BY-SA 4.0.
