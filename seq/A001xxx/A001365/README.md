# A001365

> Expansion of 1/(1-x)^2/(1-x^2)/(1-x^6)/(1-x^12)/(1-x^24)/(1-x^48)/(1-x^60).
> — [OEIS A001365](https://oeis.org/A001365)

Offset 0: 1, 2, 4, 6, 9, 12, 17, 22, 29, 36, 45, 54, 67, 80, 97, 114, 135, 156, 183, 210, 243, …

### Python 3 — 66 bytes

```python
a=[0]*999
while v:=1:a+=(v:=v+a[-7*c]for c in b'0<');print(v)
```

The bytes literal holds five raw control bytes (0x01, 0x02, 0x06, 0x0C and 0x18) that a browser
does not show. Byte for byte, the second line is

```text
while v:=1:a+=(v:=v+a[-7*c]for c in b'<01><02><06><0C><18>0<');print(v)
```

where `<01>` stands for the single byte 0x01, and so on.

**How it works**

- **Layers.** The generating function is
  1/((1 − x)²(1 − x²)(1 − x⁶)(1 − x¹²)(1 − x²⁴)(1 − x⁴⁸)(1 − x⁶⁰)): change
  for n with two kinds of 1-coin and coins 2, 6, 12, 24, 48, 60. One kind of
  1-coin alone pays n in one way: A₀(n) = 1. Add the other seven coins
  c₁, …, c₇ = 1, 2, 6, 12, 24, 48, 60 one factor at a time:
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ) (multiplying by 1/(1 − x^cⱼ)), with
  Aⱼ(m) = 0 for m < 0, and a(n) = A₇(n).
- **One flat list, read while it grows.** `a` starts with 999 zeros and each
  pass appends row n: A₁(n), …, A₇(n). `a+=` with a generator extends `a`
  one item at a time (CPython's `list.extend` appends each item as soon as
  the generator yields it), and the generator reads `a` in between. When
  Aⱼ(n) is computed, `a` holds 999 + 7n + (j − 1) entries and Aⱼ(n − cⱼ) is
  exactly 7cⱼ from the end: `a[-7*c]`. For n < cⱼ that entry is one of the
  leading zeros (7cⱼ ≤ 420 < 999).
- **The coins.** Iterating over a bytes object gives ints, so the literal
  holds the coins themselves: 0x01, 0x02, 0x06, 0x0C, 0x18, `0` and `<` are
  1, 2, 6, 12, 24, 48 and 60.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true). `v:=v+a[-7*c]` turns v into A₁(n), …, A₇(n) in
  turn and yields each, which stores it as its slot; a walrus inside a
  generator binds the outer `v`, so after the row v = a(n), which is
  printed. Same program as [A001364](../A001364/) with other coins.

**Notes**

- a(n) = [A001364](../A001364/)(2n): in change for 2n farthings the
  farthings come in pairs (every other coin is even), and a pair acts as a
  second kind of halfpenny; halving every value gives the coins above.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁷, far from the 4300-digit int-to-str limit.
- The b-file has 1000 terms (n = 0 to 999); the bar is all of them in 60 s,
  which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001365), CC BY-SA 4.0.
