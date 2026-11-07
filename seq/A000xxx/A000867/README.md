# A000867

> Numbers beginning with letter 'f' in English.
> — [OEIS A000867](https://oeis.org/A000867)

Offset 1: 4, 5, 14, 15, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, …

### Python 3 — 61 bytes

```python
n=0
while 1:n+=1;c=f'{n:_}_';c[c[:3:2]=='1_']in'45'!=print(n)
```

**Which names**

- US names as in the OEIS data: 100 is "one hundred" (not "a hundred"),
  1100 is "one thousand one hundred" (not "eleven hundred"), and there is
  no "and".
- Split n into groups of three digits from the right; the leading group k
  has 1 to 3 digits. Every name of n ≥ 1000 starts with the name of k, then
  the scale word. So the first word is that of k: the hundreds digit when k
  has three digits ("four hundred …"), ten … nineteen when k is 10–19, a
  tens word twenty … ninety when k ≥ 20 has two digits, a digit name
  otherwise.
- The scale words never come first, so this holds whatever the large
  scales are called: short scale, long scale ("one thousand million") or
  the systematic names past vigintillion. The rule, and so the program, is
  right for every n.
- The tens words start like the digits (twenty/two, thirty/three, …,
  eighty/eight, ninety/nine), and so do thirteen … nineteen. So one digit
  decides: the second digit of a leading group 10–19, the leading digit
  otherwise. The words starting with f are four, five, fourteen,
  fifteen, forty, fifty and the hundreds of four and five: the deciding
  digit is 4 or 5.

**How it works**

- `f'{n:_}_'` writes n with `_` between the groups and one more `_` at the
  end: 12345 → `12_345_`.
- `c[:3:2]` is characters 0 and 2. It is `1_` exactly when the leading
  group is 10–19: the group has two digits, so the `_` is at index 2, and
  starts with 1.
- That test, as 0 or 1, indexes `c`: `c[1]` for a 10–19 group, `c[0]`
  otherwise, the deciding digit. `in'45'` tests it.
- `X in'45'!=print(n)` is a chained comparison: Python evaluates
  `print(n)` only when the `in` test is true, and then `'45'!=None` is true
  too. That is `and print(n)` in 2 bytes less.

**Notes**

- The same program with `'67'` is [A000870](../A000870/) ("s"); the
  e-words need one more test ([A000873](../A000873/)).
- A regular expression, `re.match('[45]|1[45],',f'{n:,},')and print(n)`
  with `import re`, is 72 bytes; the index `c[:3]in'14_15_'` in place of
  `c[:3:2]=='1_'` (its stray matches, `4_`, `5_` and `4_1`, start with 4 or 5
  anyway) needs `in'45_'` and is 64.
- The program tests every n: about 3.9 million terms in 60 s here (up to
  15.7 million).
- The b-file has 10000 terms (up to a(10000) = 45775); the bar is the whole
  b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000867), CC BY-SA 4.0.
