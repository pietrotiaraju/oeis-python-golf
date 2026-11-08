# A001104

> Numbers k such that k / product of digits of k is a square.
> — [OEIS A001104](https://oeis.org/A001104)

Offset 1: 1, 2, 3, 4, 5, 6, 7, 8, 9, 135, 144, 384, 1575, 1715, 6144, 6912, 11664, 14112, …

### Python 3 — 93 bytes

```python
k=0
while 1:k+=1;p=eval('*'.join(str(k)))or-1;sum(k%m<1for m in range(p,k+1,p))%2>0==print(k)
```

**How it works**

- The [A001103](../A001103/) program with the
  [A001102](../A001102/) test: p is the product of the digits
  (`eval('*'.join(str(k)))`), and the number of multiples m of p, from p
  up to k, that divide k is 0 when p does not divide k and d(k/p) when it
  does.
- k/p is a square exactly when d(k/p) is odd (divisors pair off as d and
  (k/p)/d, except √(k/p)), so `X%2>0==print(k)` prints exactly the terms.
  The square 1 counts, so 1 to 9 are terms.
- A zero digit makes p = 0 and such k are not terms; `or-1` turns it into
  −1, `range(-1,k+1,-1)` is empty and the count 0 is even.

**Notes**

- Correct for every k straight from the definition.
- The terms thin out fast: the 32nd is 371112, the next ones are
  1168128 and 2214144, and the b-file's 1000 terms (Bert Dobbelaere) reach
  1.7·10¹⁹, far beyond a brute force over k; p is always 7-smooth, so a
  faster program would build k = p·m² from p = 2ᵃ3ᵇ5ᶜ7ᵈ instead. Here
  32 terms come out in 60 s and the 31st, 248832, after about 15 s; the
  bar is 31 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001104), CC BY-SA 4.0.
