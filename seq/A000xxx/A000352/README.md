# A000352

> One half of the number of permutations of [n] such that the differences have three runs with the same signs.
> — [OEIS A000352](https://oeis.org/A000352)

Offset 4: 5, 29, 118, 418, 1383, 4407, 13736, 42236, 128761, 390385, …

### Python 3 — 42 bytes

```python
n=4
while[print(3**n//4-n//2+3-2**n)]:n+=1
```

**How it works**

- The closed form in the OEIS entry is a(n) = (3ⁿ − 4·2ⁿ − 2n + 11)/4.
  It follows from André's recurrence for the number R(n, k) of
  permutations of [n] with k alternating runs,
  R(n, k) = k·R(n−1, k) + 2R(n−1, k−1) + (n−k)·R(n−1, k−2): with
  R(n, 1) = 2 and R(n, 2) = 2ⁿ − 4 it gives
  a(n) = R(n, 3)/2 = 3a(n−1) + 2ⁿ⁻¹ + n − 7, a(3) = 0, which the closed
  form satisfies.
- Since 4·2ⁿ/4 = 2ⁿ, the rest (3ⁿ − 2n + 11)/4 is an integer as well,
  and it equals `3**n//4-n//2+3`: for even n, 3ⁿ ≡ 1 (mod 4), so
  ⌊3ⁿ/4⌋ = (3ⁿ − 1)/4 and ⌊n/2⌋ = n/2; for odd n, 3ⁿ ≡ 3, so
  ⌊3ⁿ/4⌋ = (3ⁿ − 3)/4 and ⌊n/2⌋ = (n − 1)/2. Both cases add up to
  (3ⁿ − 2n + 11)/4.

**Notes**

- Exact integer arithmetic, correct for every n; checked against a
  brute-force count for n ≤ 10. Only the 4300-digit int-to-str limit of
  Python 3.11+ stops it, after about 9000 terms. The whole b-file
  (397 terms, n = 4 to 400) prints at once; the bar is the whole b-file
  in 60 s.
- The formula as written, `(3**n-4*2**n-2*n+11)//4`, is 4 bytes longer,
  `(3**n-2*n+11)//4-2**n` 2 bytes and `(3**n-2*n)//4+3-2**n` 1 byte.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000352), CC BY-SA 4.0.
