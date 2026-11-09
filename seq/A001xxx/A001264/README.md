# A001264

> Final 2 digits of 4^n.
> — [OEIS A001264](https://oeis.org/A001264)

Offset 0: 1, 4, 16, 64, 56, 24, 96, 84, 36, 44, 76, 4, 16, 64, …

### Python 3 — 28 bytes

```python
n=1
while[print(n%100)]:n*=4
```

**How it works**

- `n` holds 4ⁿ itself, multiplied by 4 at every step, and `n%100` is its
  last two digits read as a number: 4¹¹ = 4194304 gives 4, written `4` and
  not `04`, as in the data and the b-file. Integers are exact, so every
  term is right.
- `print(…)` runs in the loop condition: it returns `None`, and `[None]` is
  a non-empty list, so the loop never ends.

**Notes**

- The same program as [A000855](../../A000xxx/A000855/) (final two digits
  of 2ⁿ) with 4 for 2. Keeping only the residue, `n=n*4%100`, stays fast
  forever but is 29 bytes.
- From a(1) on the sequence has period 10 (4¹¹ ≡ 4 mod 100), but a table
  of those ten values is longer than the whole program.
- The price of the big `n` is speed: step k works on a 2k-bit number, so
  the program slows down as it goes; the 1001 b-file terms still take
  well under a second. `n` is never turned into a string, so the
  4300-digit int-to-str limit does not apply.
- The b-file has 1001 terms (up to a(1000)); the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001264), CC BY-SA 4.0.
