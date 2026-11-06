# A000422

> Concatenation of numbers from n down to 1.
> — [OEIS A000422](https://oeis.org/A000422)

Offset 1: 1, 21, 321, 4321, 54321, 654321, 7654321, 87654321, 987654321, 10987654321, …

### Python 3 — 40 bytes

```python
s='';n=0
while 1:print(s:=str(n:=n+1)+s)
```

**How it works**

Keep the concatenation as a string. Before each output, increment n
and prepend its decimal representation. All component numbers are
positive, so no leading zero appears; printing the string is exactly
the required integer representation and avoids integer conversion limits.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 150 terms in 60 s; the official b-file contains 150 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000422), CC BY-SA 4.0.
