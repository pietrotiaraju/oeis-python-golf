# A001123

> Primes with 3 as smallest primitive root.
> — [OEIS A001123](https://oeis.org/A001123)

Offset 1: 7, 17, 31, 43, 79, 89, 113, 127, 137, 199, 223, 233, …

### Python 3 — 87 bytes

```python
p=1
while 1:p+=2;[len({pow(b,k,p)for k in range(p)})>p-2for b in(2,3)]==[0,1]==print(p)
```

**How it works**

- For odd p, `len({pow(b,k,p)for k in range(p)})>p-2` says that the powers
  of b mod p take p − 1 values, i.e. b is a primitive root mod p (and then p
  is prime, see [A001122](../A001122/)). The list of these tests for the bases 2 and then 3 is compared with "all
  false except the last": booleans compare equal to 0 and 1.
- Composite p never pass, because the test for 3 is false.
- At p = 3, 5, 7 a base can be ≡ 0 mod p; its powers are {1, 0}, which is
  p − 1 values at p = 3. That never matters: 3 and 5 have the primitive root
  2 and 7 has 3, so the list does not start with zeros there.
- `p-2for` gives a SyntaxWarning on stderr, which the rules allow.

**Notes**

- Every candidate costs p calls of `pow` per base: about 215 terms in 30 s
  here. The bar is 190 terms in 60 s (about 21 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001123), CC BY-SA 4.0.
