# A002113

> Palindromes in base 10.
> — [OEIS A002113](https://oeis.org/A002113)

Offset 1: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, …

### Python 3 — 92 bytes

```python
i=0
while 1:
 for h in map(str,range((k:=10**(i//2))-0**i,k*10)):print(h+h[i%2-2::-1])
 i+=1
```

**How it works**

- **Halves.** A palindrome of length 2d − 1 or 2d is fixed by its first d
  digits, a number h in [10^(d−1), 10^d): its digits followed by their
  reversal, without the last digit of h repeated when the length is odd.
  For a fixed length the order of the palindromes is the order of h.
- **Passes.** Pass i = 0, 1, 2, … handles the length i + 1: h runs over
  [k, 10k) with k = 10^⌊i/2⌋, and `h+h[i%2-2::-1]` appends the reversal
  starting at the last digit (even length, `h[-1::-1]`) or at the one
  before it (odd length, `h[-2::-1]`; for a one-digit h that slice is
  empty). Shorter palindromes are smaller, so the passes print every
  palindrome in increasing order.
- **Zero.** `-0**i` lowers the start of pass 0 to 0 (0⁰ = 1, 0^i = 0
  later), so a(1) = 0 comes first.

**Notes**

- Looping over (k, ±) with `for j in-2,-1:` and `k*=10`, with `print(0)`
  in front, is 96 bytes.
- The whole b-file (19999 terms, up to 99999999) takes a fraction of a
  second; the bar is the whole b-file in 60 s.
- Testing every number is half as long but needs 10⁸ tests for the b-file:
  see the separate record below.

## First 16000 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 16000 terms have to arrive in time.

### Python 3, 16000 terms — 46 bytes

```python
n=0
while 1:s=str(n);s==s[::-1]==print(n);n+=1
```

**How it works**

- Every n from 0 up is tested: `s==s[::-1]==print(n)` is a chained
  comparison, so `print(n)` runs only when the decimal string equals its
  reversal; it returns None, the comparison is false, and the loop goes on.

**Limits**

- One test per number: the first 16000 terms come in about 22 reference
  seconds, and the whole b-file (up to 99999999) needs 10⁸ tests.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 92 | first entry |

**Python 3, 16000 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 46 | first entry: test every number |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002113), CC BY-SA 4.0.
