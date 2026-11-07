# A000422

> Concatenation of numbers from n down to 1.
> — [OEIS A000422](https://oeis.org/A000422)

Offset 1: 1, 21, 321, 4321, 54321, 654321, 7654321, 87654321, 987654321, 10987654321, …

### Python 3 — 38 bytes

```python
n=s=1
while[print(s)]:n+=1;s=f'{n}{s}'
```

**How it works**

- a(n) is the decimal text of n followed by that of a(n − 1), so the program
  keeps the term as a string and prepends the new number:
  `s=f'{n}{s}'`. Crossing a digit boundary needs nothing special:
  "10" + "987654321" is a(10).
- s starts as the integer 1 = a(1). The f-string turns both parts into text,
  so the first step gives the string '21' and s stays a string from then on;
  `str(n)+s` would fail on the integer start.
- `while[print(s)]:` prints in the loop condition: `print` returns `None`
  and `[None]` is true.

**Notes**

- `s='';n=0` with `while 1:print(s:=str(n:=n+1)+s)`: 40 bytes.
- The terms are built and printed as strings, never as integers, so the
  program is right for every n and Python's 4300-digit int-to-str limit does
  not apply.
- a(n) has about n·log₁₀ n digits, so the time goes into copying and
  printing ever longer strings: about 32700 terms in 60 s here (a(32704) has
  152414 digits).
- The b-file has 150 terms (up to a(150)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 40 | first entry |
| 2026-11-07 | Python 3 | 38 | start from the integer 1 and prepend with an f-string |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000422), CC BY-SA 4.0.
