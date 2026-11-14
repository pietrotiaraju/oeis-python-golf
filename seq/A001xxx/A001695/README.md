# A001695

> a(n) = H_n(2,n) where H_n is the n-th hyperoperator.
> — [OEIS A001695](https://oeis.org/A001695)

Offset 0: 1, 3, 4, 8, 65536

### Python 3 — 86 bytes

```python
H=lambda n,y:n<3and y+[1,2,y][n]or y<1or H(n-1,H(n,y-1))
n=0
while[print(H(n,n))]:n+=1
```

**How it works**

- **The hyperoperators with base 2.** H(n, y) is H_n(2, y) in the
  convention of [A054871](https://oeis.org/A054871): H_0(2, y) = y + 1,
  H_1(2, y) = 2 + y, H_2(2, y) = 2·y, and for n ≥ 3, H_n(2, 0) = 1 and
  H_n(2, y) = H_(n−1)(2, H_n(2, y−1)). So H_3(2, y) = 2^y, H_4(2, y) is a
  tower of y twos, and a(n) = H(n, n) gives 0+1 = 1, 2+1 = 3, 2·2 = 4,
  2³ = 8 and 2^2^2^2 = 65536.
- **Closed forms for n < 3.** `y+[1,2,y][n]` is y+1, y+2, y+y, which is
  what the same recursion gives from H_0 with the bases H_1(2, 0) = 2,
  H_2(2, 0) = 0 (induction on y). Recursing down to the successor instead
  would take over a billion steps and a recursion 65534 deep for a(4); with
  H_0 to H_2 in closed form, a(4) = H_4(2, 4) = H_3(2, 16) is 16 steps of
  H_2.
- **The short-circuits are safe.** For n ≥ 3 and y = 0, `y<1or …` returns
  True, which Python uses as 1 in arithmetic; it is only ever passed on as
  an argument (H(3, 1) = H(2, True) = True + True = 2), and the printed
  H(n, n) for n ≥ 3 comes out of H(2, ·) or H(n−1, ·) as an int.
  `n<3and … or …` would fall through if the closed form were 0, which
  happens only for H(2, 0); that call never occurs, since the outer call
  for n = 2 is H(2, 2) and the recursion only calls H(n−1, v) with
  v = H(n, y−1) ≥ 1.

**Notes**

- **Only five terms can be printed.** a(5) = H_5(2, 5) =
  H_4(2, H_5(2, 4)), and H_5(2, 4) = H_4(2, H_5(2, 3)) = H_4(2, 65536), a
  tower of 65536 twos: its fifth storey 2^65536 already has 19729 digits
  and the next one, 2^(2^65536), has more bits than there are atoms in the
  universe. The program stops there on an interpreter limit: right after
  a(4) it descends H_4(2, 65536) → H_4(2, 65535) → … and Python raises a
  RecursionError; with no recursion limit it would run out of memory
  instead. The program is still right for every n in the sense of the
  definition; it is the values that cannot exist in any computer.
- The b-file has the five terms; the bar is all five, in 60 s, and they
  come at once.
- Five terms fit in a table shorter than any program, so this record needs
  a review: the program computes each term from the definition, with
  nothing stored but the three closed forms of H_0, H_1 and H_2.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001695), CC BY-SA 4.0.
