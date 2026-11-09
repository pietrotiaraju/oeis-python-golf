# A001311

> Final 2 digits of 6^n.
> — [OEIS A001311](https://oeis.org/A001311)

Offset 0: 1, 6, 36, 16, 96, 76, 56, 36, 16, 96, 76, 56, 36, …

### Python 3 — 28 bytes

```python
n=1
while[print(n%100)]:n*=6
```

**How it works**

- `n` holds 6ⁿ itself, multiplied by 6 at every step, and `n%100` is its
  last two digits read as a number: 6³ = 216 gives 16. Integers are exact,
  so every term is right.
- `print(…)` runs in the loop condition: it returns `None`, and `[None]` is
  a non-empty list, so the loop never ends.

**Notes**

- The same program as [A000855](../../A000xxx/A000855/) (2ⁿ) and
  [A001264](../A001264/) (4ⁿ) with 6 for the base. Keeping only the
  residue, `n=n*6%100`, stays fast forever but is 29 bytes.
- From a(2) on the sequence has period 5 (36, 16, 96, 76, 56), but a
  table of those values is longer than the whole program.
- The price of the big `n` is speed: step k works on a number of about
  2.6k bits; the 1001 b-file terms take well under a second. `n` is never
  turned into a string, so the 4300-digit int-to-str limit does not apply.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001311), CC BY-SA 4.0.
