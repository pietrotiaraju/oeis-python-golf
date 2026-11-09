# A001359

> Lesser of twin primes.
> — [OEIS A001359](https://oeis.org/A001359)

Offset 1: 3, 5, 11, 17, 29, 41, 59, 71, 101, 107, 137, 149, 179, 191, 197, …

### Python 3 — 54 bytes

```python
P=k=1
while 1:P*=k;k+=1;(4*P+4+k)%(k*k+2*k)or print(k)
```

**How it works**

- **Clement's theorem** (P. A. Clement, "Congruences for sets of primes",
  *Amer. Math. Monthly* 56 (1949), 23–25): for an integer k ≥ 2, k and
  k + 2 are both prime if and only if
  4·((k − 1)! + 1) + k ≡ 0 (mod k(k + 2)).
  So a single test per k decides whether k is the lesser of a twin pair.
- **The loop.** At the top of each pass the body first turns P into
  (k − 1)! for the new k: P = 1 = 1! when k becomes 2, then P = 2!, 3!, …
  The expression `(4*P+4+k)%(k*k+2*k)or print(k)` prints k exactly when the
  remainder is 0. Starting from k = 2 matters: at k = 1 the congruence
  holds (4·2 + 1 = 9 ≡ 0 mod 3) although 1 is not prime, and the order of
  the statements skips it.

**Notes**

- Exact, and correct for every n by Clement's theorem (a theorem, not a
  conjecture; whether there are infinitely many twin primes does not
  matter for the program, which just keeps testing).
- P = (k − 1)! has about k·log₁₀ k digits, so each step costs time
  proportional to that, and the program slows down roughly quadratically.
- The b-file has 100000 terms (up to 18409199); the bar is 800 terms
  (a(800) = 58907) in 60 s.
- Testing k and k − 2 separately by Wilson's theorem, with the two flags
  kept in a shift register as in [A001097](../A001097/), is `P=k=1;s=0` / `while 1:s+=s+P%k;s&5>4==print(k-2);P*=k*k;k+=1`,
  56 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001359), CC BY-SA 4.0.
