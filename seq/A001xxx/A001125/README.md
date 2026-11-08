# A001125

> Primes with 6 as smallest primitive root.
> — [OEIS A001125](https://oeis.org/A001125)

Offset 1: 41, 109, 151, 229, 251, 271, 367, 733, 761, 971, 991, 1069, …

### Python 3 — 95 bytes

```python
p=1
while 1:p+=2;[len({pow(b,k,p)for k in range(p)})>p-2for b in(2,3,5,6)]==[0,0,0,1]==print(p)
```

**How it works**

- For odd p, `len({pow(b,k,p)for k in range(p)})>p-2` says that the powers
  of b mod p take p − 1 values, i.e. b is a primitive root mod p (and then p
  is prime, see [A001122](../A001122/)). The list of these tests for the bases 2, 3 and 5 (4 is a square, never a
  primitive root, so it is left out) and then 6 is compared with "all false
  except the last": booleans compare equal to 0 and 1.
- Composite p never pass, because the test for 6 is false.
- At p = 3, 5, 7 a base can be ≡ 0 mod p; its powers are {1, 0}, which is
  p − 1 values at p = 3. That never matters: 3 and 5 have the primitive root
  2 and 7 has 3, so the list does not start with zeros there.
- `p-2for` gives a SyntaxWarning on stderr, which the rules allow.

**Notes**

- Every candidate costs p calls of `pow` per base, and the terms grow fast
  (a(40) = 3251): about 43 terms in 30 s here. The bar is 38 terms in 60 s
  (about 21 s here). Testing 6 first and stopping early with
  `all(…//~-p==b//6for b in(6,2,3,5))` is 1 byte longer and about twice as
  fast.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 95 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001125), CC BY-SA 4.0.
