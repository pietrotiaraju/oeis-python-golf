# A000378

> Sums of three squares: numbers of the form x^2 + y^2 + z^2.
> — [OEIS A000378](https://oeis.org/A000378)

Offset 1: 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, …

### Python 3 — 52 bytes

```python
n=0
while[n//(p:=n&-n or 1)%8-p%3>5or print(n)]:n+=1
```

**How it works**

- Legendre's three-square theorem (proved by Gauss): n ≥ 0 is a sum of three
  squares exactly when n is not of the form 4ᵃ(8b + 7). The program prints
  every n that is not.
- Write n = p·t with p = `n&-n` the largest power of 2 dividing n and t odd.
  n is of the form 4ᵃ(8b + 7) exactly when t ≡ 7 (mod 8) and p is a power
  of 4, that is p mod 3 = 1 (an odd power of 2 is 2 mod 3).
- `n//p%8-p%3>5` tests both at once: t mod 8 is 1, 3, 5 or 7 and p mod 3 is
  1 or 2, so the difference is 6 only for t ≡ 7 with p mod 3 = 1, and at
  most 5 otherwise. When it is false, `or print(n)` prints n.
- At n = 0, `n&-n` is 0; `or 1` makes p = 1, so the test is 0 − 1 > 5,
  false, and 0 is printed. That is 3 bytes under a separate `print(n:=0)`.

**Notes**

- Exact integer arithmetic; correctness for every n is Legendre's theorem.
  The output was also compared with a brute force over x² + y² + z² up to
  20000.
- `n%(8*p)>6*p` for the first half of the test is the same idea in more
  bytes, and the `p:=` walrus inside `n//(…)` costs the same as a separate
  `p=n&-n or 1;` in a `while 1:` body (52 bytes too).
- Brute force over the squares (as in [A000164](../A000164/)) is longer and
  far slower.
- The b-file has 10000 terms (up to 11994) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000378), CC BY-SA 4.0.
