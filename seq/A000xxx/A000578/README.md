# A000578

> The cubes: a(n) = n^3.
> — [OEIS A000578](https://oeis.org/A000578)

Offset 0: 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, …

### Python 3 — 27 bytes

```python
n=0
while[print(n**3)]:n+=1
```

**How it works**

- `n**3` is the cube, printed for n = 0, 1, 2, …
- `while[print(…)]:` never ends: `print` returns `None` and `[None]` is a
  non-empty list (the [A000007](../A000007/) loop), a byte under `while 1:`
  plus a separate `print(…);`.

**Notes**

- Other versions that print the same terms: `n*n*n`: 28 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10001 terms (up to a(10000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.2 s here.
- a(n) has about 3·log10(n) digits, so the 4300-digit int-to-str limit is
  far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000578), CC BY-SA 4.0.
