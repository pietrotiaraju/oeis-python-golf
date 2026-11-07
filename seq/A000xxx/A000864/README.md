# A000864

> Deceptive nonprimes: composite numbers k that divide the repunit R_{k-1}.
> — [OEIS A000864](https://oeis.org/A000864)

Offset 1: 91, 259, 451, 481, 703, 1729, 2821, 2981, 3367, 4141, 4187, 5461, …

### Python 3 — 55 bytes

```python
P=k=1
while 1:P*=k;k+=1;pow(10,k-1,9*k)+P%k<2==print(k)
```

**How it works**

- k divides the repunit R_{k−1} = (10^{k−1} − 1)/9 exactly when 9k divides
  10^{k−1} − 1, so the test is `pow(10,k-1,9*k)==1`.
- Every prime p ≥ 7 passes (Fermat: p divides 10^{p−1} − 1 = 9·R_{p−1}, and
  p ≠ 3), so the terms are the composites that pass. Primes are removed with
  Wilson's theorem: `P` is (k−1)!, and `P%k` is k − 1 at primes, 0 at
  composites, and 2 at k = 4.
- The remainder of 10^{k−1} modulo 9k is never 0 (9 does not divide a power
  of 10), so `pow(10,k-1,9*k)+P%k<2` holds exactly when the power is 1 and
  `P%k` is 0. At k = 4 the 2 keeps it out, and 4 is not a term anyway
  (R₃ = 111 is odd).
- `x<2==print(k)` is a chained comparison: `print` only runs when `x<2`.
- `P=k=1` and `P*=k;k+=1` at the top of the loop give P = (k−1)! for
  k = 2, 3, …. The plain factorial is enough here (no need for the squared
  one that makes `P%k` a 0/1 flag), which saves 2 bytes and halves the size
  of `P`.

**Notes**

- Exact integer arithmetic, correct for every n.
- `P` has about k·log₂k bits, and each step multiplies it and takes a
  remainder, so reaching k costs about k² operations: about 80 terms in 60 s
  (a(80) = 137137).
- The b-file has 10000 terms; the bar is 58 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000864), CC BY-SA 4.0.
