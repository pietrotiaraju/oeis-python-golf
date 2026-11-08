# A001058

> 1-digit numbers in reverse alphabetical order, then 2-digit numbers, etc.
> — [OEIS A001058](https://oeis.org/A001058)

Offset 1: 0, 2, 3, 6, 7, 1, 9, 4, 5, 8, 22, 23, 26, 27, 21, 29, 24, 25, 28, 20, …

### Python 3 — 395 bytes

```python
from unicodedata import*
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+'HUNDRED THOUSAND M B TR QUADR QUINT SEXT SEPT OCT NON %UN%DUO%TRE%QUATTUOR%QUIN%SEX%SEPTEN%OCTO%NOVEM%VIGINT'.replace('%','DEC ').split()[e//3]+'ILLION'*(e>3)+f(n%10**e)or n and name(chr([n+119520,n//10+65807][t:=n>19]))[14:]+f(n%10*t)or''
d=1
while[*map(print,[0]*(d<2)+sorted(range(d,d*10),key=f)[::-1])]:d*=10
```

**How it works**

- This is [A000052](../../A000xxx/A000052/) (the same blocks in
  alphabetical order) read backwards block by block, and the program is
  that page's program with the last line changed: each block of d-digit
  numbers, d = 1, 10, 100, …, is sorted by name and printed reversed
  (`[::-1]`).
- `f(n)` is the US English name of n in capitals with spaces and hyphens
  left out, f(726) = `SEVENHUNDREDTWENTYSIX`, built from Unicode character
  names: `chr(119520+n)` is MAYAN NUMERAL ONE … NINETEEN and
  `chr(65807+t)` is AEGEAN NUMBER TWENTY … NINETY, and `[14:]` cuts both
  14-character prefixes. From 100 on, f(n) = f(n // 10^e) + scale word +
  f(n % 10^e) with e the exponent of the largest scale word that fits:
  HUNDRED, THOUSAND, then MILLION … VIGINTILLION (`%` expands to `DEC `
  in the word list). The A000052 page explains each piece.
- Zero: f(0) is the empty string (so that remainders of 0 add nothing),
  which would sort first and so print last. ZERO is the last 1-digit name
  alphabetically (after TWO), so reversed it comes first:
  `[0]*(d<2)+` puts it in front of the first block.

**Which names, and where the sequence ends**

- US names without "and" (101 is "one hundred one"), as the entry's
  comment says, compared letter by letter with spaces and hyphens ignored,
  as on the A000052 page; there it is shown where the hyphen would matter
  (from the 5-digit numbers on, e.g. 80000 against 83000).
- The scale words go up to vigintillion (10^63), the last of the standard
  dictionary names before centillion, so the sequence is taken to end with
  the 66-digit numbers; at 10^66 the word list lookup fails with an
  `IndexError` and the program stops.
- Each block is sorted in memory: the 6-digit block (900000 names) takes
  about 18 s and 130 MB, and the 7-digit block would hold 9·10^6 names.

**Notes**

- The OEIS has no b-file for this entry. The one here has 10000 terms
  (all numbers up to 4 digits): each block of the A000052 b-file, reversed.
  Its first 72 terms are exactly the entry's data. The program prints them
  in about 0.3 s, and the bar is the whole b-file.
- `sorted(…,reverse=1)` costs 4 bytes more than `[::-1]`; there are no
  ties to break, since no two numbers have the same name.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 395 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001058), CC BY-SA 4.0.
