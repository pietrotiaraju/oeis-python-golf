# A002038

> Numbers dividing A002037(i) and larger than A002037(i-1), for some i>0.
> — [OEIS A002038](https://oeis.org/A002038)

Offset 1: 1, 2, 3, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210, 221, 230, 231, …

### Python 3 — 84 bytes

```python
P=R=k=d=1
while[R%d or print(d)]:
 d+=1
 while R<d or 3**k%k:k+=1;R*=k**(P%k);P*=k*k
```

**How it works**

- Write Pᵢ = A002037(i), the product of the primes up to 3ⁱ: P₀ = 1,
  P₁ = 6, P₂ = 210, P₃ = 223092870, … The terms are the divisors d of
  some Pᵢ with d > Pᵢ₋₁. The data starts with 1, which needs i = 0 with
  P₋₁ read as 0; the program follows the data.
- Since d | Pᵢ gives d ≤ Pᵢ, a number d can only qualify for the least
  i with Pᵢ ≥ d (for a larger j, d ≤ Pᵢ ≤ Pⱼ₋₁). So d is a term exactly
  when d divides that Pᵢ, and testing d = 1, 2, 3, … in turn lists the
  terms in increasing order.
- R is the current Pᵢ. When d passes it, the inner loop multiplies in
  the next primes, k by k, until k is again a power of 3 (`3**k%k` is
  0 exactly when k is 1 or a power of 3) and R ≥ d. Primes come from
  Wilson's theorem: P is kept equal to (k!)², so right after `k+=1` it
  is ((k − 1)!)², which is 1 mod k for a prime k and 0 mod k otherwise;
  `R*=k**(P%k)` multiplies in exactly the primes.
- `[R%d or print(d)]` prints d when it divides R and is always true (a
  one-element list); then d moves on, and R with it if needed.

**Notes**

- Exact integer arithmetic, so the program is right for every n; it is
  slow in the long run (it tests every d), but i ≤ 3 already gives 470
  terms, up to 223092870.
- The b-file has the 57 terms of the entry (up to 690); the bar is all
  57, which come at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002038), CC BY-SA 4.0.
