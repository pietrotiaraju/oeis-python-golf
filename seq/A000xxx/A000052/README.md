# A000052

> 1-digit numbers arranged in alphabetical order, then the 2-digit numbers arranged in alphabetical order, then the 3-digit numbers, etc.
> — [OEIS A000052](https://oeis.org/A000052)

Offset 1: 8, 5, 4, 9, 1, 7, 6, 3, 2, 0, 18, 80, 88, 85, 84, 89, 81, 87, 86, 83, 82, 11, 15, 50, …

### Python 3 — 389 bytes

```python
from unicodedata import*
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+'HUNDRED THOUSAND M B TR QUADR QUINT SEXT SEPT OCT NON %UN%DUO%TRE%QUATTUOR%QUIN%SEX%SEPTEN%OCTO%NOVEM%VIGINT'.replace('%','DEC ').split()[e//3]+'ILLION'*(e>3)+f(n%10**e)or n and name(chr([n+119520,n//10+65807][t:=n>19]))[14:]+f(n%10*t)or''
d=1
while[*map(print,sorted(range(d,d*10),key=f)+[0]*(d<2))]:d*=10
```

**How it works**

- `f(n)` is the US English name of n with the spaces and hyphens taken out,
  in capitals: f(726) = `SEVENHUNDREDTWENTYSIX`. The loop sorts each block
  of d-digit numbers, d = 1, 10, 100, …, by that key and prints it.
- The words come from Unicode character names. `chr(119520+n)` is
  MAYAN NUMERAL ONE … NINETEEN for n = 1..19, and `chr(65807+t)` is
  AEGEAN NUMBER TWENTY … NINETY for t = 2..9. Both prefixes are 14
  characters long, so `[14:]` leaves the word. Below 100, `t=n>19` picks the
  Aegean tens word and then adds `f(n%10)` for the units, or the Mayan word
  for 1..19 and then adds `f(0)`. `n and…or''` makes f(0) the empty string,
  so a zero remainder adds nothing: f(20) = `TWENTY`, f(100) = `ONEHUNDRED`.
- From 100 on, `e` is the exponent of the largest scale word that fits:
  `~-len(str(n))//3*3` is the number of digits minus one, rounded down to a
  multiple of 3, and `or 2` turns the 0 of the 3-digit numbers into 2. Then
  f(n) = f(n // 10^e) + word + f(n % 10^e), the US way: f(1005000) =
  `ONEMILLIONFIVETHOUSAND`.
- The words list is indexed by e//3: HUNDRED (e = 2), THOUSAND (3), then
  the roots M, B, TR, …, VIGINT (6, 9, …, 63) with `ILLION` added when e > 3.
  `%` expands to `DEC `, so `NON %UN%DUO%` reads `NON DEC UNDEC DUODEC`.
- Zero is the one number whose name is not used: f(0) is empty and would
  sort first, but ZERO comes after TWO, last of the 1-digit names. So the
  first block sorts 1..9 and `+[0]*(d<2)` appends the 0.
- `while[*map(print,…)]:` prints the block; the list is never empty, so the
  loop goes on to the next block.

**Which names, and where the sequence ends**

- US names, so no "and": 101 is "one hundred one", as the OEIS comments say.
  The order is letter by letter, ignoring spaces: the b-file has
  a(1003) = 8018 ("eight thousand eighteen") before a(1004) = 8800 ("eight
  thousand eight hundred"). The program ignores hyphens as well. The b-file
  stops at the 4-digit numbers and cannot tell, but from a(18001) on the
  hyphen matters: ignoring it puts 80000 ("eighty thousand") before 83000,
  while keeping it, as the OEIS Python program does through num2words,
  puts "eighty-three thousand" first because `-` sorts before letters.
- The scale words are the standard dictionary names, million through
  vigintillion (10^63), with the dictionary spellings sexdecillion and
  novemdecillion (see
  [Names of large numbers](https://en.wikipedia.org/wiki/Names_of_large_numbers)).
  The Conway–Guy system writes sedecillion instead, and that changes the
  order: 20·10^51 ("twenty sedecillion") would come before 27·10^51
  ("twenty-seven …"), while "twenty sexdecillion" comes after it.
- After vigintillion the dictionaries jump to centillion (10^303). Names in
  between, such as "unvigintillion" for 10^66, come only from naming
  systems, so this page takes the sequence to end with the 66-digit
  numbers, after 10^66 terms. There the program stops: for 10^66, e = 66
  and the list lookup fails with an `IndexError`. Up to that point the
  names, and so the order, are exact for every n.
- Each block is sorted in memory, which is the real limit: 10^6 terms take
  about 26 s, the 7-digit block holds 9·10^6 names at once, and the
  10-digit block would need 9·10^9. The bar is the whole b-file (10000
  terms), which prints in about 0.3 s.

**Notes**

- The scale words cost 119 bytes: with only HUNDRED, THOUSAND and MILLION in
  the list the program is 270 bytes, but it would stop at the 10-digit
  numbers, and the sequence goes on to 66 digits.
- Spelling out the 27 words one … nineteen, twenty … ninety takes a
  178-character string on its own; the import and the two `name(chr(…))`
  calls take about 70 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 389 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000052), CC BY-SA 4.0.
