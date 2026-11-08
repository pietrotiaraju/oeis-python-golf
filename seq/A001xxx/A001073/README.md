# A001073

> Label a 1-cm ruler with digits 1 cm wide.
> — [OEIS A001073](https://oeis.org/A001073)

Offset 0: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 2, 1, 4, 1, 6, 1, 8, …

### Python 3 — 40 bytes

```python
l=[0]
for c in l:print(c);l+=str(len(l))
```

**How it works**

- The labels are written one after another along the ruler, each at the
  first free centimetre: 0, …, 9, then 10 (which also covers cm 11), 12,
  …, 98, then 100 (covering 101 and 102), 103, … The term a(n) is the
  digit at cm n.
- Since the labels fill the ruler with no gaps, the next label is always
  the number of digits written so far. So the list `l` of digits grows by
  `str(len(l))`: `+=` with a string appends its characters one by one.
- The loop prints the list while it grows: each pass prints one digit and
  appends at least one, so `for c in l:` never runs out. The first entry is
  the int 0 and the rest are one-character strings; `print` shows both the
  same way.

**Notes**

- About 7 digits are appended per digit printed once the labels have 7
  digits, so the list stays a few times longer than the output.
- The b-file has 10001 terms (n = 0..10000); they print at once, and the
  bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001073), CC BY-SA 4.0.
