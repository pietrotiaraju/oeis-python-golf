# A001355

> Mix digits of Pi and e.
> — [OEIS A001355](https://oeis.org/A001355)

Offset 1: 3, 2, 1, 7, 4, 1, 1, 8, 5, 2, 9, 8, 2, 1, 6, 8, 5, 2, 3, 8, 5, 4, …

### Python 3 — 136 bytes

```python
t=l=N=F=Q=1;y=4
while y%t<Q*F or-N%F<=Q or[print(y//t),y:=y%t*10,print(N//F),N:=N%F*10,Q:=Q*10]:l+=2;y=y*l-2*Q*F;t*=l;N=l//2*N+Q;F*=l//2
```

**How it works**

The terms alternate the digits of π (odd n) and of e (even n): 3, 2, 1, 7,
4, 1, 1, 8, … Two exact unbounded spigots run side by side, the one of
[A000796](../../A000xxx/A000796/) for π and the one of
[A001113](../A001113/) for e, and each pass of the loop takes one more
term of both series. A pair of digits is printed only when both are
certain.

- **π** (Gibbons' spigot): π = 2 + 1/3·(2 + 2/5·(2 + 3/7·(2 + …))), and
  step k = `l//2` (with `l` = 2k + 1) is the map x ↦ 2 + k·x/(2k + 1). The
  digits still to come are those of f(x) = (q·x + y − 4q)/t, where x, the
  rest of the series, lies in [3, 4]. When y mod t ≥ q, f(3) = (y − q)/t
  and f(4) = y/t have the same integer part y // t, which is then the next
  digit; printing it replaces f by 10(f − digit), so q gains a factor 10
  and y becomes 10·(y mod t). A step multiplies q by k and t by 2k + 1 and
  sets y to y·(2k + 1) − 2q.
- **e**: after k steps N/F = 10^d·(1/0! + 1/1! + … + 1/k!) minus the d
  digits already printed, with F = k! and Q = 10^d. The rest of the
  series, 10^d·(1/(k+1)! + …), is below 10^d/k! = Q/F, so when
  F − (N mod F) > Q (`-N%F>Q`) the next digit is certainly N // F;
  printing it multiplies N mod F and Q by 10. A step adds the term
  Q/k!: N becomes k·N + Q and F becomes k·F.
- **One variable less.** π's q starts at 1, gains a factor k per step and
  a factor 10 per digit. Since the two spigots print their digits
  together, F = k! and Q = 10^d give exactly q = Q·F, so the program
  writes `Q*F` and never keeps q.
- **The loop.** The condition is true while either digit is uncertain;
  otherwise it prints the π digit, then the e digit, and the list it
  builds is non-empty, so the loop goes on in every case and the body
  always takes one more step of both series. A digit that is certain stays
  certain as the intervals shrink, so waiting for the other spigot is
  harmless; the e series gains more than a digit per step, π about 0.3,
  so it is π that sets the pace.

**Notes**

- Exact: a digit is printed only when the whole interval known to contain
  the constant gives it, and since π and e are irrational the interval
  always ends up inside one digit, so none is held back forever. Each
  printed value is one digit, so the 4300-digit int-to-str limit never
  applies.
- The numbers grow by about log₁₀(2k + 1) and log₁₀ k digits per step:
  by term 10000 (5000 digits of each, about 16600 steps) t and F have
  around 70000 and 62000 digits, and the program slows down roughly
  quadratically.
- The bar is the whole b-file (10000 terms) in 60 s; they take about 25 s
  on a machine some two times slower than the reference.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 136 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001355), CC BY-SA 4.0.
