# A000870

> Numbers beginning with letter 's' in English.
> — [OEIS A000870](https://oeis.org/A000870)

Offset 1: 6, 7, 16, 17, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, …

### Python 3 — 61 bytes

```python
n=0
while 1:n+=1;c=f'{n:_}_';c[c[:3:2]=='1_']in'67'!=print(n)
```

**Which names**

- US names as in the OEIS data: 100 is "one hundred" (not "a hundred"),
  1100 is "one thousand one hundred" (not "eleven hundred"), and there is
  no "and".
- Split n into groups of three digits from the right; the leading group k
  has 1 to 3 digits. Every name of n ≥ 1000 starts with the name of k, then
  the scale word. So the first word is that of k: the hundreds digit when k
  has three digits ("six hundred …"), ten … nineteen when k is 10–19, a
  tens word twenty … ninety when k ≥ 20 has two digits, a digit name
  otherwise.
- The scale words never come first, so this holds whatever the large
  scales are called: short scale, long scale ("one thousand million") or
  the systematic names past vigintillion. The rule, and so the program, is
  right for every n.
- The tens words start like the digits (twenty/two, thirty/three, …,
  eighty/eight, ninety/nine), and so do thirteen … nineteen. So one digit
  decides: the second digit of a leading group 10–19, the leading digit
  otherwise. The words starting with s are six, seven, sixteen,
  seventeen, sixty, seventy and the hundreds of six and seven: the deciding
  digit is 6 or 7.

**How it works**

- `f'{n:_}_'` writes n with `_` between the groups and one more `_` at the
  end: 12345 → `12_345_`.
- `c[:3:2]` is characters 0 and 2. It is `1_` exactly when the leading
  group is 10–19: the group has two digits, so the `_` is at index 2, and
  starts with 1.
- That test, as 0 or 1, indexes `c`: `c[1]` for a 10–19 group, `c[0]`
  otherwise, the deciding digit. `in'67'` tests it.
- `X in'67'!=print(n)` is a chained comparison: Python evaluates
  `print(n)` only when the `in` test is true, and then `'67'!=None` is true
  too. That is `and print(n)` in 2 bytes less.

**Notes**

- The same program with `'45'` is [A000867](../A000867/) ("f"); the
  e-words need one more test ([A000873](../A000873/)).
- A regular expression, `re.match('[67]|1[67],',f'{n:,},')and print(n)`
  with `import re`, is 72 bytes; the index `c[:3]in'16_17_'` in place of
  `c[:3:2]=='1_'` (its stray matches, `6_`, `7_` and `6_1`, start with 6 or 7
  anyway) needs `in'67_'` and is 64.
- The program tests every n: about 3.6 million terms in 60 s here (up to
  17.3 million).
- The b-file has 10000 terms (up to a(10000) = 65775); the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000870), CC BY-SA 4.0.
