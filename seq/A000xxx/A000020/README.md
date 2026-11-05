# A000020

> Number of primitive polynomials of degree n over GF(2) (version 2).
> — [OEIS A000020](https://oeis.org/A000020)

Offset 1: 2, 1, 2, 2, 6, 6, 18, 16, 48, 60, 176, 144, 630, 756, 1800, 2048, …

### Python 3 — 83 bytes

```python
import math
n=1
while[print(sum(math.gcd(k,2**n-1)<2for k in range(2**n))//n)]:n+=1
```

**How it works**

- A primitive polynomial of degree n is the minimal polynomial of a generator
  of the cyclic group GF(2ⁿ)*, which has order 2ⁿ − 1 and so φ(2ⁿ − 1)
  generators. Each polynomial has n roots, all generators (the conjugates
  α, α², α⁴, …), so for n > 1 the count is **φ(2ⁿ − 1)/n**. The division is
  exact: 2 has order n modulo 2ⁿ − 1, so n divides φ(2ⁿ − 1).
- φ(m) is counted directly as the k with gcd(k, m) = 1. The range runs over
  `range(2**n)`, that is 0…m: for n > 1 the two extra values k = 0 and k = m
  both have gcd m > 1 and drop out.
- For n = 1, m = 1 and both k = 0 and k = 1 have gcd 1, so the program prints
  2. That is the "version 2" convention of this entry, which counts x and
  x + 1 ([A011260](https://oeis.org/A011260) is the version starting with 1),
  and it comes out of the range for free.
- `import math` with `math.gcd` is 1 byte shorter than `from math import*`
  with `gcd` here, since `gcd` appears only once.
- `while[print(...)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true, and it saves a byte over `while 1:print(...);`.

**Notes**

- Term n costs 2ⁿ gcds, so the program prints 25 terms in a minute. The bar
  is 24 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000020), CC BY-SA 4.0.
