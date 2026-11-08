# A001047

> a(n) = 3^n - 2^n.
> — [OEIS A001047](https://oeis.org/A001047)

Offset 0: 0, 1, 5, 19, 65, 211, 665, 2059, 6305, 19171, …

### Python 3 — 32 bytes

```python
n=0
while[print(3**n-2**n)]:n+=1
```

**How it works**

- The counter n starts at 0 and the program prints the definition
  `3**n-2**n` directly; Python's integers are exact, so there is nothing
  to round.
- `while[print(…)]:` prints in the loop condition: `print` returns `None` and
  the one-element list `[None]` is true.

**Notes**

- Two running powers, `a=b=1` / `while[print(a-b)]:a*=3;b*=2`, cost 33
  bytes; the recurrences a(n) = 3a(n−1) + 2ⁿ⁻¹ and a(n) = 5a(n−1) − 6a(n−2)
  need two variables as well and are longer still.
- Recomputing both powers is a few big-integer multiplications per term,
  far below the bar.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s.
- a(9013) is the first term with more than 4300 digits (4301) and Python's
  int-to-str limit stops the printing there; a(9012) has 4300.
- Related: [A000244](../../A000xxx/A000244/) 3ⁿ and
  [A000079](../../A000xxx/A000079/) 2ⁿ.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001047), CC BY-SA 4.0.
