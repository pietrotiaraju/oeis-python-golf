# A001300

> Number of ways of making change for n cents using coins of 1, 5, 10, 25, 50 cents.
> — [OEIS A001300](https://oeis.org/A001300)

Offset 0: 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 9, …

### Python 3 — 64 bytes

```python
a=[0]*999
while v:=1:a+=[v:=v+a[-i]for i in b'(b\305'];print(v)
```

The bytes literal holds one raw control byte (0x13) that a browser does not
show, and one octal escape. Byte for byte, the second line is

```text
while v:=1:a+=[v:=v+a[-i]for i in b'(<13>bÅ'];print(v)
```

where `<13>` stands for the single byte 0x13. Escaping it too, ``, makes
the program 66 bytes.

**How it works**

- **Layers.** Pennies alone pay any n ≥ 0 in exactly one way: A₀(n) = 1. Add
  the other coins one at a time, in the order c₁, …, c₄ = 10, 5, 25, 50, and
  let Aⱼ(n) count the ways with pennies and c₁, …, cⱼ. A way either uses no
  cⱼ coin or uses one and leaves a way for n − cⱼ, so
  Aⱼ(n) = Aⱼ₋₁(n) + Aⱼ(n − cⱼ), with Aⱼ(m) = 0 for m < 0, and
  a(n) = A₄(n). The order of the coins does not change the count.
- **One flat list.** `a` starts with 999 zeros and each pass appends row n:
  A₁(n), …, A₄(n). While row n is built the list still has 999 + 4n
  entries, because `a+=[…]` evaluates the whole comprehension before it
  extends `a`. Slot k (k = 0…3) of row n − c is then 4c − k places before
  the end, at `a[-(4c-k)]`; for n < c the index falls into the zeros, which
  supply Aⱼ(m) = 0 for m < 0. The largest offset is 197, so 99 zeros would
  not be enough.
- **The offsets.** For (k, cⱼ) = (0, 10), (1, 5), (2, 25), (3, 50), 4cⱼ − k
  is 40, 19, 98, 197: `(`, the byte 0x13, `b`, and `Å` (a bytes literal
  takes only ASCII, so 197 needs the octal escape whichever slot the
  half-dollar gets). This order keeps 39, the quote, out of the literal.
  Iterating over a bytes object gives ints, so `i` is the offset itself.
- **The running sum.** `while v:=1:` sets v = A₀(n) = 1 at the start of
  every pass (and is always true). `v:=v+a[-i]` turns v into A₁(n), …,
  A₄(n) in turn and stores each as its slot; the walrus in the
  comprehension binds the outer `v`, so after the row v = a(n), which is
  printed. The same template gives [A001301](../A001301/) and
  [A000008](../../A000xxx/A000008/).

**Notes**

- The previous record (74 bytes) counted in nickels: with t = ⌊n/5⌋,
  quarters and halves making 5r nickels in ⌊r/2⌋ + 1 ways and nickels and
  dimes paying the rest in ⌊(t − 5r + 2)²/4⌋ ways, it is

  ```python
  m=60
  while[print(sum((m-5*j)//50*(j*j//4)for j in range(m//5,0,-5)))]:m+=1
  ```

- Writing the weight as `(m//5-j)//10` is 75 bytes; a double sum over
  halves and quarters, `sum(j*j//4for k in range(m//5,0,-10)for j in
  range(k,0,-5))`, is 83; summing the cubic of [A001299](../A001299/) over
  the halves is 78, and the weighted sum with five prints per pass is 80.
  Unlike A001299, no formula ⌊P(t)⌋ with a single polynomial P exists:
  the generating function in t has a double pole at −1, which adds an
  unbounded (−1)^t·t/160 term.
- Exact integer arithmetic, so the program is right for every n; a(n) grows
  like n⁴/1500000, far from the 4300-digit int-to-str limit.
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 74 | first entry |
| 2026-11-09 | Python 3 | 64 | layered running sums in one flat list, offsets in a bytes literal (-10) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001300), CC BY-SA 4.0.
