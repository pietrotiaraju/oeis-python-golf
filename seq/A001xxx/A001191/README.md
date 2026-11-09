# A001191

> Digits of positive squares.
> — [OEIS A001191](https://oeis.org/A001191)

Offset 1: 1, 4, 9, 1, 6, 2, 5, 3, 6, 4, 9, 6, 4, 8, 1, 1, …

### Python 3 — 41 bytes

```python
n=1
while[print(*str(n*n),sep='\n')]:n+=1
```

**How it works**

- Print the decimal digits of 1², 2², 3², … one per line:
  `print(*str(n*n),sep='\n')` splits the string into its characters.

**Notes**

- The whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001191), CC BY-SA 4.0.
