# A001313

> Number of ways of making change for n cents using coins of 1, 2, 5, 10, 20, 50 cents.
> — [OEIS A001313](https://oeis.org/A001313)

Offset 0: 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 19, 22, 25, 28, 31, 34, 41, …

### Python 3 — 65 bytes

```python
a=[0]*250
while v:=1:a+=(v:=v+a[-5*c]for c in b'\n2');print(v)
```

The coin table holds three raw control bytes (0x02, 0x05 and 0x14) that a
browser does not show. Byte for byte, the second line is

```text
while v:=1:a+=(v:=v+a[-5*c]for c in b'<02><05>\n2<14>');print(v)
```

where `<02>` stands for the single byte 0x02, and so on. The table lists the
coins other than the penny: 2, 5, 10 (`\n`), 50 (`2`) and 20. With the raw
bytes escaped, `b'\2\5\n2\24'`, the program is 69 bytes.

**How it works**

- **Stages.** Number the coin kinds c₁ = 1 (the penny), then c₂, …, c₆ in
  the order of the table, and let Aⱼ(m) be the number of ways to pay m cents
  with the first j kinds, with Aⱼ(m) = 0 for m < 0. A way either has no coin
  of kind j, or has one, and the rest is a way to pay m − cⱼ, so
  Aⱼ(m) = Aⱼ₋₁(m) + Aⱼ(m − cⱼ), and a(n) = A₆(n). Pennies alone pay any
  m ≥ 0 in exactly one way: A₁(m) = 1. (In series terms each stage divides
  by 1 − x^cⱼ, so the order of the kinds does not matter.)
- **One pass per n.** `while v:=1:` sets v = A₁(n) = 1, a non-zero value, so
  the loop never ends. The generator then runs through the table: for
  c = cⱼ, `v:=v+a[-5*c]` adds Aⱼ(n − cⱼ) to v, which turns Aⱼ₋₁(n) into
  Aⱼ(n). A walrus inside a generator binds the outer `v`, so after the last
  coin v = A₆(n) = a(n), which is printed.
- **Reading the list while it grows.** `a+=` with a generator extends `a`
  one item at a time (CPython's `list.extend` appends each item as soon as
  the generator yields it), and the generator reads `a` in between, so each
  Aⱼ(n) is stored before the next stage is computed. When Aⱼ(n) is computed
  `a` holds 250 + 5n + (j − 2) entries, and Aⱼ(n − c) is entry
  250 + 5(n − c) + (j − 2), exactly 5c from the end: `a[-5*c]`. If
  n − c < 0, that entry is one of the 250 leading zeros, as it should be:
  its index lies between 0 (as 250 = 5·50) and 249.
- **Bytes table.** Iterating over `bytes` gives ints, so no `ord` is needed,
  and Python accepts raw control bytes inside a bytes literal (only NUL, the
  line breaks, the backslash and the quote are not allowed there).
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The comprehension form of [A001301](../A001301/), `a+=[…]` with the
  offsets 5c minus the slot, ties at 65 bytes: in the order 10, 5, 50, 2, 20
  the offsets 50, 24, 248, 7, 96 fit in a bytes literal, 248 as `\xf8`. The
  coins as a tuple instead of bytes make 69.
- The 20 sits last in the table so that its escape `\24` is not followed by
  a digit.
- a(n) is a quasi-polynomial of degree 5 with period dividing 100; no single
  polynomial with a floor, as in [A001299](../A001299/), was found, and
  nested closed sums like the earlier records of
  [A000008](../../A000xxx/A000008/) and [A001300](../A001300/) need one
  level per extra coin (two levels are already 116 bytes for
  [A001312](../A001312/)).
- a(n) ≤ (n + 1)⁵, since the numbers of the five larger coins fix the
  pennies, so the terms stay far below the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001313), CC BY-SA 4.0.
