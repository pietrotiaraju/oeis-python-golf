# A000779

> a(n) = 2*(2n-1)!!-(n-1)!*2^(n-1), where (2n-1)!! is A001147(n).
> — [OEIS A000779](https://oeis.org/A000779)

Offset 1: 1, 4, 22, 162, 1506, 16950, 224190, 3408930, 58596930, 1123663590, …

### Python 3 — 43 bytes

```python
a=e=k=1
while[print(a)]:k+=2;a=a*k+e;e*=k-1
```

**How it works**

- (n−1)!·2ⁿ⁻¹ = 2·4·6···(2n−2) is the even double factorial (2n−2)!!, so
  a(n) = 2·(2n−1)!! − (2n−2)!!: twice the product of the odd numbers up to
  2n − 1, minus the product of the even numbers up to 2n − 2.
- Write e = (2n−2)!!. Since (2n+1)!! = (2n+1)·(2n−1)!! and
  (2n)!! = 2n·e, a(n+1) = (2n+1)·(a(n) + e) − 2n·e =
  (2n+1)·a(n) + e. So only the term and the even product are kept.
- `k` is the odd number 2n − 1: `k+=2` makes it 2n + 1, `a=a*k+e` is the
  step above with the old e, and `e*=k-1` multiplies in 2n.
- At n = 1 everything is 1: a(1) = 2·1 − 1, e = 0!! = 1 (the empty
  product), k = 1.

**Notes**

- Keeping both products, `d=e=k=1` / `while[print(2*d-e)]:k+=2;d*=k;e*=k-1`,
  is 44 bytes: the step is 3 bytes shorter but the print 4 longer. An even
  counter (`k=2n`) needs `k=0` or `k=2` in the start and is longer.
- Exact integer arithmetic, correct for every n.
- The b-file has 250 terms (up to a(250)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 1424, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000779), CC BY-SA 4.0.
