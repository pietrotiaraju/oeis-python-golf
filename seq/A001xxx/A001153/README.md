# A001153

> Degrees of primitive irreducible trinomials: n such that 2^n - 1 is a Mersenne prime and x^n + x^k + 1 is a primitive irreducible polynomial over GF(2) for some k with 0 < k < n.
> — [OEIS A001153](https://oeis.org/A001153)

Offset 1: 2, 3, 5, 7, 17, 31, 89, 127, 521, 607, 1279, 2281, …

### Python 3 — 186 bytes

```python
k=s=0
while 1:
 p=k+2;j=s and p
 while j<p:a=2;exec("for _ in[0]*p:\n a=int(f'{a:b}',4)\n while h:=a>>p:a^=h<<p^h<<j^h");j+=1+p*(a==2)
 j>p==print(p);k+=1;s=4;exec('s=s*s%~-(4<<k)-2;'*k)
```

**How it works**

- Two tests on each exponent p = k + 2:
  - 2^p − 1 is prime (the Lucas–Lehmer test of
    [A000043](../../A000xxx/A000043/)): `s=4`, then k steps of
    `s=s*s%M-2` with M = `~-(4<<k)` = 2^p − 1. The value stays in [−2, M−3]
    and is 0 exactly when the last residue is 0. If s_{p−2} ≡ 0 (mod M), M is
    prime whether or not p is (the usual proof of that direction does not use
    it), so every p is tested. p = 2 comes from the start `s=0`.
  - some trinomial x^p + x^j + 1 is irreducible over GF(2). Its value at 0 and
    at 1 is 1, so it has no linear factor; then it is irreducible exactly when
    x^(2^p) ≡ x modulo it (it divides x^(2^p) − x, the product of the
    irreducibles of degree 1 and p, p prime). Since 2^p − 1 is prime, x then
    has order 2^p − 1: irreducible means primitive here.
- Polynomials over GF(2) are bit masks. `int(f'{a:b}',4)` squares one: it
  reads the binary digits in base 4, which moves bit i to bit 2i (squaring
  over GF(2) has no cross terms). Then `h=a>>p` is the part of degree ≥ p and
  x^p ≡ x^j + 1 replaces it, until the degree is below p.
- `j=s and p` skips the trinomials when 2^p − 1 is not prime. `j` runs from
  0 (x^p + 1 + 1 = x^p, which always fails); a success adds p + 1, which ends
  the loop with j > p, and `j>p==print(p)` calls `print` only then.

**Notes**

- Exact for every n: integer arithmetic only, and every exponent is tested in
  order, so no term is skipped.
- The bar is 11 terms (up to 1279) in 60 s, about 22 s here, most of it in
  compiling the Lucas–Lehmer `exec` strings. A `for` loop instead of that
  `exec` (4 bytes longer) reaches 1279 in 7 s. The next term, 2281, needs 715
  trinomials of degree 2281 and is out of reach in 60 s.
- Members found by the smallest j ([A074743](https://oeis.org/A074743)): 89
  with j = 38, 521 with 32, 607 with 105, 1279 with 216. The Mersenne
  exponents 13, 19, 61 and 107 have no irreducible trinomial, so all j fail.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 186 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001153), CC BY-SA 4.0.
