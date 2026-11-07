# A000496

> Restricted permutations.
> — [OEIS A000496](https://oeis.org/A000496)

Offset 0: 1, 1, 2, 6, 24, 44, 80, 144, 260, 476, …

The entry counts restricted permutations from N. S. Mendelsohn, *Permutations
with confined displacements* (Canad. Math. Bull. 4, 1961). Beyond the listed
data, the program follows Simon Plouffe's generating function, which the
OEIS marks as conjectured (see Notes).

### Python 3 — 57 bytes

```python
a=[*b',P\x90']
for x in a:print(x);a+=sum(a[-3:])-8,
```

The bytes literal holds five raw control bytes (0x01, 0x01, 0x02, 0x06 and
0x18) that a browser does not show. Byte for byte, the first line is

```text
a=[*b'<01><01><02><06><18>,P\x90']
```

where `<01>` stands for the single byte 0x01, and so on. With those bytes
escaped, `a=[*b'\1\1\2\6\30,P\x90']`, the program is 63 bytes.

**How it works**

- Plouffe's g.f. for the tail is
  Σ_{m≥0} a(m+4)xᵐ = N(x)/((1 − x)(1 − x − x² − x³)) with
  N(x) = 24 − 4x − 8x² − 16x³ − 4x⁴ (the denominator multiplies out to
  1 − 2x + x⁴).
- Split off the pole at x = 1: N(1)/(1 − 1 − 1 − 1) = 4, so N(x) =
  4(1 − x − x² − x³) + (1 − x)R(x) with R of degree 3, and the g.f. is
  4/(1 − x) + R(x)/(1 − x − x² − x³). The coefficients of R/(1 − x − x² − x³)
  obey the tribonacci recurrence from index 4 on, so b(n) = a(n) − 4 satisfies
  b(n) = b(n−1) + b(n−2) + b(n−3) for n ≥ 8, that is,
  **a(n) = a(n−1) + a(n−2) + a(n−3) − 8 for n ≥ 8.**
  It fails at n = 7 (80 + 44 + 24 − 8 = 140, not 144), so the seeds are
  a(0), …, a(7): 1, 1, 2, 6 from the data and 24, 44, 80, 144, the first four
  coefficients of the g.f.
- `[*b'…']` unpacks the bytes literal into a list of ints: the five control
  bytes are 1, 1, 2, 6, 24, then `,` is 44, `P` is 80 and `\x90` is 144.
- `for x in a:` walks a list that grows while it is read: the list iterator
  sees the appended items, so the loop never ends. When x = a(k) is printed,
  the list holds a(0), …, a(k+7), and `a+=sum(a[-3:])-8,` appends a(k+8)
  from its last three entries.

**Notes**

- Other versions: the same program with a plain list
  `a=[1,1,2,6,24,44,80,144]` is 62 bytes, with escaped bytes 63; nine seeds
  with the order-4 recurrence a(n) = 2a(n−1) − a(n−4) (n ≥ 9),
  `a=[1,1,2,6,24,44,80,144,260]` / `while[print(a.pop(0))]:a+=[2*a[-1]-a[-4]]`,
  70 bytes.
- Correctness: the arithmetic is exact, so the program prints the
  coefficients of Plouffe's g.f. for every n. That these are Mendelsohn's
  counts beyond the data is the conjecture the OEIS records (Plouffe 1992);
  the 1001-term b-file agrees with it. The count is not the circulant
  permanent with displacements 0, 1, 2, 3 mod n: that matches up to n = 7 and
  then gives 264 at n = 8.
- The list keeps every term, which costs nothing at these sizes. The b-file
  has 1001 terms (up to a(1000)); the bar is the whole b-file in 60 s. All of
  it prints in 0.1 s here.
- a(16247) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there, after about 4 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |
| 2026-11-07 | Python 3 | 57 | tribonacci − 8 form, seeds as raw bytes, growing-list loop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000496), CC BY-SA 4.0.
