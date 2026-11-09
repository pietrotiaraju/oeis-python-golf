# A001310

> Number of ways of making change for n cents using coins of 1, 2, 4, 10, 20, 40, 100 cents.
> — [OEIS A001310](https://oeis.org/A001310)

Offset 0: 1, 1, 2, 2, 4, 4, 6, 6, 9, 9, 13, 13, 18, 18, 24, 24, 31, 31, 39, 39, 50, …

### Python 3 — 66 bytes

```python
a=[0]*600
while v:=1:a+=(v:=v+a[-6*c]for c in b'\n(d');print(v)
```

The coin table holds three raw control bytes (0x02, 0x04 and 0x14) that a
browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=(v:=v+a[-6*c]for c in b'<02><04>\n<14>(d');print(v)
```

where `<02>` stands for the single byte 0x02, and so on. The table lists the
coins other than the penny: 2, 4, 10 (`\n`), 20, 40 (`(`) and 100 (`d`).
With the raw bytes escaped, `b'\2\4\n\24(d'`, the program is 70 bytes.

**How it works**

- **Stages.** Number the coin kinds c₁ = 1 (the penny), then c₂, …, c₇ in
  the order of the table, and let Aⱼ(m) be the number of ways to pay m cents
  with the first j kinds, with Aⱼ(m) = 0 for m < 0. A way either has no coin
  of kind j, or has one, and the rest is a way to pay m − cⱼ, so
  Aⱼ(m) = Aⱼ₋₁(m) + Aⱼ(m − cⱼ), and a(n) = A₇(n). Pennies alone pay any
  m ≥ 0 in exactly one way: A₁(m) = 1. (In series terms each stage divides
  by 1 − x^cⱼ, so the order of the kinds does not matter.)
- **One pass per n.** `while v:=1:` sets v = A₁(n) = 1, a non-zero value, so
  the loop never ends. The generator then runs through the table: for
  c = cⱼ, `v:=v+a[-6*c]` adds Aⱼ(n − cⱼ) to v, which turns Aⱼ₋₁(n) into
  Aⱼ(n). A walrus inside a generator binds the outer `v`, so after the last
  coin v = A₇(n) = a(n), which is printed.
- **Reading the list while it grows.** `a+=` with a generator extends `a`
  one item at a time (CPython's `list.extend` appends each item as soon as
  the generator yields it), and the generator reads `a` in between, so each
  Aⱼ(n) is stored before the next stage is computed. When Aⱼ(n) is computed
  `a` holds 600 + 6n + (j − 2) entries, and Aⱼ(n − c) is entry
  600 + 6(n − c) + (j − 2), exactly 6c from the end: `a[-6*c]`. If
  n − c < 0, that entry is one of the 600 leading zeros, as it should be:
  its index lies between 0 (as 600 = 6·100) and 599.
- **Bytes table.** Iterating over `bytes` gives ints, so no `ord` is needed,
  and Python accepts raw control bytes inside a bytes literal (only NUL, the
  line breaks, the backslash and the quote are not allowed there).
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- With a list comprehension, `a+=[…]`, the whole row is built before `a`
  grows, so the offsets become 6c minus the slot, as in
  [A001301](../A001301/) and [A001306](../A001306/); the offsets for 40 and
  100 then pass 127 and need `ord` on a `str`, and the best order gives 68
  bytes. The stages as a `for` statement, `for c in b'…':v+=a[-6*c];a+=v,`,
  with `print(v)` on the next line, are 69 bytes; the coins as a tuple
  instead of bytes make 73. Recomputing the whole table up to n on every
  pass is 103 bytes, and reading a(n) as a digit of one big-integer
  quotient, `X**(n+177)//math.prod(X**c-1for c in …)%X` with X = 2^(n+99),
  is 98 bytes and takes about 50 s for the b-file here.
- a(n) is a quasi-polynomial of degree 6 whose period divides 200, the lcm
  of the coins; no single polynomial with a floor, as in
  [A001299](../A001299/), was found, and the nested sums of
  [A001300](../A001300/) need one level per extra coin (two levels over the
  sum of [A000008](../../A000xxx/A000008/) already make 116 bytes for
  [A001312](../A001312/)).
- a(n) ≤ (n + 1)⁶, since the numbers of the six larger coins fix the
  pennies, so the terms stay far below the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001310), CC BY-SA 4.0.
