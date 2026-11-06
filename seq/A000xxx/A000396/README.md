# A000396

> Perfect numbers k: k is equal to the sum of the proper divisors of k.
> — [OEIS A000396](https://oeis.org/A000396)

Offset 1: 6, 28, 496, 8128, 33550336, 8589869056, 137438691328, …

### Python 3 — 62 bytes

```python
n=1
while[sum(d*(n%d<1)for d in range(1,n))==n==print(n)]:n+=1
```

**How it works**

- The definition, tried on every n ≥ 1: `d*(n%d<1)` is d when d divides n
  and 0 otherwise, so the sum is the sum of the proper divisors of n.
- `sum(...)==n==print(n)` is the chain `sum(...)==n and n==print(n)`:
  `print(n)` only runs when n is perfect, and the chain is then false
  (`n==None`), which does not matter.
- `while[...]:` keeps looping because a one-element list is always true,
  1 byte under `while 1:` with `;n+=1` at the end.
- `d>>n%d*n` (d shifted right by at least n bits unless d | n) is the same
  length and speed.

**Notes**

- Nothing here depends on the Euclid–Euler theorem or on the open question
  of odd perfect numbers: every n is tested, so an odd perfect number would
  be printed too.
- It is slow, about n steps for each n: 6, 28, 496 and 8128 come out in
  about 7 s, and the 5th term, 33550336, would take years. The bar is 4
  terms in 60 s.
- Printing 2^(p−1)(2^p − 1) for the Mersenne primes 2^p − 1 is far faster,
  but it gives only the even perfect numbers. It is right for every term
  below 10^1500, since there is no odd perfect number there (Ochem and Rao,
  Math. Comp. 81 (2012), 1869–1877), which covers the 15 terms of the
  b-file; past that it rests on the conjecture that no odd perfect number
  exists. With a Lucas–Lehmer test it is 73 bytes and prints 16 terms in
  60 s:

  ```python
  j=s=0;m=3
  while[s or print(m<<j+1)]:j+=1;m-=~m;s=4;exec('s=(s*s-2)%m;'*j)
  ```

  Here m = 2^(j+2) − 1, s is the Lucas–Lehmer residue after j squarings,
  and `m<<j+1` = m(m + 1)/2. The first term, 6 (m = 3, where the test does
  not apply), comes from the starting values s = 0, m = 3.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000396), CC BY-SA 4.0.
