# A000425

> Coefficients of ménage hit polynomials.
> — [OEIS A000425](https://oeis.org/A000425)

Offset 1: 2, 0, 0, 8, 30, 192, 1344, 10800, 97434, 976000, …

### Python 3 — 57 bytes

```python
a=b=n=1;c=0
while[print(2*n*b)]:a,b,c=-b,c,n*(b+c)-a;n+=1
```

**How it works**

- Let W_m be the straight-table ménage number
  [A000271](../A000271/). The circular ménage hit polynomial is
  U_n(t)=Σₖ₌₀ⁿ 2n/(2n−k)·C(2n−k,k)(n−k)!(t−1)ᵏ.
  This sequence is its coefficient of t.
- Taking that coefficient gives a factor (−1)^(k−1)k.
  Put j=k−1 and simplify the factorials; the result is

  a(n)=2n·Σⱼ₌₀ⁿ⁻¹ (−1)ʲ C(2n−j−2,j)(n−j−1)!
  =2n·W_(n−1).

- At a print the state is
  (a,b,c)=(−W_(n−2),W_(n−1),W_n). The recurrence
  W_(n+1)=n(W_n+W_(n−1))+W_(n−2) therefore becomes
  `a,b,c=-b,c,n*(b+c)-a`, followed by the counter increment.
- Initially n=1, b=W_0=1 and c=W_1=0. The auxiliary a=1
  makes the first update produce W_2=0; later updates use the
  ordinary recurrence. The output `2*n*b` starts at 2,0,0,8.

**Notes**

- **Index correction.** The unshifted conjecture a(n)=2n·W_n
  on the OEIS page is off by one. Extracting the coefficient proves
  the shifted identity above; for n=1 it gives 2W_0=2.
- The state and recurrence proof are explained in
  [A000271](../A000271/). Storing the oldest term with a minus
  sign permits the shorter initialization `a=b=n=1`.
- Exact integer arithmetic and three stored recurrence values.
  Changing A000271's `print(b)` to `print(2*n*b)` accounts
  for the 4-byte increase from its 53-byte program.
- Factorial growth eventually reaches Python 3.11+'s default
  4300-digit integer-to-string limit, an interpreter limit.
- The b-file has 22 terms (indices 1 through 22). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000425), CC BY-SA 4.0.
