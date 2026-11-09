# A001196

> Double-bitters: only even length runs in binary expansion.
> — [OEIS A001196](https://oeis.org/A001196)

Offset 0: 0, 3, 12, 15, 48, 51, 60, 63, 192, 195, 204, 207, 240, 243, 252, 255, …

### Python 3 — 40 bytes

```python
n=0
while[print(3*int(f'{n:b}',4))]:n+=1
```

**How it works**

- Doubling every bit of n gives the n-th number whose binary runs all
  have even length, in order: bit bᵢ of n becomes the pair bᵢbᵢ, worth
  3·bᵢ·4ⁱ.
- `int(f'{n:b}',4)` reads the binary digits of n in base 4 (Σ bᵢ·4ⁱ), and
  `3*` doubles each bit.

**Notes**

- The whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001196), CC BY-SA 4.0.
