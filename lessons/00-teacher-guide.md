# Teacher's Guide

## Who this is for

Seventh and eighth graders who have written some code (Scratch, Python, or a little JavaScript)
and are curious. They do **not** need to know TypeScript. They do need to be okay with the idea
that code runs one line at a time.

## Pacing for a month (eight to twelve class periods)

| Week | Lessons | What students should be able to say by Friday |
|------|---------|-----------------------------------------------|
| 1 | 1, 2 | "JavaScript has one cook. A Promise is a receipt for something that isn't ready yet." |
| 2 | 3, 4 | "An Effect is a recipe card. It lists what you get, what can go wrong, and what it needs." |
| 3 | 5, 6 | "A recipe asks for a blender; the kitchen provides one. A fiber is a bookmark in a recipe." |
| 4 | 7, review, project | "Whatever you borrow, you give back." Then they build the smoothie shop. |

## The one rule for teaching this

**Never introduce two new words in one breath.** The kitchen story exists so that every new
technical term lands on top of a picture students already have. Say the picture first, the
word second: "the receipt the counter hands you, which programmers call a Promise."

## Running the demos

You need Node 20 or newer and a folder with Effect installed:

```bash
mkdir smoothie-shop && cd smoothie-shop
npm init -y
npm install effect@rc typescript tsx
```

Run any snippet with `npx tsx file.ts`. Students do not need to see `tsconfig.json`;
if you want one, `npx tsc --init` is enough.

## Misconceptions to expect

- **"Async means faster."** No. Async means the cook doesn't stand still while waiting.
  The smoothie still takes the same time; the cook just makes toast meanwhile.
- **"A Promise runs when I call .then()."** No. It starts the moment it's created.
  That's the key difference from an Effect, so hammer it in Lesson 2 before Lesson 3.
- **"An Effect does the thing."** No. An Effect *describes* the thing. Running it does the thing.
  Repeat the phrase "plan, not action" until they groan.
- **"Error means crash."** Effect splits "expected problems we wrote on the card"
  from "the kitchen caught fire." Lesson 4 is entirely about that split.
- **"never means it will never finish."** In Effect types, `never` in the error slot means
  "nothing can go wrong here," and in the requirements slot means "needs nothing." Say "nothing" out loud.

## When a sharp kid asks the hard question

- *"Isn't this just Promises with extra steps?"* Great question. Promises can't tell you what
  can go wrong, can't be re-run, can't be cancelled, and can't say what they need. Effect adds
  exactly those four things. Show the [cheat sheet](cheat-sheet.md).
- *"Why not just use try/catch?"* Because `try/catch` catches *everything* with one net,
  including bugs you didn't mean to hide, and the compiler can't check that you did it.
- *"Does Effect use more than one cook?"* No. Still one cook (one thread). Fibers are bookmarks,
  not extra cooks. Lesson 6 covers this.
- *"What's `yield*`?"* Read it as "do this step and hand me the result." That's all they need this month.

## Assessment idea: the smoothie shop project

Students describe (on paper first, then in code) a smoothie shop that:

1. Looks up a recipe (can fail: "no such smoothie"),
2. Checks the fridge (can fail: "out of bananas"),
3. Blends (needs a Blender service),
4. Retries the fridge check twice if it fails,
5. Gives up after five seconds no matter what,
6. Always turns the blender off at the end.

Grade on whether their recipe card's three lines are right, not on syntax.
