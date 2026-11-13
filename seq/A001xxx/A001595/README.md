# A001595

> a(n) = a(n-1) + a(n-2) + 1, with a(0) = a(1) = 1.
> — [OEIS A001595](https://oeis.org/A001595)

Offset 0: 1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 1219, 1973, …

### Python 3 — 32 bytes

```python
a=b=1
while[print(a)]:a,b=b,a-~b
```

**How it works**

- (a, b) holds two consecutive terms; `a,b=b,a-~b` shifts the window and
  appends a + b + 1 (a−~b = a + b + 1), as in
  [A000071](../../A000xxx/A000071/). The start is a(0) = a(1) = 1.

**Notes**

- These are the Leonardo numbers, a(n) = 2F(n+1) − 1 with F the Fibonacci
  numbers.
- The walrus form `a,b=-1,0` / `while[print(a:=b-a)]:b-=~a` is 35 bytes;
  a search over two-variable programs (one or two in-place statements,
  tuple updates, walrus prints) found nothing below 32.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (a(0) to a(500)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001595), CC BY-SA 4.0.
