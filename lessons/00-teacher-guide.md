# Teacher's Guide

## Who this is for

Seventh and eighth graders who have written some code (Scratch, Python, or a little JavaScript)
and are curious. They do **not** need to know TypeScript. They do need to be okay with the idea
that code runs one line at a time.

## Pacing (two months, eight to twelve class periods each)

### Unit 1: The recipe card

| Week | Lessons | What students should be able to say by Friday |
|------|---------|-----------------------------------------------|
| 1 | 1, 2 | "JavaScript has one cook. A Promise is a receipt for something that isn't ready yet." |
| 2 | 3, 4 | "An Effect is a recipe card. It lists what you get, what can go wrong, and what it needs." |
| 3 | 5, 6 | "A recipe asks for a blender; the kitchen provides one. A fiber is a bookmark in a recipe." |
| 4 | 7, review, project | "Whatever you borrow, you give back." Then they build the smoothie shop. |

### Unit 2: The busy kitchen

Unit 2 assumes Unit 1. Every lesson leans on the recipe card's three lines, on services (Lesson 5),
and on bookmarks (Lesson 6).

| Week | Lessons | What students should be able to say by Friday |
|------|---------|-----------------------------------------------|
| 5 | 8, 9 | "A schedule says when to go again and when to stop. A Ref is a whiteboard where read, change, write back is one step." |
| 6 | 10, 11 | "A queue is a shelf between bookmarks; a full shelf makes the counter wait. A stream is a belt that hands you many things, only when you reach for the next one." |
| 7 | 12, 13 | "Stuff from outside is unknown until a schema checks it. Effect's diary lines know when, how serious, and which bookmark." |
| 8 | 14, review, project | "In the practice kitchen the blender is pretend and the clock only moves when I turn the knob." Then they open the smoothie shop for real. |

## The one rule for teaching this

**Never introduce two new words in one breath.** The kitchen story exists so that every new
technical term lands on top of a picture students already have. Say the picture first, the
word second: "the receipt the counter hands you, which programmers call a Promise."

## Running the demos

You need Node 20 or newer and a folder with Effect installed:

```bash
mkdir smoothie-shop && cd smoothie-shop
npm init -y
npm install effect typescript tsx
```

Run any snippet with `npx tsx file.ts`. Students do not need to see `tsconfig.json`;
if you want one, `npx tsc --init` is enough.

Lesson 14 adds a test runner: `npm install -D vitest @effect/vitest`, name files `*.test.ts`, and run
`npx vitest run`. No config file is needed.

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
- **"recurs(3) means 3 runs."** It means 3 *more* runs after the first, so up to 4 in total.
  And `spaced` or `exponential` alone never stop: add a limit (Lesson 8).
- **"One cook means shared numbers can't go wrong."** A plain `count++` is never torn, but
  *read, pause, write back* loses updates. Only a one-step `Ref.update` is safe (Lesson 9).
- **"Waiting at the shelf freezes the kitchen."** A waiting `take` or `offer` parks one bookmark;
  everyone else keeps cooking (Lesson 10).
- **"A stream is just an array."** An array is already made. A stream makes each value only when
  someone reaches for it, which is why an endless belt plus `take(5)` finishes (Lesson 11).
- **"TypeScript already checks my data."** Ty checks code before it runs. Data from the internet arrives
  while it runs. Only a run-time check, a schema, can look inside the crate (Lesson 12).
- **"The test clock makes code faster."** Nothing runs faster. The clock jumps instead of ticking, and only
  waits that ask Effect's clock (`Effect.sleep`, schedules) notice. Plain `setTimeout` doesn't (Lesson 14).

## When a sharp kid asks the hard question

- *"Isn't this just Promises with extra steps?"* Great question. Promises can't tell you what
  can go wrong, can't be re-run, can't be cancelled, and can't say what they need. Effect adds
  exactly those four things. Show the [cheat sheet](cheat-sheet.md).
- *"Why not just use try/catch?"* Because `try/catch` catches *everything* with one net,
  including bugs you didn't mean to hide, and the compiler can't check that you did it.
- *"Does Effect use more than one cook?"* No. Still one cook (one thread). Fibers are bookmarks,
  not extra cooks. Lesson 6 covers this.
- *"What's `yield*`?"* Read it as "do this step and hand me the result." That's all they need this month.
- *"Why not just write a loop for retries?"* You can, but then the "when to go again" rules are tangled
  into the recipe. A schedule is its own value: name it, reuse it on any card, combine it, and test it with a
  fast-forwarded clock (Lessons 8 and 14).
- *"What's the difference between a Ref and a Queue?"* The whiteboard holds one current value you can read
  again and again. The shelf holds a line of values, and taking one removes it.
- *"Why not just `console.log`?"* No time, no level, no bookmark, no sticky notes, no volume knob.
  `Console.log` is fine for "here is my answer"; `Effect.log` is for "here is what happened."

## Assessment idea for Unit 1: the smoothie shop project

Students describe (on paper first, then in code) a smoothie shop that:

1. Looks up a recipe (can fail: "no such smoothie"),
2. Checks the fridge (can fail: "out of bananas"),
3. Blends (needs a Blender service),
4. Retries the fridge check twice if it fails,
5. Gives up after five seconds no matter what,
6. Always turns the blender off at the end.

Grade on whether their recipe card's three lines are right, not on syntax.

## Assessment idea for Unit 2: open the shop for real

Students take their Unit 1 smoothie shop and run a busy afternoon:

1. The front counter puts orders on a 3-slot order shelf (a bounded queue); two blending bookmarks take them off.
2. Every finished smoothie bumps a "sold today" whiteboard with `Ref.update`.
3. Orders arrive as unknown JSON and are checked by a schema; a bad order gets a rejection slip, not a crash.
4. The fridge check retries with doubling waits, at most three more times.
5. Each order's diary lines carry a sticky note with the order number.
6. Three tests in the practice kitchen: the happy path with a pretend blender, a bad delivery, and the fridge
   retry with the test clock turned forward.

Grade on whether each piece is the right tool for its job (shelf vs. whiteboard vs. belt), not on syntax.
