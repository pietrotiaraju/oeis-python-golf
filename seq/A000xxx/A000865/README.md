# A000865

> Numbers beginning with letter 'o' in English.
> — [OEIS A000865](https://oeis.org/A000865)

Offset 1: 1, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, …

### Python 3 — 46 bytes

```python
n=0
while 1:n+=1;f'{n:_}_'[::2]<'1_'!=print(n)
```

**Which names**

- US names as in the OEIS data: 100 is "one hundred" (not "a hundred"),
  1100 is "one thousand one hundred" (not "eleven hundred"; the b-file has
  1100), and there is no "and".
- Split n into groups of three digits from the right; the leading group k
  has 1 to 3 digits. Every name of n ≥ 1000 starts with the name of k, then
  the scale word. So the first word is that of k: the hundreds digit when k
  has three digits ("one hundred …"), ten … nineteen when k is 10–19, a tens
  word twenty … ninety when k ≥ 20 has two digits, a digit name otherwise.
- The scale words never come first, so this holds whatever the large
  scales are called: short scale, long scale ("one thousand million") or
  the systematic names past vigintillion. The rule, and so the program, is
  right for every n.
- "o" starts only "one": the terms are the n whose leading group is 1 or
  100–199, that is, leading digit 1 and a leading group that is not 10–19.

**How it works**

- `f'{n:_}_'` writes n with `_` between the groups and one more `_` at the
  end: 12345 → `12_345_`. Its characters 0, 2, 4, … (`[::2]`) are the
  leading digit, then the character at index 2, which is `_` exactly when
  the leading group has two digits (a digit for one or three, missing for
  n < 10), then more.
- `_` sorts after the digits, so `…<'1_'` holds exactly when the leading
  digit is 1 and the leading group is not 10–19: `1` alone (n = 1) and `1`
  followed by a digit (100, 1_000, …) are below `1_`, while `1_…` (10–19,
  10_000, …) and anything starting with 2–9 are not.
- `X<'1_'!=print(n)` is a chained comparison: Python evaluates `print(n)`
  only when `X<'1_'` is true, and then `'1_'!=None` is true too. That is
  `and print(n)` in 2 bytes less.

**Notes**

- With `s=str(n)` the test is `len(s)%3<2>int(s[0])`, 56 bytes with the
  same chained print; a regular expression on the grouped string,
  `re.match('1(?!.,)',f'{n:,},')and print(n)`, is 68.
- The terms come in long blocks (1, 100–199, 1000–1999, 100000–199999, …,
  then nothing from 2·10⁶ to 10⁸), and the program tests every n: about
  1.1 million terms in 60 s here, every term up to 1999999.
- The b-file has 10000 terms (up to a(10000) = 108898); the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000865), CC BY-SA 4.0.
