# Functional 2

A functional language.

## Usage

`python functional2.py file`

## Examples

* Factorizing a number

```
NUM={in."Enter a number to calculate the factors of. >> "}
isprintfactor = {x->y->{x%y?0:{out.y&out."\n"}}}
val={isprintfactor.NUM}

printloop={n->{n}?{val.n & printloop.{n-1}}:1}
printloop.NUM
```

## Docs

See `docs/`