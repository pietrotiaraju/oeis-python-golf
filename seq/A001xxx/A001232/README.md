# A001232

> Numbers k such that 9*k = (k written backwards), k > 0.
> — [OEIS A001232](https://oeis.org/A001232)

Offset 1: 1089, 10989, 109989, 1099989, 10891089, 10999989, 108901089, 109999989, 1089001089, 1098910989, 1099999989, …

### Python 3 — 67 bytes

```python
k=1
while[str(x:=99*int(f'{k:b}'))[::-1]!=f'{9*x}'or print(x)]:k+=1
```

**How it works**

- Every term is 99·m where m's decimal digits are all 0 or 1: the OEIS
  entry states this as a theorem (David W. Wilson, 1997: the terms are
  exactly 99·m for palindromic 0/1 strings m with no isolated digit; see
  also N. J. A. Sloane, "2178 And All That", *Fibonacci Quarterly* 52
  (2014), on reverse multiples). The program uses only the half "every
  term is 99 times a 0/1 number" and tests the definition itself on those
  candidates, so it prints exactly the terms.
- `int(f'{k:b}')` reads the binary digits of k as a decimal number; for
  k = 1, 2, 3, … this lists every 0/1 number in increasing order (equal
  lengths compare the same way in both bases). Each x = 99·m is tested
  directly: `str(x)[::-1]` against `f'{9*x}'`.

**Notes**

- The candidates double with each extra digit while the terms grow like
  Fibonacci numbers of half the length, so the terms slow down: about 460
  in 30 s here. The b-file has 10000 terms; the bar is 400 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001232), CC BY-SA 4.0.
