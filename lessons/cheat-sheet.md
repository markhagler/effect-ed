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
| Go again on a timetable | `setInterval`, or a loop with `setTimeout` | `Effect.repeat(card, Schedule.spaced("10 minutes"))` |
| Retry, waiting longer each time | A loop, a counter, and `setTimeout`, by hand | `Effect.retry(card, Schedule.max([Schedule.exponential("1 second"), Schedule.recurs(3)]))` |
| Share a number between running tasks | A global `let` (read, `await`, write back loses updates) | `Ref.make(0)`, then `Ref.update(board, (n) => n + 1)` (one step) |
| Hand work from one task to another | A shared array and polling | `Queue.bounded(3)`, `Queue.offer`, `Queue.take` (a full shelf makes the putter wait) |
| Many values over time | Event listeners push whether you're ready or not | `Stream` with `map`, `filter`, `take`; runs only when pulled |
| Check data from outside | `JSON.parse` and hope | `Schema.decodeUnknownEffect(Crate)(data)` gives `Effect<Crate, SchemaError>` |
| Write down what happened | `console.log` (no time, level, or fiber) | `Effect.log`, `Effect.annotateLogs({ order: 42 })`, `Effect.withLogSpan("blend")` |
| Test "wait 10 minutes" quickly | Fake timers that patch `setTimeout` everywhere | `it.effect` + `TestClock.adjust("10 minutes")` |

## Reading an Effect type out loud

```
Effect<Smoothie, OutOfMango, Blender>
```

"An Effect that **gives you** a Smoothie, **might fail with** OutOfMango, and **needs** a Blender."

- `never` in slot 2: nothing can go wrong.
- `never` in slot 3: needs nothing. Ready to run.
- Trailing `never`s can be left off: `Effect<number>` means `Effect<number, never, never>`.

## The five lines of Unit 1 you actually need

```ts
import { Effect, Console, Context, Layer, Data, Fiber } from "effect"

Effect.gen(function* () { const x = yield* step; return x })   // a recipe with steps
class OutOfMango extends Data.TaggedError("OutOfMango") {}     // a named error
class Blender extends Context.Service<Blender, { ... }>()("Blender") {}   // a needed thing
Layer.succeed(Blender, { ... })                                 // a way to provide it
Effect.runPromise(card.pipe(Effect.provide(layer)))            // the door out of the kitchen
```

## The Unit 2 lines you'll reach for

```ts
import { Effect, Schedule, Ref, Queue, Stream, Schema } from "effect"
import { TestClock } from "effect/testing"

Effect.retry(card, Schedule.exponential("1 second"))               // try again, waiting longer each time
Ref.make(0)                                                        // a card that makes a shared whiteboard
Queue.bounded<string>(3)                                           // a card that makes a 3-slot order shelf
Stream.make("🥭", "🍓", "🥝").pipe(Stream.map(wash), Stream.take(2))  // a conveyor belt with stations
Schema.decodeUnknownEffect(Crate)(delivery)                        // check the delivery at the back door
Effect.log("blending").pipe(Effect.annotateLogs({ order: 42 }))    // a diary line with a sticky note
TestClock.adjust("10 minutes")                                     // turn the magic clock's knob
```
