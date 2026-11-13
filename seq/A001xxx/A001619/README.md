# A001619

> Number of letters in English name for n increases at these numbers.
> — [OEIS A001619](https://oeis.org/A001619)

Offset 1: 1, 3, 11, 13, 17, 21, 23, 73, 101, 103, 111, 113, 117, 121, 123, 173, 323, 373, …

### Python 3 — 258 bytes

```python
z=lambda k:b'033544355436688779886655576678778;;::999;<<A=<?=><'[k]-48
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+z(28+e//3)+3*(e<3<3+n%100)+f(n%10**e)or n>19and z(n//10+18)+(n%10>0)+f(n%10)or z(n)
m=n=0
while n:=n+1:
 if f(n)>m:m=f(n);print(n)
```

**Which names**

- The terms are the n whose name has more letters than the name of every
  smaller number. As the OEIS comment says, the names use "and" and the
  hyphen counts as a letter: 101 is "one hundred and one" (16 letters, more
  than the 13 of "seventy-three"), and "twenty-one" (10) is longer than
  "seventeen" (9). Spaces do not count.
- The "and" goes between the hundreds and the rest of every 3-digit group:
  103373 is "one hundred and three thousand three hundred and
  seventy-three". This reproduces all 42 terms of the b-file and gives 52
  terms below one million, the last 373373.
- British usage also writes 1001 as "one thousand and one". That "and"
  never changes a term: if n ≥ 1000 ends in a group b = 1…99, then
  n = 1000A + b has at most the letters of 1000A plus 16 ("and" and a
  two-digit name of at most 13), while the smaller m = 1000(A − 1) + 373
  has those of 1000(A − 1) plus 28. The name of 1000A has at most 11 more
  letters than that of 1000(A − 1): a new "one thousand", or the thousands
  group a − 1 becoming a (at most 6 more), while a carry, which turns
  groups of 999 into 000, only shortens it. So m has at least as many
  letters as n, and n is never a term. So the program leaves that "and"
  out.
- Above the thousands come the short-scale dictionary words million,
  billion, … vigintillion (10⁶³), with the spellings sexdecillion and
  novemdecillion, as in [A000052](../../A000xxx/A000052/). Dictionaries go
  on only at centillion (10³⁰³), so the names, and with them the sequence,
  end with the 66-digit numbers; there the program stops with an
  `IndexError`. Up to that point every term is exact.

**How it works**

- `z(k)` reads a length from the bytes string, each stored as the
  character 48 + length: k = 0…19 are zero (0), one, …, nineteen; k = 20…27
  are twenty … ninety; k = 28…49 are hundred, thousand, million, …,
  vigintillion.
- `f(n)` is the number of letters of n's name. Below 20 it is the table;
  below 100 it is the tens word plus, when the units digit is not 0, the
  hyphen and the units word. From 100 on, `e` is the exponent of the
  largest word that fits: the number of digits minus one rounded down to a
  multiple of 3, or 2 for the 3-digit numbers, so f(n) = f(n // 10ᵉ) +
  word + f(n % 10ᵉ), plus 3 for "and" when e = 2 and n % 100 > 0. f(0) = 0,
  so a zero remainder adds nothing.
- The loop keeps the record m and prints each n that beats it.

**Notes**

- The b-file has 42 terms, up to 103373, which is the bar; they print in
  about 1 s, and all 52 terms below one million in about 10 s. Since a
  table of the 42 terms is shorter than the program, the program goes
  through review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 258 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001619), CC BY-SA 4.0.
