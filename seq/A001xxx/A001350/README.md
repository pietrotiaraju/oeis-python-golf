# A001350

> Associated Mersenne numbers.
> — [OEIS A001350](https://oeis.org/A001350)

Offset 0: 0, 1, 1, 4, 5, 11, 16, 29, 45, 76, 121, 199, 320, 521, 841, 1364, 2205, …

### Python 3 — 42 bytes

```python
a=c=0;b=1
while[print(a)]:a,b=b,a+b+c;c^=2
```

**How it works**

- a(n) = L(n) − 1 − (−1)ⁿ with L the Lucas numbers (Fischer's formula in
  the entry; it is −(φⁿ − 1)(ψⁿ − 1) for the roots φ, ψ of x² − x − 1).
  Since L(n) = L(n−1) + L(n−2) and the correction 1 + (−1)ⁿ is 2 for even n
  and 0 for odd n, the terms obey
  a(n) = a(n−1) + a(n−2) + 1 − (−1)ⁿ, i.e. they add 2 exactly when n is
  odd.
- `a,b` are a(n), a(n+1); the update makes a(n+2) = a(n) + a(n+1) + c
  with `c` = 2·[n odd]. `c` starts at 0 (n = 0 is even) and `c^=2` flips it
  between 0 and 2 every step.

**Notes**

- Lucas numbers with the correction in the print,
  `a=c=2;b=1` / `while[print(a-c)]:a,b=b,a+b;c^=2`, are also 42 bytes;
  the walrus form `a=b=-1;c=2` / `while[print(a:=b-a)]:b+=a+c;c^=2` is 43,
  and printing two terms per pass from the bisections
  (`a+=b;b+=a+2` on (L(2k) − 2, L(2k+1))) is 44.
- No two-variable linear update can do it: the terms need the roots φ, ψ
  and −1 (plus the constant), three dimensions besides the constant.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (a(0) to a(1000)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001350), CC BY-SA 4.0.
