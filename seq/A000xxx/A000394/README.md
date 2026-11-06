# A000394

> Numbers of form x^2 + y^2 + 7z^2.
> — [OEIS A000394](https://oeis.org/A000394)

Offset 0: 0, 1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, …

### Python 3 — 75 bytes

```python
s={n:=0}
while[s&{n-j-7*k for j in s for k in s}and print(n)]:n+=1;s|={n*n}
```

**How it works**

- `s` is the set of squares 0², 1², …, n², which contains every square up
  to n. n = x² + y² + 7z² has a solution exactly when n − y² − 7z² is in
  `s` for some squares y², z² in `s`, so the program builds the set of all
  n − j − 7k and prints n when it meets `s`.
- Negative values of n − j − 7k never meet `s`, and squares above n give
  negative values only, so keeping all of them is harmless.
- `s={n:=0}` starts the set and the counter together; each pass adds the
  next square with `s|={n*n}`.

**Notes**

- Exact integers, a direct test of the definition. The form is not regular
  (3, 6, 14, 19, 21, 22, 31, … are missing in no simple pattern), so there
  is no congruence test to replace the search.
- `any(n-j-7*k in s for j in s for k in s)` with a list `s` is 5 bytes
  longer, and a list with `{…}&{*s}` 2 bytes longer.
- Term n looks at (n + 1)² pairs, so the program prints about 450 terms in
  20 s. The b-file is the 60 terms of the OEIS entry (up to 72); the bar is
  all 60 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000394), CC BY-SA 4.0.
