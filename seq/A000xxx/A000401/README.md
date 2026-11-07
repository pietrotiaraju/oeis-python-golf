# A000401

> Numbers of form x^2 + y^2 + 2*z^2.
> — [OEIS A000401](https://oeis.org/A000401)

Offset 1: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, …

### Python 3 — 48 bytes

```python
n=0
while[print(n)]:n+=1;n+=n//(l:=n&-n)%8+l%3>8
```

**How it works**

- Dickson (1927), quoted in the OEIS entry: x² + y² + 2z² represents
  exactly the nonnegative integers that are not of the form 4ᵏ(16m + 14).
  Since 4ᵏ(16m + 14) = 2^(2k+1)·(8m + 7), writing n = 2ᵉ·u with u odd,
  n is left out exactly when e is odd and u ≡ 7 (mod 8).
- `l:=n&-n` is the lowest set bit 2ᵉ of n, so `n//l` is u. Then u mod 8 is
  1, 3, 5 or 7, and 2ᵉ mod 3 is 2 for odd e and 1 for even e. The sum
  `n//l%8+l%3` is therefore at most 9, and it is 9 only for u ≡ 7 (mod 8)
  with e odd (the next largest values are 7 + 1 and 5 + 2), so `…>8` is
  exactly the exclusion test.
- After printing n, the body moves to n + 1 and adds one more step if that
  number is excluded. Excluded numbers are even, so the odd number after
  one is always represented: a single extra step never skips a term.
- `print(n)` sits in the loop condition: `[None]` is a non-empty list, so
  the loop never ends. Printing a(1) = 0 before the first test also keeps
  n = 0 (where `n&-n` is 0) away from the division.

**Notes**

- Also 48 bytes: `n=1` and `while[print(n-1)]:n-=~(n//(l:=n&-n)%8+l%3>8)`
  (`n-=~b` adds 1 + b). The test `(n+l)%(8*l)<l%3>1` is 53 bytes, and
  stripping factors of 4 with `m=n=n+1` / `while m%4<1:m//=4` /
  `n+=m%16==14` is 61.
- Integer arithmetic; correctness for every n rests on Dickson's theorem
  (also Exercise 4 on p. 395 of Sierpiński's *Elementary Theory of
  Numbers*). The output matches a direct search over x, y, z for every
  n < 300 000.
- The program is output-bound: about 100 000 terms in 3 s here. The b-file
  has 1000 terms (up to a(1000) = 1089); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 61 | first entry |
| 2026-11-07 | Python 3 | 48 | lowest set bit: `n//l%8+l%3>8` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000401), CC BY-SA 4.0.
