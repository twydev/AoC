### OOP
- Class = is just a syntactic sugar for the prototype based inheritance model.
- Constructor = functions that defines objects. function name starts with uppercase by convention.
- Prototype = used as a template for all instance of an object to inherit properties.
- Own Properties = properties belonging to particular instance of object. also properties defined in constructor instead of prototype.

```
function Child() {/* this is the constructor. you can define Own properties */}
Child.prototype = Object.create(Parent.prototype); //inherit from parent
Child.prototype.constructor = Child; //ensure child prototype uses the correct constructor when createing new object instances
Child.prototype.method = function() {} //methods can be extended into the prototype.
```

Mixin is used to extend functionalities to objects without subclassing.

```
function addMixinFeature(obj) {
  obj.newFeature = function() {
    /* do stuff */
  }
}
```

Applying addMixinFeature() to the object does not modify the object prototype or the constructor.

### Closures

Great document explaining clearly the concept of closure: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

Closure is the combination of a function and the lexical environment within which the function was declared.

JavaScript functions has access to:
- Global Scope
- Outer Functions Scope
- Local Scope

```
/* GLOBAL */
function outer() {
  /* OUTER */
  return function() {
    /* LOCAL */
  }
}
```

In this example, the anonymous inner function is returned by the outer() function, providing you access to all the 3 scopes.
You can limit how users interact with variables in the 3 scopes through the inner function implementation. This allows you to:

- Associate data to functions
- Emulates Private attributes and methods of Java programming
- Create a module pattern

However, try not to use closures unnecessarily as it impacts processing speed and memory consumption.

### IIFE
Immediately Invoked Function Expressions

```
(function() {
  /* this is executed immediately */
  var text = "Hello World";
  console.log(text);
})()
```

From my understanding, this syntax means that the function is called as soon as it is defined. Use cases:

1. if ES5 is not supported, then `let` and `const` are not available for block-scope. IIFE allows you to create `var` which is limited in the scope, without polluting the global scope.
2. allows truly private state by creating a closure in an IIFE and returning a function that has access to the private states.
3. capturing `global` object in both browser and Node.js.

