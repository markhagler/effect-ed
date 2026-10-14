# Glossary, in Kid Language

Kitchen word first, programmer word second, one sentence each.

## Unit 1

| Kitchen picture | Programmer word | What it means |
|---|---|---|
| One cook | **single-threaded** | JavaScript does one instruction at a time. Always. |
| Standing and staring at the toaster | **blocking / synchronous** | Waiting in a way that freezes everything else. |
| Leaving a ticket and walking away | **asynchronous** | Waiting in a way that lets other work happen. |
| The ticket you leave | **callback** | A function to run later, when something finishes. |
| The ticket rail | **event loop** | The list the cook checks whenever hands are free. |
| A receipt for a smoothie | **Promise** | A value that isn't ready yet. Starts the moment it's made. |
| Still blending / here you go / sorry, out | **pending / fulfilled / rejected** | The three states of a Promise. |
| "Pause this story until it's ready" | **await** | Wait for a Promise inside an `async` function. |
| A recipe card | **Effect** | A plan for producing a value. Does nothing until run. |
| "You get" line | **Success type** (slot 1) | What the Effect produces if all goes well. |
| "Can go wrong" line | **Error type** (slot 2) | The named, expected failures. |
| "Needs" line | **Requirements type** (slot 3) | The services the Effect needs before it can run. |
| Nothing on that line | **never** | Nothing can go wrong, or nothing is needed. |
| Handing the card to the kitchen | **running** (`Effect.runPromise`) | Actually doing the plan. Done once, at the edge of the program. |
| "Do this step and hand me the result" | **`yield*`** inside `Effect.gen` | Run one sub-recipe and get its value. |
| Out of mango | **error** (expected) | A known failure, written on the card, must be handled. |
| Kitchen fire | **defect** (unexpected) | A bug. Not on the card. Crashes loudly on purpose. |
| A name tag on a problem | **tagged error** (`Data.TaggedError`) | An error class with a `_tag` string so you can tell it apart. |
| Crossing an error off the card | **`Effect.catchTag`** | Handle one specific error; its name leaves the type. |
| Try again | **retry** | Run the card again on failure, per some rule. |
| Give up after a while | **timeout** | Fail with a timeout error if it takes too long. |
| An appliance the recipe asks for | **service** (`Context.Service`) | A described capability, like "a Blender that can blend." |
| The kitchen supplying the appliance | **layer** (`Layer.succeed`) | A way to build or provide a service. |
| A pretend blender for practice | **test implementation** | A fake service used to test a recipe without side effects. |
| Plugging in the appliance | **provide** (`Effect.provide`) | Satisfy a requirement; the "Needs" line shrinks. |
| A bookmark in a half-done recipe | **fiber** | A lightweight running Effect that can be paused, resumed, or stopped. |
| Several recipes in progress | **concurrency** | Many things underway with one cook. Not the same as many cooks. |
| Pulling the bookmark out | **interruption** | Stopping a fiber cleanly; its cleanup still runs. |
| First one done wins | **race** | Run two; keep the first result; interrupt the other. |
| Borrow it, always return it | **acquire / release** (`Effect.acquireRelease`) | Get a resource and guarantee cleanup on every ending. |
| The due date | **scope** | The window during which a borrowed resource is held. |

## Unit 2

| Kitchen picture | Programmer word | What it means |
|---|---|---|
| The routine chart on the wall | **schedule** (`Schedule`) | A plan for when to go again and when to stop, separate from any card. |
| Knock again because the box wasn't there | **retry with a schedule** (`Effect.retry(card, schedule)`) | Run the card again after a failure, following the schedule. |
| Wipe again because the counter is clean | **repeat** (`Effect.repeat(card, schedule)`) | Run the card again after a success, following the schedule. |
| 1 minute, then 2, then 4 | **exponential backoff** (`Schedule.exponential`) | Each wait is double the last one. Never stops on its own. |
| At most 3 more times | **`Schedule.recurs`** | Go again up to N more times. The first run doesn't count. |
| Follow both rules on the chart | **`Schedule.max([a, b])`** | Go again only while both schedules say yes; wait the longer of their two gaps. |
| The kitchen whiteboard | **Ref** (`Ref.make`) | A box holding one value that several fibers share. Making one is a card, so each run gets a fresh one. |
| Look, add one, write it back, in one step | **`Ref.update`** | Change the value with a function, all at once, so no other fiber can cut in. |
| Three sales, board says 1 | **lost update** (race condition) | A fiber reads, pauses, and writes back an old number, erasing other fibers' changes. |
| The order shelf between counter and blenders | **queue** (`Queue.bounded`) | A line of values between fibers: one side puts in, the other takes out, first in, first out. |
| Putting a slip on / taking one off | **offer / take** (`Queue.offer`, `Queue.take`) | Add a value (waits if full) / remove the oldest (waits if empty). |
| The full shelf pushing back on the counter | **backpressure** | A slow taker makes a fast putter wait, so work never piles up without limit. |
| The loudspeaker | **PubSub** | Like a queue, but every listener gets every message. |
| A conveyor belt of fruit | **stream** (`Stream`) | A plan that hands you many values, one after another, maybe forever. Nothing moves until it's run. |
| The belt moves only when someone reaches | **pull-based** | Nothing upstream is made until the consumer asks for the next value. |
| Wash / toss bruised / only the first 5 | **`Stream.map` / `Stream.filter` / `Stream.take`** | Change every value / keep only some / stop after n, even on an endless belt. |
| A sealed crate nobody has opened | **unknown** | TypeScript's type for "could be anything"; check it before using it. |
| The packing list by the back door | **schema** (`Schema.Struct`) | A description of what data should look like. Checks real data while running and gives TypeScript the type. |
| Checking a delivery against the packing list | **decoding** (`Schema.decodeUnknownEffect`) | Turning unknown outside data into a value you can trust, or failing with what's wrong. |
| The rejection slip | **SchemaError** | The error on the "Can go wrong" line when a delivery doesn't match. |
| The kitchen diary | **log** (`Effect.log`) | A line written while the program runs, so you can find out later what happened. |
| Whisper, normal voice, watch out, problem! | **log level** (`logDebug` / `logInfo` / `logWarning` / `logError`) | How serious a line is. Quiet ones can be turned off. |
| A sticky note on every line | **annotation** (`Effect.annotateLogs`) | Extra info, like `{ order: 42 }`, added to every log line inside. |
| A stopwatch in the diary | **log span** (`Effect.withLogSpan`) | Adds how long a step has been running, like `blend=122ms`, to each line. |
| One bar on the timeline | **span** (`Effect.withSpan`, `Effect.fn("name")`) | A named step with a start and an end, for a tracing tool to draw. |
| A practice run with a checklist | **test** (`it.effect`) | Run a recipe in the practice kitchen and check the result is what it should be. |
| Ty checking his clipboard | **`expect(x).toBe(y)`** | Say what the result should be; the test fails if it isn't. |
| The magic wall clock | **test clock** (`TestClock`) | A pretend clock that only moves when the test says so. |
| Turning the knob | **`TestClock.adjust("10 minutes")`** | Jump the test clock forward; waits that are due finish right away. |
