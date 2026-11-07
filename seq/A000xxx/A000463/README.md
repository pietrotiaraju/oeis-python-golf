# A000463

> n followed by n^2.
> — [OEIS A000463](https://oeis.org/A000463)

Offset 1: 1, 1, 2, 4, 3, 9, 4, 16, 5, 25, …

### Python 3 — 35 bytes

```python
n=1
while[print(n),print(n*n)]:n+=1
```

**How it works**

- Each pass prints n and then n², so a(2n−1) = n and a(2n) = n².
- Both prints sit in the loop condition: they return `None`, and
  `[None, None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: `[*map(print,(n,n*n))]` in
  the condition ties; one f-string, `print(f'{n}\n{n*n}')`, is 1 byte
  longer; an exponent that alternates between 1 and 2,
  `n=e=1` / `while[print(n**e)]:n+=e>1;e^=3`: 36 bytes; putting the
  increment in the condition, `n=0` / `while[print(n:=n+1),print(n*n)]:0`:
  37 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 10000 terms print in about 0.1 s here. The b-file has 10000
  terms (up to a(10000)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000463), CC BY-SA 4.0.
