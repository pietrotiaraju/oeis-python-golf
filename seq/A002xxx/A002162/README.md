# A002162

> Decimal expansion of the natural logarithm of 2.
> — [OEIS A002162](https://oeis.org/A002162)

Offset 0: 6, 9, 3, 1, 4, 7, 1, 8, 0, 5, 5, 9, 9, 4, 5, 3, 0, 9, 4, 1, 7, 2, 3, …

### Python 3 — 84 bytes

```python
z=q=10;t=l=2
while-z%t<q or[print(z//t),q:=q*10,z:=z%t*10]:q*=l//2;l+=2;z=z*l+q;t*=l
```

**How it works**

A Gibbons-style unbounded spigot, the halved form of the π spigot in
[A001672](../../A001xxx/A001672/), run on ln 2 = Σ_(k≥1) 1/(k·2ᵏ).

- **Series.** The term ratio is r_k = k/(2k+2) < ½ and the first term is
  ½, so ln 2 = ½·u₁ with u_k = 1 + r_k·u_(k+1):
  ln 2 = ½(1 + 1/4·(1 + 2/6·(1 + 3/8·(1 + …)))). Every tail u_k lies in
  [1, 2], since r_k < ½.
- **State.** The digits still to print are those of (q·u + z − q)/t,
  where u is the current tail, so the number lies in [z/t, (z+q)/t]. At
  the start that is 10·ln 2 = 10u₁/2: z = q = 10, t = 2, the interval
  [5, 10].
- **Taking a term.** With l = 2k + 2 (`l` runs 2, 4, 6, …, and `l//2` is k
  before `l+=2`), substituting u = 1 + (k/l)·u′ gives q → q·k,
  z → z·l + q·k, t → t·l: `q*=l//2` comes first, so `z=z*l+q` adds the
  new q. The width q/t is multiplied by r_k < ½.
- **Printing a digit.** Both ends have the integer part `z//t` unless
  z mod t + q > t, which `-z%t<q` tests (−z mod t = t − z mod t; when
  z mod t = 0 the test just waits one more term). Then the digit is
  certain; the list prints it and the interval becomes 10·(x − digit):
  `q*10` and `z%t*10`. Otherwise the body takes one more term. A term is
  worth log₁₀ 2 ≈ 0.3 digits, and each term gets one chance to print, so
  the loop keeps up.

**Notes**

- Exact integer arithmetic: a digit is printed only when both ends of an
  interval that contains ln 2 agree, and ln 2 is irrational, so no digit
  is held back forever. The program is right for every n.
- Each printed value is one digit, so the 4300-digit int-to-str limit
  does not apply. t gains about log₂(2k) bits per term; the whole
  b-file, 20001 digits (a(0) to a(20000)), takes about 66 000 terms and
  some 16 s here. The bar is the whole b-file in 60 s.
- ln 2 = 2·artanh(⅓) = Σ 2/((2k+1)·3²ᵏ⁺¹) gains 3.2 bits a term and is
  several times faster, but its update (`q*=l;l+=2;z=z*l*9+q;t*=l*9`
  with `z=q=20;t=3;l=1`) costs three bytes more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002162), CC BY-SA 4.0.
