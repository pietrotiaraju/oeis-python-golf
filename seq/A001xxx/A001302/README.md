# A001302

> Number of ways of making change for n cents using coins of 1, 2, 5, 10, 25, 50 cents.
> — [OEIS A001302](https://oeis.org/A001302)

Offset 0: 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 19, 22, 25, 28, 31, 34, 40, …

### Python 3 — 65 bytes

```python
a=[0]*999
while v:=1:a+=[v:=v+a[-i]for i in b'1z\xf6'];print(v)
```

The bytes literal holds two raw control bytes (0x19 and 0x08) that a browser
does not show. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'<19>1<08>z\xf6'];print(v)
```

where `<19>` stands for the single byte 0x19, and so on. With those two bytes
escaped, `b'\x191\10z\xf6'` (an octal `\31` would swallow the `1` after it),
the program is 70 bytes.

**How it works**

- **Layers.** Pennies alone pay any n ≥ 0 in exactly one way: A₀(n) = 1. Add
  the other coins one at a time, in the order c₁, …, c₅ = 5, 10, 2, 25, 50
  (the order of the factors of the generating function does not matter), and
  let Aⱼ(n) count the ways with pennies and c₁, …, cⱼ. A way either uses no
  cⱼ coin or uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and a(n) = A₅(n).
- **One flat list.** `a` starts with 999 zeros, and each pass appends row n:
  A₁(n), …, A₅(n). While row n is being built the list still has 999 + 5n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`. Slot k (k = 0…4) of row n − c then sits 5c − k places before
  the end, at `a[-(5c-k)]`; for n < c that index falls into the padding,
  which supplies Aⱼ(m) = 0 for m < 0 (the largest offset is 246).
- **The offsets.** For the slots (k, cⱼ) = (0, 5), (1, 10), (2, 2), (3, 25),
  (4, 50), 5cⱼ − k is 25, 49, 8, 122, 246: the bytes 0x19, `1`, 0x08, `z` and
  `\xf6`. Iterating over a bytes object gives ints, so `i` is the offset
  itself. The 2-cent coin goes third because in first place its offset would
  be 10, a line break that needs the 2-byte escape `\n`; 246 is above 127, so
  it costs 4 bytes in any order.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of every
  pass (and is always true). In the comprehension `v:=v+a[-i]` turns v into
  A₁(n), …, A₅(n) in turn, and each value is stored as its slot; a walrus
  inside a comprehension binds the outer `v`, so after the row v is
  A₅(n) = a(n), which is printed.

**Notes**

- This is the template of [A001301](../A001301/) with one more layer. A `str`
  literal read with `ord` would hold 246 as a 2-byte character, but `ord()`
  costs 5 against the `b` and the 4-byte `\xf6`: 66 bytes.
- Summing [A001301](../A001301/)'s closed form over the number of half
  dollars, `m=22` /
  `while[print(sum(((k-j)**2+250)//500*(j//2)for k in range(m,0,-50)for j in range(k,1,-5)))]:m+=1`,
  is 100 bytes.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁵/15000000, far from the 4300-digit int-to-str limit.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes about a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001302), CC BY-SA 4.0.
