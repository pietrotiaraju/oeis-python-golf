# A000461

> Concatenate n n times.
> — [OEIS A000461](https://oeis.org/A000461)

Offset 1: 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999, 10101010101010101010, …

### Python 3 — 31 bytes

```python
n=1
while[print(str(n)*n)]:n+=1
```

**How it works**

- `str(n)*n` repeats the decimal string of n n times, which is the decimal
  string of a(n); for n = 10 it is ten copies of `10`. The string never
  starts with 0, so printing it is the same as printing the integer.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: `'%d'%n*n` or `f'{n}'*n` tie;
  the original `n=0` / `while 1:n+=1;print(str(n)*n)`: 32 bytes. The
  numeric form n·(10^(dn) − 1)/(10^d − 1), d = number of digits of n, is
  longer and would run into the 4300-digit int-to-str limit at n = 1076.
- Exact: the output is built as text, never as an integer, so it is right
  for every n and the 4300-digit int-to-str limit does not apply.
- The b-file's 333 terms print in 0.1 s here; the time per term grows
  with the output length n·d, about 20000 terms in 20 s. The b-file has 333
  terms (up to a(333)); the bar is the whole b-file in 60 s.
- [A000422](../A000422/) concatenates n, n−1, …, 1 instead.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |
| 2026-11-07 | Python 3 | 31 | `while[print(…)]:` loop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000461), CC BY-SA 4.0.
