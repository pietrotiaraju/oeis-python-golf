# A000128

> A nonlinear binomial sum.
> — [OEIS A000128](https://oeis.org/A000128)

Offset 1: 1, 2, 4, 8, 16, 31, 58, 105, 185, 319, 541, 906, 1503, 2476, 4058, …

### Python 3 — 47 bytes

```python
a=b=d=x=1
while[print(x)]:d+=b-1;x+=d;a,b=b,a+b
```

**How it works**

- This is Lind's 5th-order sum L(n, 5) (Fib. Quart. 3, 1965): the first
  five entries of row n − 1 of Pascal's triangle plus the "stairstep"
  diagonal after them,
  L(n, 5) = Σᵢ₌₀⁴ C(n−1, i) + Σⱼ≥₁ C(n−j−1, j+4).
- The diagonal is the tail of the Fibonacci diagonal sum
  F(n+4) = Σᵢ C(n+3−i, i) from i = 5 on (put i = j + 4). Its head
  Σᵢ₌₀⁴ C(n+3−i, i) minus Σᵢ₌₀⁴ C(n−1, i) is 3 + (2n − 1) + C(n−1, 2), so

  **a(n) = F(n+4) − n(n+1)/2 − 3**

  for every n ≥ 1 (Ralf Stephan's formula on the OEIS page).
- Taking differences: a(n) − a(n−1) = F(n+2) − n (A000126 shifted by one), and
  the next difference is F(n) − 1 (A000071). The program sums twice:
  `a, b` are F(n), F(n+1), `d` is F(n+2) − n and `x` is a(n).
  `d+=b-1` steps `d` to F(n+3) − (n+1), `x+=d` gives a(n+1), and
  `a,b=b,a+b` moves the Fibonacci pair on.
- At n = 1 all four are 1: F(1) = F(2) = 1, F(3) − 1 = 1 and a(1) = 1, so
  the start is `a=b=d=x=1`.
- `while[print(x)]:` prints the current term in the loop condition: the
  one-element list `[None]` is always true, and it is one byte shorter than
  `while 1:print(x);`.

**Notes**

- Exact integer arithmetic and a proved identity, so the program is right
  for every n. 2000 terms also agree with Lind's double sum computed
  directly.
- The same 47 bytes with the order-3 recurrence of the differences
  (see [A000126](https://oeis.org/A000126)), d(n) = 2d(n−1) − d(n−3) + 1:
  `a=b=c=x=1` + `while[print(x)]:x+=c;a,b,c=b,c,c-~c-a`.
- A Fibonacci pair with a counter, `x+=b-n;n+=1`, is 48 bytes, and printing
  `b-n*-~n//2-3` straight from the closed form is 53.
- Three variables with an affine update cannot do it: the sequence has
  characteristic polynomial (x² − x − 1)(x − 1)³, degree 5, and a 3×3
  affine map only reaches degree 4.
- The b-file has the 201 terms a(1)..a(201), all printed at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000128), CC BY-SA 4.0.
