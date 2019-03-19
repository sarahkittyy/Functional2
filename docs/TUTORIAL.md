# Tutorial

## Output

`name.param` indicates a function call.
`out` is a built-in function, which prints its parameter.

```
out."Hello World!"; ~$ This is a comment
```

## Variables

Variables are dynamically typed.

```
x = 2;
y = 3;
out.x;       ~$ outputs 2
out."\n";    ~$ newline
out.y;       ~$ outputs 3
```

## Input

```
~$ Expressions wrapped in {} return their value.
x = {in."input >> "};
out.x;
```

## Arithmetic

Returning values / doing arithmetic should all be wrapped in \{...\}.

```
x = 5;
y = 3;
z = {x + 3}; ~$ +, -, *, /, %

~$ '&' Executes both statements, returns the first's value.

out.z; ~$ outputs 8
```

## Conditionals

Functional 2 uses C-Like ternary operators.

"True" is indicated by a non-zero value.

Format: {value ? if-not-zero : if-zero}

```
x = 5;
y = {x?0:1};
out.y; ~$ outputs 0

out."\n";

x = 0;
y = {x?0:1};
out.y; ~$ outputs 1 
```

## Lambdas

Lambda expressions are defined as `param -> expr`
`expr` does not need to be brace-wrapped.

Ex:

```
addOne = { x -> x + 1 };
out.{addOne.5}; ~$ Outputs 6.
```

## Objects

```
object = [
    1,2,3,4,5
];
out.{{get.object}.2}
```

## Examples

See `examples/`