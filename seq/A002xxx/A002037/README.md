# A002037

> Product of all primes up to 3^n.
> — [OEIS A002037](https://oeis.org/A002037)

Offset 0: 1, 6, 210, 223092870, 3217644767340672907899084554130, …

### Python 3 — 64 bytes

```python
P=r=k=m=1
while 1:r*=k**(P%k);m*=3**(k==m!=print(r));P*=k*k;k+=1
```

**How it works**

- Wilson's theorem: with P = ((k − 1)!)², P mod k is 1 when k is prime
  and 0 when k is 1 or composite (for composite k > 4, k | (k − 1)!;
  for k = 4, 36 mod 4 = 0). So `r*=k**(P%k)` multiplies k into r
  exactly when k is prime, and r is the product of the primes ≤ k.
- m runs through 1, 3, 9, 27, …: when k reaches m, r is a(n) for
  m = 3ⁿ. `k==m!=print(r)` is false at once when k ≠ m; otherwise it
  prints r and compares m with print's None, which is true, so m is
  multiplied by 3.
- `P*=k*k` then turns ((k − 1)!)² into (k!)² for the next k.

**Notes**

- Exact integer arithmetic, so the program is right for every n. P has
  about 2k·log₁₀ k digits, so a(7) (k = 2187) is still instant;
  a(n) itself has about 3ⁿ·log₁₀ e digits (a(8) has 2803), so from
  n = 9 on printing it hits the 4300-digit int-to-str limit of Python
  3.11+, an interpreter limit.
- The b-file has the 6 terms of the entry (n = 0 to 5); the bar is all
  6, which come at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002037), CC BY-SA 4.0.
