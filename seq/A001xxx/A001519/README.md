# A001519

> a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1.
> — [OEIS A001519](https://oeis.org/A001519)

Offset 0: 1, 1, 2, 5, 13, 34, 89, 233, 610, 1597, 4181, 10946, 28657, 75025, …

### Python 3 — 31 bytes

```python
a=b=1
while[print(a)]:b-=a;a-=b
```

**How it works**

- a(n) = F(2n − 1), the odd-indexed Fibonacci numbers (with F(−1) = 1):
  F(m + 2) = 3F(m) − F(m − 2) follows from applying F(k+1) = F(k) + F(k−1)
  twice, and a(0) = F(−1) = 1, a(1) = F(1) = 1.
- Before a(n) is printed, `a` = F(2n − 1) and `b` = −F(2n − 2). Then
  `b-=a` makes b = −(F(2n − 2) + F(2n − 1)) = −F(2n), and `a-=b` makes
  a = F(2n − 1) + F(2n) = F(2n + 1): two Fibonacci steps per term.
- Keeping the even-indexed numbers negated lets the start be `a=b=1`:
  F(−1) = 1 and −F(−2) = −(−1) = 1.

**Notes**

- With positive Fibonacci numbers the start needs a zero, `a=1;b=0` /
  `while[print(a)]:a+=b;b+=a`, 33 bytes; the pair update `a=b=1` /
  `a,b=b,3*b-a` is 33 too. A search over all two-variable programs with one
  or two in-place statements (coefficients up to 6, starts −3 to 9) found
  nothing shorter than 31.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 10300.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001519), CC BY-SA 4.0.
