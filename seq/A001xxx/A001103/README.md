# A001103

> Numbers k such that (k / product of digits of k) is 1 or a prime.
> — [OEIS A001103](https://oeis.org/A001103)

Offset 1: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 24, 36, 115, 175, 212, 624, 735, 816, 1115, …

### Python 3 — 93 bytes

```python
k=0
while 1:k+=1;p=eval('*'.join(str(k)))or-1;0<sum(k%m<1for m in range(p,k+1,p))<3==print(k)
```

**How it works**

- `eval('*'.join(str(k)))` is the product of the digits: 115 becomes the
  expression `1*1*5`.
- The [A001101](../A001101/) count with p in place of the digit sum: the
  number of multiples m of p, from p up to k, that divide k is 0 when p
  does not divide k and d(k/p), the number of divisors of k/p, when it
  does. k/p is 1 or a prime exactly when d(k/p) is 1 or 2, which is the
  chain `0<X<3`, and `<3==print(k)` prints only then.
- A zero digit makes the product 0, k/0 is undefined, and such k are not
  terms. `or-1` turns that 0 into −1, and `range(-1,k+1,-1)` is empty, so
  the count is 0: no zero step, no division by zero.
- The product of the digits is never more than k (the leading digit
  times at most 9 for each further digit), so the range always reaches p.
  [A001104](../A001104/) is the same program with the parity of the count.

**Notes**

- Another version that prints the same terms: `from math import*` with
  `prod(map(int,str(k)))`, 110 bytes.
- Correct for every k straight from the definition.
- Speed: compiling the `eval` string for every k is the main cost. About
  105 terms (up to 739935) come out in 60 s here, and the 90th term,
  313173, after about 20 s. The b-file has 12677 terms (up to
  998222413824); the bar is 90 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001103), CC BY-SA 4.0.
