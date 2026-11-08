# A001102

> Numbers k such that k / (sum of digits of k) is a square.
> — [OEIS A001102](https://oeis.org/A001102)

Offset 1: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, 81, 100, 144, 150, 192, 200, 225, …

### Python 3 — 87 bytes

```python
k=0
while 1:k+=1;s=sum(map(int,str(k)));sum(k%m<1for m in range(s,k+1,s))%2>0==print(k)
```

**How it works**

- The [A001101](../A001101/) count: with s the digit sum of k, the number
  of multiples m of s, from s up to k, that divide k is 0 when s does not
  divide k and d(k/s), the number of divisors of q = k/s, when it does.
- q is a square exactly when d(q) is odd: the divisors pair off as d and
  q/d, and only d = √q is its own partner. So the count is odd exactly when
  k/s is a square integer, with no square root at all.
- The square 1 counts, so 1 to 9 (k = s) are terms.
- `X%2>0==print(k)` is the chain `X%2>0 and 0==print(k)`: `print(k)` only
  runs for an odd count.

**Notes**

- Other versions that print the same terms: an integer square root,
  `import math` + `k%s<1>k//s-math.isqrt(k//s)**2==print(k)`, 92 bytes and
  about ten times as many terms in the same time; keeping a set of the
  squares up to k, `S|={i*i}` with `i+=k>i*i`, also 92 bytes. The float
  test `(k//s)**.5%1` would be shorter but is not exact once q passes 2⁵³,
  so it is not used.
- Correct for every k straight from the definition.
- The count takes about k/s steps for every k, so the run time grows like
  k²: about 290 terms (up to 106032) come out in 60 s here, and the 220th
  term, 53371, after about 16 s. The b-file has 10000 terms (up to
  222278520); the bar is 220 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001102), CC BY-SA 4.0.
