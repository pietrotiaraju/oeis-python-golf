# A002062

> a(n) = Fibonacci(n) + n.
> — [OEIS A002062](https://oeis.org/A002062)

Offset 0: 0, 2, 3, 5, 7, 10, 14, 20, 29, 43, 65, 100, 156, 246, 391, 625, 1003, …

### Python 3 — 42 bytes

```python
a=n=0;b=1
while[print(a+n)]:a,b=b,a+b;n+=1
```

**How it works**

- `a, b` walk through consecutive Fibonacci numbers F(n), F(n+1), starting
  from F(0) = 0, F(1) = 1, and n counts the steps, so every line is
  F(n) + n.

**Notes**

- The Fibonacci loop of [A000045](../../A000xxx/A000045/)
  (`a=b=1` / `print(a:=b-a)` / `b+=a`) needs the `+n` in parentheses,
  `print((a:=b-a)+n)`, and comes to 45 bytes.
- F(n) + n satisfies x(n) = x(n−1) + x(n−2) + 3 − n, which still needs n.
- Exact integer arithmetic, right for every n. The b-file has 501 terms
  (n = 0 to 500); the bar is the whole b-file in 60 s, a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002062), CC BY-SA 4.0.
