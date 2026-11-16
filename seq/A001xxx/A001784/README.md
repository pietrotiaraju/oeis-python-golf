# A001784

> Second-order reciprocal Stirling number (Fekete) a(n) = [[2n+3, n]]. The number of n-orbit permutations of a (2n+3)-set with at least 2 elements in each orbit. Also known as associated Stirling numbers of the first kind (e.g., Comtet).
> — [OEIS A001784](https://oeis.org/A001784)

Offset 0: 1, 24, 924, 26432, 705320, 18858840, 520059540, 14980405440, 453247114320, 14433720701400, …

### Python 3 — 67 bytes

```python
d=j=3
while[print(d*(j-3)*~-j*(10*j*j+15*j-1)//1620or 1)]:j+=2;d*=j
```

**How it works**

- [[m, k]] counts permutations of m points with k cycles, all of length
  ≥ 2. For m = 2n + 3 and k = n the lengths exceed 2 by 3 in total, so the
  cycle type is 5·2ⁿ⁻¹, 4·3·2ⁿ⁻², or 3³·2ⁿ⁻³ (one 5-cycle and n − 1
  transpositions, and so on). A cycle type with c_ℓ cycles of length ℓ has
  m!/∏(ℓ^c_ℓ·c_ℓ!) permutations, so
  a(n) = m!/(2ⁿ(n−1)!)·(2/5 + (n−1)/3 + 4(n−1)(n−2)/81)
  = m!/(2ⁿ(n−1)!)·(20n² + 75n + 67)/405, Kotesovec's formula in the entry
  (the terms of the types that do not exist for n = 1, 2 vanish).
- m!/(2ⁿ(n−1)!) = 2n(n+1)·(2n+3)!!, and with j = 2n + 3 everything is a
  polynomial in j times d = j!!:
  a(n) = d(j−3)(j−1)(10j² + 15j − 1)/1620. The loop starts at `d=j=3`
  (n = 0) and does `j+=2;d*=j`; the quotient is an integer, so `//1620` is
  exact.
- For n = 0 the definition gives [[3, 0]] = 0 (three points cannot form no
  cycles), and so does the formula, but the entry lists a(0) = 1 (all its
  programs special-case it). The program follows the data: `or 1` turns that
  single zero into 1, every later term being positive. (`1620or` is fine:
  only a literal starting with 0 would read as an octal prefix.)

**Notes**

- a(1419) is the first term over 4300 digits, where Python's int-to-str
  limit stops the program.
- Straight from the recurrence of the definition (see
  [A001785](../A001785/)), with four entries per row instead of five, is
  74 bytes.
- The b-file has 16 terms (a(0) to a(15)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001784), CC BY-SA 4.0.
