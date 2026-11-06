# A000356

> Number of rooted cubic maps with 2n nodes and a distinguished Hamiltonian cycle: (2n)!(2n+1)! / (n!^2*(n+1)!(n+2)!).
> — [OEIS A000356](https://oeis.org/A000356)

Offset 1: 1, 5, 35, 294, 2772, 28314, 306735, 3476330, 40831076, 493684828, 6114096716, 77266057400, …

### Python 3 — 53 bytes

```python
a=1;t=3
while[print(a)]:a=a*16*t*(t:=t+2)//-~t//(t+3)
```

**How it works**

- From the closed form, a(n)/a(n−1) = 4(2n−1)(2n+1)/((n+1)(n+2)).
  With t = 2n−1 this is 16·t·(t+2)/((t+3)(t+5)), and t steps by 2.
- `t*(t:=t+2)` multiplies by t and t + 2 and steps t at once, so the two
  divisors t + 3 and t + 5 of the old t are `-~t` and `t+3` of the new one.
- `a=1;t=3`: a(1) = 1, and the first step (n = 2) uses t = 3.

**Notes**

- The numerator a(n−1)·16t(t+2) equals a(n)·(t+3)(t+5), so it is
  divisible by (t+3)(t+5), and two floor divisions in a row are one exact
  division (`x//p//q` is `x//(p*q)`).
- Alternatives: the same step in n, `n+=1;a=a*(16*n*n-4)//(n+1)//(n+2)`,
  is 56 bytes; dividing by `(t*t+4*t+3)` after the walrus is a byte longer
  than `-~t//(t+3)`; a variable that starts at 1 together with a, such as
  2n − 3, makes the step longer than the 2 bytes it saves.
- Exact integer arithmetic, so the program is right for every n. a(3581)
  is the first term with more than 4300 digits, so Python 3.11+ stops
  there with a `ValueError` from the int-to-str limit, which is not counted
  as a failure.
- The b-file has 800 terms (n = 1 to 800); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000356), CC BY-SA 4.0.
