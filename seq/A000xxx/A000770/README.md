# A000770

> Stirling numbers of the second kind, S(n,6).
> — [OEIS A000770](https://oeis.org/A000770)

Offset 6: 1, 21, 266, 2646, 22827, 179487, 1323652, 9321312, 63436373, 420693273, …

### Python 3 — 63 bytes

```python
L=[s:=1]*5
while[print(s)]:s=j=1;L=[s:=(j:=j+1)*x+s for x in L]
```

**How it works**

- Σ_m S(m+6,6)·xᵐ = 1/((1−x)(1−2x)···(1−6x)). Write h_k(m) for the
  coefficient of xᵐ in the product of the first k factors; then
  H_k = H_{k−1}/(1 − kx) gives h_k(m) = k·h_k(m−1) + h_{k−1}(m), with
  h_1(m) = 1 and h_k(0) = 1. So a(m+6) = h_6(m).
- `L` holds h_2(m), …, h_6(m). Each level needs the level below at the
  same m, so the new row is a running sum: with `s` = h_1 = 1 and `j`
  counting 2, 3, …, 6, `s:=(j:=j+1)*x+s` turns h_{k}(m−1) into h_k(m) and
  keeps it in `s` for the next level. After the comprehension `s` is
  h_6(m), the term to print.
- `L=[s:=1]*5` starts every level at h_k(0) = 1 and sets `s` for the first
  print, S(6,6) = 1.
- The list form beats the unrolled chain of [A000481](../A000481/) here:
  `a=b=c=d=e=1` / `while[print(a)]:e-=~e;d=3*d+e;c=4*c+d;b=5*b+c;a=6*a+b`
  is 65 bytes, and every further column adds 9 more, while the list only
  changes its length ([A000771](../A000771/) is the same 63 bytes).

**Notes**

- Other forms: `s=1;L=[s:=j*x+s for j,x in enumerate(L,2)]` is 4 bytes
  longer than the walrus counter; the inclusion–exclusion formula
  (6ⁿ − 6·5ⁿ + 15·4ⁿ − 20·3ⁿ + 15·2ⁿ − 6)/720 in a `while[print(…)]:n+=1`
  loop is 67 bytes, and reading h_6 off Bⁿ//((B−1)···(B−6)) with
  `math.perm(B-1,6)` and B = 7ⁿ is also 67 (and slow).
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 195 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 5530, so printing stops
  there with a ValueError (about one second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000770), CC BY-SA 4.0.
