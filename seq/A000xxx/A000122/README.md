# A000122

> Expansion of Jacobi theta function theta_3(x) = Sum_{m =-oo..oo} x^(m^2)
> (number of integer solutions to k^2 = n).
> — [OEIS A000122](https://oeis.org/A000122)

Offset 0: 1, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, …

### Python 3 — 40 bytes

```python
k=0
while[print('12'[k>0]+'\n0'*k)]:k+=2
```

**How it works**

- a(n) counts the integers k with k² = n: one (k = 0) for n = 0, two
  (±√n) when n is a nonzero square, none otherwise.
- So the sequence splits into blocks: `1` for n = 0, then for each
  m ≥ 1 a `2` at n = m² followed by 2m zeros for m² < n < (m+1)², since
  (m+1)² − m² − 1 = 2m.
- `k` runs through 0, 2, 4, … and each `print` writes one whole block:
  the leading digit, then `'\n0'*k`, that is k more lines holding 0.
  `'12'[k>0]` picks `1` for the first block (k = 0, no zeros) and `2`
  for all the others.
- The loop is the [A000027](../A000027/) one: `print` returns `None`,
  `[None]` is a non-empty list and so always true, and the body steps `k`.
- Only string repetition and integer steps are involved, so every term is
  exact, for every n.

**Notes**

- Putting the zeros before each `2` instead,
  `k=-2` + `while[print('0\n'*k+'12'[k>-1])]:k+=2`, is 42 bytes: a
  negative repeat count gives the empty string, so k = −2 prints just the
  `1` and k = 0 just the first `2`.
- Printing a(0) on its own, `print(1);k=0` +
  `while[print('0\n'*k+'2')]:k+=2`, is 43 bytes, as is growing the block
  as a string, `print(1);s='2'` + `while[print(s)]:s='0\n0\n'+s`.
- `while 1:print(…);k+=2` is 1 byte longer than the `while[print(…)]`
  form.
- Testing each n with `n**.5%1` is not exact: for large n the float
  square root of m² + 1 rounds to m, so a non-square would print 2.
- The b-file has the 10 001 terms a(0)..a(10000), all printed in well
  under a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000122), CC BY-SA 4.0.
