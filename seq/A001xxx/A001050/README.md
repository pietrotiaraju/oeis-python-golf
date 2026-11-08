# A001050

> Number of letters in n (in Finnish).
> — [OEIS A001050](https://oeis.org/A001050)

Offset 0: 5, 4, 5, 5, 5, 5, 5, 9, 9, 8, 8, 10, 11, 11, 11, 11, 11, 15, 15, 14, …

### Python 3 — 226 bytes

```python
f=lambda n:n>99and f(q:=n//10**(e:=((g:=~-len(str(n))//3)&~(g>3))*3or 2))+b'579999::======<<;;;;;;'[g]-48-(q<2)*(5+(g==1))+f(n%10**e)or n>19and f(n//10)+8+f(n%10)or b'04555559988:;;;;;??>'[n]-48
n=0
while[print(f(n)or 5)]:n+=1
```

**How it works**

- `f(n)` is the number of letters of the Finnish name of n, with f(0) = 0
  so that a zero remainder adds nothing; the loop prints `f(n)or 5`, since
  0 alone is *nolla*. Only lengths are needed, never the words.
- Below 20 the lengths come from a table, `b'04555559988:;;;;;??>'[n]-48`:
  yksi 4, kaksi 5, …, seitsemän 9, kahdeksan 9, yhdeksän 8, kymmenen 8,
  then the teens with *-toista* (yksitoista 10, …, yhdeksäntoista 14).
  From 20 to 99 the tens add *kymmentä* (8 letters): kaksikymmentäkolme =
  f(2) + 8 + f(3).
- From 100 on, n = q·10^e + r with 10^e the largest scale word that fits,
  and the name is that of q, the scale word (in the partitive after
  q ≥ 2: *sata*/*sataa*, *tuhat*/*tuhatta*, *miljoona*/*miljoonaa*), then
  the name of r. One of each is said without *yksi*: 100 is *sata*,
  1000 *tuhat*, 10^6 *miljoona*. The table `b'579999::======<<;;;;;;'`
  holds the partitive lengths, and for q = 1 the program takes off the 4
  letters of *yksi* plus the partitive ending (1 letter, or 2 for
  *tuhatta*): `-(q<2)*(5+(g==1))`.
- The table is indexed by g, the number of digits minus one, divided by 3.
  Finnish uses the long scale: *miljoona* 10^6, *miljardi* 10^9,
  *biljoona* 10^12, *triljoona* 10^18, *kvadriljoona* 10^24, …,
  *dekiljoona* 10^60, and 10^15 is *tuhat biljoonaa*, so from g = 4 on the
  scale exponent is 6·⌊g/2⌋, while up to *miljardi* it is 3g (2 for the
  hundreds). `(g&~(g>3))*3or 2` gives both: g&~1 clears the low bit when
  g > 3.

**Which names, and where the sequence ends**

- The spelling follows the entry's example and the OEIS b-file
  (0..20000), which agree with these rules: numbers written as one word
  (the letter count is the same if *miljoona* and the larger words are
  written apart), no *yksi* before *sata*, *tuhat* or a big scale word.
- The scale words are the standard ones listed under "Suurten lukujen
  nimet" in the Finnish Wikipedia, *miljoona* through *dekiljoona* (10^60);
  the 10^54 word is spelled *noniljoona* or *noviljoona*, both with 10
  letters. The forms *biljardi*, *triljardi* are proposals that are not
  standard. Past *dekiljoona* there is no standard word, so the sequence
  is taken to end with the 66-digit numbers: at n = 10^66 the table lookup
  fails with an `IndexError` and the program stops. Up to there the counts
  are exact for every n (checked against a word-by-word speller on random
  numbers of every length up to 66 digits).

**Notes**

- `~` on a bool gives a `DeprecationWarning` on stderr in Python 3.12; it
  still means `~1` = −2.
- The b-file has 20001 terms; they print in well under a second, and the
  bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 226 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001050), CC BY-SA 4.0.
