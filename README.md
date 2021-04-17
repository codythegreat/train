# [Train](https://github.com/codythegreat/train)

## About
Train is an esoteric programming language that is about trains. Train compiles into Python.

Train is extremely simple and good language. Defining a function is simple; just lay down some track `=|=`, add some cars `[exp1]-[exp2]-[exp3]` and finish off with a little more track `=|=`

Your app's main entry point will look like this: `=|=<[choo("Hello World")]=|=` (notice the `<`)
## Examples
**Hello World**

`=|=<[choo("Hello World")]=|=`

**Ask a question**

You can use `#` inside of a car to indicate that that car is inside of a previous block statement (in this case `switch`)

```
=|=[chug greet(greeting)]-[ticket = aboard("Do you have a ticket? ")]-[switch ticket == "yes"]
-[#choo(greeting)]-[else switch ticket = "no"]-[#choo("Sorry, looks like you don't have a ticket!")]=|=

=|=<[greet("Welcome aboard passenger!")]=|=
```

## Syntax

```
print     . . .  choo
input     . . .  aboard
if        . . .  switch 
elif      . . .  else switch
def       . . .  chug 
return    . . .  caboose 

COMING SOON!
class     . . .  car 
except    . . .  derail
__init__  . . .  __conduct__
__str__   . . .  __steam__
```

## Installation
First you'll need to clone the repo : use `git clone https://github.com/codythegreat/train`

Next you can add the compiler to your path (optional) or run it from the location you downloaded it.