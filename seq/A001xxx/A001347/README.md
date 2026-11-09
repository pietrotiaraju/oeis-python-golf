# A001347

> a(n) = Sum_{k=0..5} (n+k)! * C(5,k).
> — [OEIS A001347](https://oeis.org/A001347)

Offset -1: 88, 326, 1631, 10112, 74046, 622704, 5900520, 62118720, 718709040, 9059339520, …

For n ≥ 0, a(n) = n! + 5·(n+1)! + 10·(n+2)! + 10·(n+3)! + 5·(n+4)! +
(n+5)!. At n = −1 the k = 0 term would be (−1)!, so the sum does not define
a(−1); the OEIS gives a(−1) = 88, which is the sum with (−1)! read as −1:
−1 + 5·0! + 10·1! + 10·2! + 5·3! + 4! = 88.

### Python 3 — 66 bytes

```python
g=1;x=4
while[print(g*(x*~-x*(x*x-9)+5)+g//(x-4or-1))]:x+=1;g*=x-4
```

**How it works**

- Write j = n + 1. Dividing each (j−1+k)! by (j−1)! leaves a rising
  product, so for j ≥ 1 a(j−1) = (j−1)! + j!·R(j) with
  R(j) = j⁴ + 15j³ + 75j² + 145j + 89 = (j+1)(j+3)(j+4)(j+7) + 5.
- The loop counter `x` is j + 4 = n + 5, which centres R:
  (j+1)(j+7) = x² − 9 and (j+3)(j+4) = x(x−1), so R = x(x−1)(x² − 9) + 5,
  `x*~-x*(x*x-9)+5` (`~-x` is x − 1).
- `g` is j! (it starts at 0! = 1 and `g*=x-4` multiplies by the new j).
  For j ≥ 1, (j−1)! = j!/j is `g//(x-4)`, an exact division.
- At j = 0, x − 4 is 0 and `or` falls back to −1, so the last term is
  1//−1 = −1: that is (−1)! read as −1, and the print gives
  4·3·7 + 5 − 1 = 88 = a(−1). No term is stored.
- `print` returns `None` and `[None]` is truthy, so the loop never ends.
  Exact integers, so every term is right. (`4or` makes Python warn about
  the number literal on stderr; it still parses as `4 or`.)

**Notes**

- The same (−1)! reading gives a(−1) = 2, 7, 23 in
  [A001344](../A001344/), [A001345](../A001345/) and
  [A001346](../A001346/); 88 is also a(−1) + a(0) = 23 + 65 of A001346.
- Keeping (j−1)! and j! in two variables
  (`f=-1;g=1;x=4` / `...print(f+g*(...))]:x+=1;f,g=g,g*(x-4)`) is 67
  bytes. The form of [A001344](../A001344/), which stores a(−1) in
  `f=88` and fixes it with `f=f*(x-4)or 1`, is 69 with this counter, 70
  counting by j with `-~n*(n+3)*(n+4)*(n+7)+5`, and 73 with Horner's
  `(((n+15)*n+75)*n+145)*n+89`.
- Python's 4300-digit int-to-str limit stops the program at a(1554), the
  first term with more than 4300 digits, after printing a(−1) to a(1553).
- The b-file has 102 terms (n = −1 to 100); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001347), CC BY-SA 4.0.
