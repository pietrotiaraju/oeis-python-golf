# A000449

> Rencontres numbers: number of permutations of [n] with exactly 3 fixed points.
> — [OEIS A000449](https://oeis.org/A000449)

Offset 3: 1, 0, 10, 40, 315, 2464, 22260, 222480, 2447445, 29369120, …

### Python 3 — 54 bytes

```python
d=m=0;c=1
while[print(c*(d:=d*m^1))]:m+=1;c=c*(m+3)//m
```

**How it works**

- Choose the 3 fixed points and derange the other n − 3 elements:
  a(n) = C(n, 3)·D(n−3), with D the derangement numbers
  [A000166](../A000166/). The loop runs m = n − 3 = 0, 1, 2, …
- `d` is D(m) by the [A000166](../A000166/) update: D(m) = m·D(m−1) +
  (−1)^m, and m·D(m−1) has the parity of m (D(k) ≡ k+1 (mod 2) by
  induction), so adding (−1)^m is the same as `^1`. At m = 0 the update
  gives 0^1 = 1 = D(0) whatever d was, so the walrus inside the print
  starts the sequence with no separate first term.
- `c` is C(m+3, 3): C(m+3, 3) = C(m+2, 3)·(m+3)/m, and `c*(m+3)//m` is
  exact because the quotient is the next binomial coefficient.
- `while[print(…)]:` prints first in every pass, so the product
  printed with m = 0 is C(3,3)·D(0) = 1 = a(3).

**Notes**

- The recurrence a(n) = n·a(n−1) − (−1)ⁿ·C(n,3), as
  `a=1;n=3` / `while[print(a)]:n+=1;a=n*a-(-1)**n*n*(n-1)*(n-2)//6`, is 59
  bytes. Building C(m+3, 3) by running sums (`b-=~m;c+=b`) ties at 54.
  [A000475](../A000475/) (4 fixed points) would take the same program
  with `c*(m+4)//m`.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The b-file has 98 terms (up to
  a(100)); the bar is the whole b-file in 60 s.
- a(1558) has 4299 digits and a(1559) more than 4300, so the int-to-str
  limit stops the printing after a(1558).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 59 | first entry |
| 2026-11-07 | Python 3 | 54 | C(m+3,3)·D(m) with the start-early `d*m^1` walrus |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000449), CC BY-SA 4.0.
