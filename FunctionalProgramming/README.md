### What is Functional Programming

A style of programming where solutions are simple, isolated functions, without any side effects outside of the function scope.

```
Input -> Process -> Output
```

1. isolated functions = there is **no dependence on the state** of the program, which includes global variables that are subject to change.
2. pure functions = the same input always gives the same output.
3. functions with limited side effects = any changes, or mutations, to the state of the program outside the function are carefully controlled.

Changing or altering things is called **mutation**. The outcome is called **side effect**.

Comparing functional programming to imperative programming, being unable to change things means that we can debug much more easily knowing with certainty that states are not changing and there are minimal side effects.

**Key Terms**

- **Callbacks** = function (A) passed into another function (B) to decide the invocation of (A).
- **First Class** Functions = behaviour of certain programming languages that allows functions to be assigned to variables, passed into or returned from other functions.
- **High Order Functions** = functions that takes other functions as input and return functions as output.
- **lambda** = functions that gets passed into or returned from other functions.

**Tips to keep in mind**

When doing functional programming, I remind myself this:

- can I avoid mutating a variable or object to achieve my goal?
- have I declared all dependencies explicitly? (e.g. feeding dependencies into function as param, rather than accessing global variables from within the function)

### Currying vs Partial Application

**Currying** refers to converting function calls with N arguments into a **chain of N function calls**, each taking a **single** argument.

```
//ES6
//normal function
function sum(a, b, c) { return a+b+c }

//curried function
function sum(a) {
  return function(b) {
    return function(c) {
      return a+b+c;
    }
  }
}
```

This can be useful for:
- memoization (the outer function's parameter can be applied to variations of inner function parameters)
- fail fast by throwing errors immediately at each layer
- this can associate functions to data, slightly similar to closures, by having First Class functions.

**Partial Application** creates a new function by fixing a subset of parameter inputs to a function.

```
//ES6
function sum(a,b,c) {
  return a+b+c;
}

const partialSum = sum.bind(this, a, b);
const fullSum = partialSum(c);
```

Unlike currying, partial application can abstract away any number of arguments, and the new function need not be unary function.
