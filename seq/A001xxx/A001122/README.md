# A001122

> Primes with primitive root 2.
> — [OEIS A001122](https://oeis.org/A001122)

Offset 1: 3, 5, 11, 13, 19, 29, 37, 53, 59, 61, 67, 83, …

### Python 3 — 65 bytes

```python
p=1
while 1:p+=2;len({pow(2,k,p)for k in range(p)})>p-2==print(p)
```

**How it works**

- p is in the sequence exactly when the powers 2⁰, 2¹, …, 2^(p−1) mod p take
  p − 1 different values, that is, when 2 has multiplicative order p − 1.
  That alone forces p to be prime (Lucas): modulo an odd composite p the
  order of 2 divides φ(p) < p − 1. So there is no separate primality test.
- Only odd p are tried (`p+=2` from 3).
- There are never more than p − 1 values (all of them units), so
  `len(…)>p-2` is `==p-1` with one byte less. In `…>p-2==print(p)` the
  chained comparison calls `print` only when the first comparison holds.

**Notes**

- Each candidate costs p calls of `pow`, so the time grows like the square
  of the terms: about 515 terms in 30 s here. The bar is 450 terms in 60 s
  (about 22 s here).
- Faster but longer: counting the divisors d of p − 1 with 2^d ≡ 1
  (`sum(p%d==1==pow(2,d,p)for d in range(1,p))==1`, 72 bytes), or
  multiplying in a walrus instead of `pow` (`x=1;len({x:=x*2%p for k in
  range(p)})`, 68 bytes); both are about twice as fast.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001122), CC BY-SA 4.0.
