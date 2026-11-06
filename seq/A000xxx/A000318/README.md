# A000318

> Generalized tangent numbers d(4,n).
> — [OEIS A000318](https://oeis.org/A000318)

Offset 1: 4, 128, 16384, 4456448, 2080374784, 1483911200768, …

### Python 3 — 73 bytes

```python
r=[0,s:=4]
while[print(s)]:
 for s in 0,0:r=[s:=s+x*4for x in[0]+r[::-1]]
```

**How it works**

- The OEIS entry gives a(n) = 2^(4n−2)·[A000182](../A000182/)(n), and
  Luschny's form (2n−1)!·[x^(2n−1)] sec 4x·sin 4x says the same thing:
  the e.g.f. is tan 4x, so a(n) = 4^(2n−1) times the tangent number.
- The program runs the Seidel–Entringer (boustrophedon) triangle of
  [A000111](../A000111/) with weight 4, as [A000187](../A000187/) and
  [A000191](../A000191/) do with weights 5 and 3: T(0,0) = 1,
  T(m,0) = 0 for m ≥ 1 and T(m,k) = T(m,k−1) + 4·T(m−1,m−k). Multiplying
  row m of the unweighted triangle by 4^m gives exactly this recursion, so
  T(m,m) = 4^m·A000111(m), the coefficient of x^m/m! in sec 4x + tan 4x.
  The odd rows carry tan 4x: T(2n−1,2n−1) = a(n).
- Each pass of the `while` computes two rows, an even one and an odd one.
  `s` is the `for` target, so it is 0 when each comprehension starts; the
  `[0]` in front of the reversed row makes the first entry s + 0 = 0, and
  the walrus carries the running sum. After the odd row `s` is its last
  entry, a(n), which the next `while` header prints.
- The program starts from row 1 = [0, 4] with s = a(1) = 4.
- `x*4for` saves the space of `4*x for`; the `SyntaxWarning` for `4for`
  goes to stderr.

**Notes**

- Exact integer arithmetic, correct for every n.
- The tangent program of [A000182](../A000182/) with the factor as a shift,
  `print(t<<2*len(r)-2)`, is 78 bytes; scaling the stored rows with
  `r=[4*(t:=t+x)for x in[-t]+r[::-1]]` and two steps per pass with
  `exec("…;"*2)` is 78 too. The parity test of A000182 cannot pick the odd
  rows here, since every term is even.
- Row m has m + 1 entries, so a(n) costs about 4n² big-integer additions.
  The whole b-file (100 terms) prints in well under a second; the program
  stops after a(691), when the next term passes the 4300-digit int-to-str
  limit of Python 3.11+. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000318), CC BY-SA 4.0.
