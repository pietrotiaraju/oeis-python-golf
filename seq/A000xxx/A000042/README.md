# A000042

> Unary representation of natural numbers.
> — [OEIS A000042](https://oeis.org/A000042)

Offset 1: 1, 11, 111, 1111, 11111, 111111, …

### Python 3 — 28 bytes

```python
s='1'
while[print(s)]:s+='1'
```

**How it works**

- a(n) is n written in base 1: the digit 1 repeated n times, which as a
  decimal number is the repunit (10ⁿ − 1)/9.
- The program never does arithmetic. `s` is the string `'1'`, and each pass
  of the loop prints it and appends one more `'1'`.
- `print(s)` runs in the loop condition. It returns `None`, and `[None]` is a
  non-empty list, so the condition is always true. It is the
  [A000027](../A000027/) loop with `n+=1` replaced by `s+='1'`.

**Notes**

- `n=1` + `while[print(n)]:n=n*10+1`, `n=0` + `while 1:print(n:=n*10+1)`,
  `s=''` + `while 1:print(s:=s+'1')` and `n=1` + `while[print('1'*n)]:n+=1`
  are also 28 bytes. The integer versions stop with a `ValueError` after
  term 4300, at the 4300-digit int-to-str limit of Python 3.11+. Strings
  have no such limit, so this version keeps going.
- `print(10**n//9)` (31 bytes with the loop) also works, because 10ⁿ ≡ 1
  (mod 9).
- The b-file has 1000 terms and the whole of it prints instantly; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000042), CC BY-SA 4.0.
