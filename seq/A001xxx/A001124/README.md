# A001124

> Primes with 5 as smallest primitive root.
> — [OEIS A001124](https://oeis.org/A001124)

Offset 1: 23, 47, 73, 97, 103, 157, 167, 193, 263, 277, 307, 383, …

### Python 3 — 91 bytes

```python
p=1
while 1:p+=2;[len({pow(b,k,p)for k in range(p)})>p-2for b in(2,3,5)]==[0,0,1]==print(p)
```

**How it works**

- For odd p, `len({pow(b,k,p)for k in range(p)})>p-2` says that the powers
  of b mod p take p − 1 values, i.e. b is a primitive root mod p (and then p
  is prime, see [A001122](../A001122/)). The list of these tests for the bases 2 and 3 (4 = 2² is a square, never a
  primitive root mod an odd prime, so it is left out) and then 5 is compared
  with "all false except the last": booleans compare equal to 0 and 1.
- Composite p never pass, because the test for 5 is false.
- At p = 3, 5, 7 a base can be ≡ 0 mod p; its powers are {1, 0}, which is
  p − 1 values at p = 3. That never matters: 3 and 5 have the primitive root
  2 and 7 has 3, so the list does not start with zeros there.
- `p-2for` gives a SyntaxWarning on stderr, which the rules allow.

**Notes**

- Every candidate costs p calls of `pow` per base: about 120 terms in 30 s
  here. The bar is 100 terms in 60 s (about 21 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001124), CC BY-SA 4.0.
