# Glossary, in Kid Language

Kitchen word first, programmer word second, one sentence each.

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
