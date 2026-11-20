# A001924

> Apply partial sum operator twice to Fibonacci numbers.
> — [OEIS A001924](https://oeis.org/A001924)

Offset 0: 0, 1, 3, 7, 14, 26, 46, 79, 133, 221, 364, 596, 972, 1581, 2567, 4163, 6746, …

### Python 3 — 40 bytes

```python
a=b=c=0
while[print(a:=b-a)]:c+=1;b+=a+c
```

**How it works**

- **Closed form.** The partial sums of F(0), F(1), … are F(k + 2) − 1, and
  summing those again gives a(n) = F(n + 4) − n − 3 (the entry's formula),
  so a(n + 1) = a(n) + a(n − 1) + n + 1.
- **Program.** Call the printed values x₀, x₁, … and the values of `b` and
  `c` after pass n bₙ and cₙ = n + 1 (`c` is raised before it is used). The
  program sets xₙ₊₁ = bₙ − xₙ and bₙ = bₙ₋₁ + xₙ + cₙ. As
  xₙ = bₙ₋₁ − xₙ₋₁, this is xₙ₊₁ = bₙ₋₁ + n + 1 = xₙ + xₙ₋₁ + n + 1, the
  same recurrence.
- **Start.** `a=b=c=0` gives x₀ = 0, then c = 1, b = 1 and x₁ = 1: a(0) = 0
  and a(1) = 1, so xₙ = a(n) for every n.

**Notes**

- The third-order recurrence a(n) = 2a(n − 1) − a(n − 3) + 1 from three
  zeros, `a,b,c=b,c,c-~c-a` as in [A000126](../../A000xxx/A000126/), is
  40 bytes as well.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001924), CC BY-SA 4.0.
