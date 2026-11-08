# A001061

> 1-, 2-, 3-, ... digit numbers in alphabetical order in German.
> — [OEIS A001061](https://oeis.org/A001061)

Offset 1: 8, 3, 1, 5, 9, 0, 6, 7, 4, 2, 88, 38, 58, 98, 68, 78, 48, 28, 18, 80, …

### Python 3 — 250 bytes

```python
w='f{dvhorakyg|ewipsblzdxjqtcm'
g=lambda n:n>99and g(n//(k:=10**(2+(t:=n>999))))+'hu'[t]+g(n%k)or n>19and g(n%10)+'v'[:n%10]+w[n//10+17]+'i'or w[n-1:n]
d=1
while d<1e6:[*map(print,sorted(range(d&-2,d*10),key=lambda n:g(n)+'s'*(n%100==1)or'n'))];d*=10
```

**How it works**

- Each block of d-digit numbers, d = 1, 10, …, 10⁵, is sorted by a key and
  printed. The key is not the German name itself but a much shorter string
  that sorts exactly like it: every word part gets a one-letter code, and
  the codes are chosen so that comparing codes gives the same result as
  comparing the letters of the names.
- **Number words.** Below 100 a German number is one of 27 words, or a
  unit + *und* + a tens word (*einundzwanzig*). In alphabetical order the
  words are acht, achtzehn, achtzig, drei, dreißig, dreizehn, ein(s), elf,
  fünf, fünfzehn, fünfzig, neun, neunzehn, neunzig, (null), sechs,
  sechzehn, sechzig, sieben, siebzehn, siebzig, (tausend), vier, vierzehn,
  vierzig, zehn, zwanzig, zwei, zwölf, and they get the codes a, b, c, d,
  …, `|` in that order, with gaps at *null* (`n`) and *tausend* (`u`).
  The string `w` lists the codes of 1..19, then of 20, 30, …, 90.
- **The other parts.** After a unit come *hundert*, *tausend* or *und*;
  a word followed by more letters sorts after the bare word, and among
  them h < t < u, so the codes are `h`, `u` and `v` (the code for *tausend*
  also has to sit between *siebzig* and *vier*, since after *hundert* it
  competes with the number words: *einhunderttausend* against
  *einhundertsieben…* and *einhundertvier…*).
- **Two special cases.** *dreißig* starts like *drei*: drei < dreihundert <
  dreißig < dreitausend < dreiund… < dreizehn. So 30 is coded `d` (drei)
  plus `i`, a letter between `h` and `u`; every tens code gets the `i`
  (for the other tens it changes nothing, as their codes are unique), which
  is cheaper than testing for 30. And a final 1 is *eins* while 1 before
  *hundert*, *tausend*, *und* is *ein*: einhundert < eins < eintausend, so
  the key of a number ending in 01 gets `s` (`'s'*(n%100==1)`), which puts
  1001 after 1100 as in the real order.
- `g(n)` builds the code like a name: q·100 or q·1000 + r is
  g(q) + `h`/`u` + g(r); 20..99 is unit, `v`, tens code, `i`; below 20 a
  single code, `w[n-1:n]`, which is empty for n = 0.

**Which names, and where the sequence ends**

- Spellings follow the OEIS data and the jOEIS German speller (Sean A.
  Irvine corrected the entry in 2012): ß sorts as ss, as the entry says;
  100 is *einhundert* and 1000 *eintausend*; 101 is *einhunderteins*
  (no *und*). Written *hundert*, 100 would sort under h instead. The
  umlauts never decide a comparison (*fünf* and *zwölf* only meet words
  that differ earlier), so their treatment does not matter.
- Every number below a million is a single word. A million is *eine
  Million*, with the article, plural *Millionen*, and agreement for
  101·10⁶ (*hunderteine Million* or *einhunderteins Millionen*) is not
  settled, so this page takes the sequence to end with the 6-digit
  numbers, 10⁶ terms in all (every number from 0 to 999999), and the
  program stops there.
- The b-file here has 10000 terms (all numbers up to 4 digits), made by a
  separate speller that writes the real names; its first 59 terms are the
  entry's data. The whole program output, all 10⁶ terms, was checked
  against that speller, so the codes are exact for every term.

**Notes**

- The 6-digit block sorts 900000 keys: the whole sequence prints in about
  15 s using about 110 MB. The bar is the whole b-file (10000 terms, a
  fraction of a second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 250 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001061), CC BY-SA 4.0.
