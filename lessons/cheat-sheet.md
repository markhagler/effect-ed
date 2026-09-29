# Promise vs. Effect, on One Page

| Question | Promise (the receipt) | Effect (the recipe card) |
|---|---|---|
| What is it? | A value that isn't ready yet | A plan for getting a value |
| When does it start? | The moment you make it | Only when you run it |
| Can you run it twice? | No, one receipt = one smoothie | Yes, as many times as you like |
| Does the type say what can go wrong? | No, `Promise<Smoothie>` | Yes, `Effect<Smoothie, OutOfMango>` |
| Does the type say what it needs? | No | Yes, `Effect<Smoothie, OutOfMango, Blender>` |
| Can you cancel it? | No | Yes, interrupt the fiber, cleanup still runs |
| Write steps top to bottom | `async` / `await` | `Effect.gen` / `yield*` |
| "Do this when it succeeds" | `.then(f)` | `Effect.map` / `Effect.andThen` |
| "Do this if it fails" | `.catch(f)` (catches everything, mystery box) | `Effect.catchTag("Name", f)` (one specific error) or `Effect.catch` (all listed errors) |
| Try again on failure | Write a loop yourself | `Effect.retry(card, { times: 3 })` |
| Give up after a while | Hard, needs a second Promise and a timer | `Effect.timeout(card, "2 seconds")` |
| Several at once | `Promise.all([...])` | `Effect.all([...], { concurrency: n })` |
| First one wins | `Promise.race([...])` (loser keeps running) | `Effect.race(a, b)` (loser is interrupted) |
| Always clean up | `try { } finally { }` (no interrupt case) | `Effect.acquireRelease` (success, error, and interrupt) |
| Ask for a helper | Import it or pass it in by hand | `yield* Blender`, then `Effect.provide(layer)` |
| Turn it into the other | (a Promise is already "running") | `Effect.runPromise(card)` at the door of the program |

## Reading an Effect type out loud

```
Effect<Smoothie, OutOfMango, Blender>
```

"An Effect that **gives you** a Smoothie, **might fail with** OutOfMango, and **needs** a Blender."

- `never` in slot 2: nothing can go wrong.
- `never` in slot 3: needs nothing. Ready to run.
- Trailing `never`s can be left off: `Effect<number>` means `Effect<number, never, never>`.

## The five lines of Effect 4 you actually need this month

```ts
import { Effect, Console, Context, Layer, Data, Fiber } from "effect"

Effect.gen(function* () { const x = yield* step; return x })   // a recipe with steps
class OutOfMango extends Data.TaggedError("OutOfMango") {}     // a named error
class Blender extends Context.Service<Blender, { ... }>()("Blender") {}   // a needed thing
Layer.succeed(Blender, { ... })                                 // a way to provide it
Effect.runPromise(card.pipe(Effect.provide(layer)))            // the door out of the kitchen
```
