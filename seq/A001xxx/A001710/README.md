# A001710

> Order of alternating group A_n, or number of even permutations of n letters.
> — [OEIS A001710](https://oeis.org/A001710)

Offset 0: 1, 1, 1, 3, 12, 60, 360, 2520, 20160, 181440, 1814400, 19958400, …

### Python 3 — 36 bytes

```python
P=n=1
while[print(-~P//2)]:P*=n;n+=1
```

**How it works**

- For n ≥ 2 the even permutations are half of the n! permutations; the
  sequence takes a(0) = a(1) = 1 (the trivial group). Both cases are
  ⌈n!/2⌉, since 0! = 1! = 1 round 1/2 up to 1 and n! is even from n = 2.
- The loop is the factorial loop of [A000142](../../A000xxx/A000142/): on
  the pass with counter n, `P` holds (n − 1)!, and `-~P//2` is
  ⌊(P + 1)/2⌋ = ⌈P/2⌉. The first pass (n = 1, P = 0!) prints a(0).
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- `P-P//2` and `P+1>>1` are the same length as `-~P//2`; `P//2or 1` is two
  bytes longer.
- Exact integers, so every term is right; a(1559) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 101 terms (a(0) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001710), CC BY-SA 4.0.
