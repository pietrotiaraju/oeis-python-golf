# A001126

> Primes with 7 as smallest primitive root.
> — [OEIS A001126](https://oeis.org/A001126)

Offset 1: 71, 239, 241, 359, 431, 499, 599, 601, 919, 997, 1051, 1181, …

### Python 3 — 97 bytes

```python
p=1
while 1:p+=2;[len({pow(b,k,p)for k in range(p)})>p-2for b in range(2,8)]==[0]*5+[1]==print(p)
```

**How it works**

- For odd p, `len({pow(b,k,p)for k in range(p)})>p-2` says that the powers
  of b mod p take p − 1 values, i.e. b is a primitive root mod p (and then p
  is prime, see [A001122](../A001122/)). The list of these tests for the bases 2 to 6 (`range(2,8)` with
  `[0]*5+[1]` is shorter than leaving 4 out) and then 7 is compared with
  "all false except the last": booleans compare equal to 0 and 1.
- Composite p never pass, because the test for 7 is false.
- At p = 3, 5, 7 a base can be ≡ 0 mod p; its powers are {1, 0}, which is
  p − 1 values at p = 3. That never matters: 3 and 5 have the primitive root
  2 and 7 has 3, so the list does not start with zeros there.
- `p-2for` gives a SyntaxWarning on stderr, which the rules allow.

**Notes**

- Every candidate costs p calls of `pow` per base: about 43 terms in 30 s
  here. The bar is 38 terms in 60 s (about 21 s here). Testing 7 first and
  stopping early, `all(len({pow(b,k,p)for k in range(p)})//~-p==b//7for b
  in(7,2,3,5,6))>0==print(p)`, is 1 byte longer and about 2.3 times as fast;
  with `x=1;` and `{x:=x*b%p for k in range(p)}` instead of `pow` it is 4
  bytes longer and about 4.5 times as fast.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001126), CC BY-SA 4.0.
