# A001306

> Number of ways of making change for n cents using coins of 1, 5, 10, 20, 50, 100 cents.
> — [OEIS A001306](https://oeis.org/A001306)

Offset 0: 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 10, …

### Python 3 — 65 bytes

```python
a=[0]*999
while v:=1:a+=(v:=v+a[-5*c]for c in b'\n2d');print(v)
```

The bytes literal holds two raw control bytes (0x05 and 0x14) that a browser
does not show. Byte for byte, the second line is

```text
while v:=1:a+=(v:=v+a[-5*c]for c in b'<05>
<14>2d');print(v)
```

where `<05>` stands for the single byte 0x05, and so on; `
` is the
two-character escape for 10, since a raw line break cannot sit in a literal.

**How it works**

- **Layers.** Pennies alone pay any n ≥ 0 in exactly one way: A₀(n) = 1. Add
  the other coins one at a time, c₁, …, c₅ = 5, 10, 20, 50, 100, and let
  Aⱼ(n) count the ways with pennies and c₁, …, cⱼ. A way either uses no cⱼ
  coin or uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and a(n) = A₅(n).
- **One flat list, read while it grows.** `a` starts with 999 zeros and each
  pass appends row n: A₁(n), …, A₅(n). `a+=` with a generator extends `a`
  one item at a time (CPython's `list.extend` appends each item as soon as
  the generator yields it), and the generator reads `a` in between. When
  Aⱼ(n) is computed, `a` holds 999 + 5n + (j − 1) entries and Aⱼ(n − cⱼ) is
  entry 999 + 5(n − cⱼ) + (j − 1), exactly 5cⱼ from the end: `a[-5*c]`.
  For n < cⱼ that entry is one of the leading zeros (5cⱼ ≤ 500 ≤ 999),
  which supply Aⱼ(m) = 0 for m < 0.
- **The coins.** Iterating over a bytes object gives ints, so the literal
  holds the coins themselves: 0x05, `
`, 0x14, `2` and `d` are 5, 10, 20,
  50 and 100. All are ASCII, so no `ord` is needed.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true). `v:=v+a[-5*c]` turns v into A₁(n), …, A₅(n)
  in turn and yields each, which stores it as its slot; a walrus inside a
  generator binds the outer `v`, so after the row v = A₅(n) = a(n), which is
  printed.

**Notes**

- The first record (67 bytes) built each row with a list comprehension,
  which reads `a` before any of the row is stored, so slot k of row n − c
  sat 5c − k from the end. Those offsets, 25, 49, 98, 247 and 496, did not
  all fit in a bytes literal, and reading them as code points of a `str`
  with `ord` cost 5 bytes:

  ```python
  a=[0]*999
  while v:=1:a+=[v:=v+a[-ord(i)]for i in'1b÷ǰ'];print(v)
  ```

  (there with U+0019 written as an escape; the record had it raw). The
  generator form is from [A001310](../A001310/).
- Pennies pay any remainder, so a(n) = A001307(⌊n/5⌋), where
  [A001307](../A001307/) counts the same coins in units of 5 cents (with an
  extra 1 for the slack). Its 61-byte program with the print repeated,
  `exec('print(v);'*5)`, is 72 bytes. Keeping the coins themselves in a bytes
  literal and appending one slot at a time, so that every offset is 5c, is 69
  as a comprehension, `[a:=a+[v:=v+a[-5*c]]for c in b'…']`, and 70 as a
  `for` loop.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁵/600000000, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 67 | first entry |
| 2026-11-09 | Python 3 | 65 | generator extends the list while it is read, coins in a bytes literal (-2) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001306), CC BY-SA 4.0.
