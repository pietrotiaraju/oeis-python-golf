# A034851

> Rows of Losanitsch's triangle T(n, k), n >= 0, 0 <= k <= n.
> — [OEIS A034851](https://oeis.org/A034851)

Offset 0: 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 4, 2, 1, 1, 3, 6, 6, 3, 1, …

### Python 3 — 92 bytes

```python
from math import*
n=k=0
while[print(comb(n,k)+(n|~k)%2*comb(n//2,k//2)>>1)]:k=-~k%-~n;n+=k<1
```

**How it works**

- T(n, k) counts binary strings of length n with k ones up to reversal. By
  Burnside over the two-element group {identity, reversal},
  T(n, k) = (C(n, k) + P(n, k))/2, where P(n, k) counts the palindromes
  (A051159), as on the OEIS page.
- A palindrome is fixed by its first ⌊n/2⌋ bits and, for odd n, its middle
  bit. The ones in the mirrored pairs come two at a time, so k odd needs a
  middle bit: P(n, k) = C(⌊n/2⌋, ⌊k/2⌋), except P = 0 when n is even and k
  is odd.
- `(n|~k)%2` is that 0/1 factor: ~k is odd exactly when k is even, so
  n | ~k is odd when n is odd or k is even. It is a negative number, but
  Python's `%2` still gives 0 or 1, and `*` then picks the palindrome term.
  `+` binds tighter than `>>`, so `>>1` halves the whole sum.
- `k=-~k%-~n` steps k through 0, 1, …, n and wraps to 0 after n, and
  `n+=k<1` moves to the next row exactly when it wraps. `while[print(…)]:`
  is always true (a one-element list), a byte under `while 1:` with the
  print in the body.

**Notes**

- About 834 000 terms (rows up to n ≈ 1290) in 60 s here; the bar is the
  whole b-file (5050 terms, rows 0–99). The 4300-digit int-to-str limit only
  matters past n ≈ 14 300.
- When n is even and k is odd, C(n, k) is even (it has the parity of
  P = 0), so any palindrome term 0 or 1 gives the same floor. That gives a
  tie at 92 bytes: `comb(n>>1+k*~n%2*n,k//2)` shifts the first argument to
  0 in that case (`k*~n%2` is 1 exactly when k is odd and n even), and
  comb(0, ⌊k/2⌋) is 0 or 1.
- Writing the factor as `comb(n%2,k%2)` (one step of Lucas' theorem:
  P = C(⌊n/2⌋, ⌊k/2⌋)·C(n mod 2, k mod 2)) is 97 bytes; a row-by-row
  `for k in range(n+1)` loop is 102. Keeping Pascal rows in lists instead
  of importing `comb` costs more than the 18-byte import.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A034851), CC BY-SA 4.0.
