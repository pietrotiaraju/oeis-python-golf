# A000004

> The zero sequence.
> — [OEIS A000004](https://oeis.org/A000004)

Offset 0: 0, 0, 0, 0, 0, …

### Python 3 — 16 bytes

```python
while 1:print(0)
```

**How it works**

Prints 0 forever. `while 1:` is the shortest infinite loop, and the body has
to be on the same line to avoid an indentation byte.

**Notes**

- `for _ in iter(int,1):print(0)` loops over the endless zeros that `int()`
  returns, but is longer (29 bytes).
- Anything built from `print(*...)` or `'0\n'*k` either stops after a finite
  number of terms or never prints, because the whole argument is built first.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 16 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000004), CC BY-SA 4.0.
