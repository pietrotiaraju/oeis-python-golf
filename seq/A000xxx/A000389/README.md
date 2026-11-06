# A000389

> Binomial coefficients C(n,5).
> — [OEIS A000389](https://oeis.org/A000389)

Offset 0: 0, 0, 0, 0, 0, 1, 6, 21, 56, 126, 252, 462, 792, 1287, 2002, …

### Python 3 — 44 bytes

```python
m=2
while[print(m*(5*m*m-m**4-4)//120)]:m-=1
```

**How it works**

- C(n, 5) is the product of the five consecutive integers n − 4 … n over 120.
  Centred at k = n − 2 the product is (k−2)(k−1)k(k+1)(k+2) = k(k² − 1)(k² − 4)
  = k(k⁴ − 5k² + 4), with no k⁴ or k² terms left over.
- The program uses m = 2 − n, which counts down from 2. Then k = −m and the
  product is −m(m⁴ − 5m² + 4) = m(5m² − m⁴ − 4), so `m*(5*m*m-m**4-4)` is
  120·C(n, 5). Counting down from 2 is a byte under counting up from −2 with
  `(m**4-5*m*m+4)*m`.
- The product of five consecutive integers is divisible by 120, so `//120`
  is exact. For n = 0 … 4 one of the factors is 0, which gives the five
  leading zeros with no special case.

**Notes**

- `import math` + `n=0` + `while[print(math.comb(n,5))]:n+=1` is 49 bytes.
  The fifth base-2^n digit of (2^n + 1)^n, `(2**n+1)**n>>5*n&2**n-1`, is 46
  (each C(n, k) < 2^n for n ≥ 1, so the digits do not carry). The factored
  `(m*m-1)*(m*m-4)*m` is 46, and the expanded `(5*m**3-m**5-4*m)` is 45.
- Five running sums, `a=b=c=d=e=0` + `while[print(e)]:e+=d;d+=c;c+=b;b+=a;a+=1`
  (e = C(n, 5), d = C(n, 4), …, a = n), is 52.
- Exact integers, so every term is right; the int-to-str limit would only be
  reached for n of about 10^860.
- The b-file has 1001 terms (n = 0 to 1000) and prints at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000389), CC BY-SA 4.0.
