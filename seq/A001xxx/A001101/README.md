# A001101

> Moran numbers: k such that k/(sum of digits of k) is prime.
> — [OEIS A001101](https://oeis.org/A001101)

Offset 1: 18, 21, 27, 42, 45, 63, 84, 111, 114, 117, 133, 152, 153, 156, 171, 190, …

### Python 3 — 86 bytes

```python
k=0
while 1:k+=1;s=sum(map(int,str(k)));sum(k%m<1for m in range(s,k+1,s))==2==print(k)
```

**How it works**

- `s` is the digit sum of k. The program counts the multiples m of s, from
  s up to k, that divide k.
- If s does not divide k, no multiple of s does either (s | m | k would give
  s | k), so the count is 0. If k = s·q, then m = s·d divides k exactly when
  d divides q, so the count is d(q), the number of divisors of q. And q is
  prime exactly when d(q) = 2: one count does both the divisibility test
  and the primality test.
- `X==2==print(k)` is a chained comparison: it is `X==2 and 2==print(k)`,
  so `print(k)` only runs when the count is 2, and the `False` it leaves is
  thrown away.
- [A001102](../A001102/) (k/s a square) is the same program with the
  parity of the count; [A001103](../A001103/) and [A001104](../A001104/)
  do the same with the product of the digits.

**Notes**

- Other versions that print the same terms: testing s | k first in the same
  chain, `k%s<1<sum(…)<3==print(k)`, 91 bytes, more than twice as many terms
  in the same time; trial division,
  `k%s<1<k//s and all(k%m for m in range(2*s,k,s))and print(k)`, 99 bytes.
- Correct for every k straight from the definition; no theorem needed.
- The count takes about k/s steps for every k, so the run time grows like
  k²: about 2000 terms (up to 104634) come out in 60 s here, and the
  1300th term, 57483, after about 20 s. The b-file has 10000 terms (up to
  761913); the bar is 1300 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001101), CC BY-SA 4.0.
