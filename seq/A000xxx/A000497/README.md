# A000497

> S2(j,2j+2) where S2(n,k) is a 2-associated Stirling number of the second kind.
> — [OEIS A000497](https://oeis.org/A000497)

Offset 1: 1, 25, 490, 9450, 190575, 4099095, 94594500, 2343240900, 62199262125, 1764494857125, …

a(n) is the number of ways to split 2n + 2 labelled elements into n blocks,
each of size at least 2.

### Python 3 — 44 bytes

```python
f=m=3
while[print((m**3-m)*f//72)]:m+=2;f*=m
```

**How it works**

- With n blocks of size ≥ 2 on 2n + 2 elements there are two elements beyond
  n pairs: either one block of size 4 and n − 1 pairs, or two blocks of size 3
  and n − 2 pairs. Counting each case,
  a(n) = (2n+2)!/(4!·2^(n−1)(n−1)!) + (2n+2)!/(3!²·2!·2^(n−2)(n−2)!),
  which simplifies to a(n) = n(n+1)(2n+1)·(2n+1)!!/18 (the same as Vaclav
  Kotesovec's Γ formula in the entry; at n = 1 only the first case exists and
  the closed form still gives 1).
- With m = 2n + 1, n(n+1)(2n+1) = (m³ − m)/4, so
  a(n) = (m³ − m)·m!!/72. The program steps m = 3, 5, 7, … and keeps
  `f` = m!! (`f*=m` after `m+=2`); `f=m=3` starts both at n = 1.
- The `//72` is exact because the quotient is the integer a(n): no
  rounding is involved.

**Notes**

- Other versions that print the same terms: `f=m=3` with
  `f*m*(m*m-1)//72`, 45 bytes; `f=m=1` / `while 1:m+=2;f*=m;print(…)`,
  45 bytes; a walrus `(f:=f*m)` inside the print, 48 bytes; R. J. Mathar's
  ratio recurrence (2n−1)(n−1)a(n) = (n+1)(2n+1)²a(n−1),
  `a=n=1` / `while[print(a)]:n+=1;a=a*(n+1)*(2*n+1)**2//((2*n-1)*(n-1))`,
  64 bytes.
- Exact integer arithmetic, so the program is right for every n. The closed
  form agrees with the associated Stirling recurrence
  S2(n, k) = k·S2(n−1, k) + (n−1)·S2(n−2, k−1) for n = 1..7.
- The b-file has 100 terms (up to a(100)); the bar is the whole b-file in
  60 s. All of it prints in 0.1 s here.
- a(1421) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there, after about 0.4 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 64 | first entry |
| 2026-11-07 | Python 3 | 44 | closed form (m³ − m)·m!!/72 with m = 2n + 1 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000497), CC BY-SA 4.0.
