# Effect, Explained to 7th and 8th Graders

Two month-long units that teach the ideas behind **Effect for TypeScript (version 4.0)**
to middle-school computer science students, without drowning them in jargon.

The units are built on one running story: **a kitchen**. JavaScript is a kitchen with one cook.
Promises are order receipts. Effects are recipe cards. Services are the appliances a recipe needs.
Fibers are bookmarks in half-finished recipes. Every lesson adds one thing to that picture,
so students never have to hold more than one new idea at a time.

Unit 1 (lessons 1 to 7) builds the recipe card. Unit 2 (lessons 8 to 14) runs a busy kitchen with it:
routines, a shared whiteboard, an order shelf, a conveyor belt, checked deliveries, a kitchen diary,
and a practice kitchen with a magic clock.

## The illustrated version

The same fourteen lessons as an interactive web page, with SVG comic panels (Sam the cook, Maya the customer,
Ty the type checker), mechanism diagrams, and a small hands-on demo per lesson:
**https://claude.ai/artifact/8xbKVQ6zzg9G5WXUJepXxD**

Its source lives in `site/src` (one file per lesson, plus `sprites.svg` for the cast and shared props and
`sprites-lNN.svg` for props added by later lessons).
Run `python3 site/build.py` to rebuild `site/dist/index.html`.

## The lessons

### Unit 1: The recipe card

| # | Lesson | The one big idea | Kitchen picture |
|---|--------|------------------|-----------------|
| 1 | [Waiting Is Normal](lessons/01-waiting-is-normal.md) | JavaScript has one cook. Waiting must not freeze the kitchen. | One cook, a timer, and a ticket rail |
| 2 | [Promises: The Receipt](lessons/02-promises.md) | A Promise is a receipt for a value that isn't ready yet. | The smoothie counter |
| 3 | [Effects: The Recipe Card](lessons/03-effects-the-recipe-card.md) | An Effect is a plan, not an action. Nothing happens until you run it. | Recipe card vs. the meal |
| 4 | [Errors You Can See](lessons/04-errors-you-can-see.md) | The card says what can go wrong, so the compiler makes you deal with it. | "Out of bananas" written on the card |
| 5 | [Asking for Help: Services](lessons/05-services-and-layers.md) | A recipe says what it needs. The kitchen supplies it. | "Needs: blender" and the pretend blender |
| 6 | [Many Things at Once: Fibers](lessons/06-fibers-and-concurrency.md) | One cook can keep many recipes going, and can stop one cleanly. | Bookmarks in several recipes |
| 7 | [Cleaning Up](lessons/07-cleaning-up.md) | Whatever you borrow, you give back, even when things go wrong. | The library book |

### Unit 2: The busy kitchen

| # | Lesson | The one big idea | Kitchen picture |
|---|--------|------------------|-----------------|
| 8 | [The Kitchen Routine: Schedules](lessons/08-schedules.md) | A schedule is a separate little plan for *when* to go again and when to stop. | The routine chart taped on the wall |
| 9 | [The Whiteboard: Shared State](lessons/09-shared-state.md) | When several bookmarks share one number, "read, change, write back" must be one step. | The "sold today" tally on the whiteboard |
| 10 | [The Order Shelf: Queues](lessons/10-queues.md) | A queue is a shelf between fibers. Empty or full, whoever finds it that way waits. | The shelf between the counter and the blenders |
| 11 | [The Conveyor Belt: Streams](lessons/11-streams.md) | A card hands you one thing; a stream hands you many, maybe forever, and only when asked. | A fruit conveyor belt with stations |
| 12 | [Checking the Delivery: Schema](lessons/12-schema.md) | Data from outside gets checked at the back door. One description checks it and gives the type. | The packing list and the inspector |
| 13 | [The Kitchen Diary: Logs and Spans](lessons/13-logs-and-spans.md) | Effect's diary lines know when, which bookmark, and which order, and can time each step. | The diary, sticky notes, and a stopwatch |
| 14 | [The Practice Kitchen: Testing](lessons/14-testing.md) | A card asks for its appliances and its clock, so a test can hand it pretend ones. | The pretend blender and a clock you wind by hand |

Extras:

- [Promise vs. Effect cheat sheet](lessons/cheat-sheet.md), one page, side by side
- [Glossary](lessons/glossary.md), every word we use, in kid language
- [Teacher's guide](lessons/00-teacher-guide.md), pacing for both units, misconceptions, and how to run the demos

## How the lessons are written

Every lesson has the same shape so students know what to expect:

1. **The big idea** in one sentence.
2. **The story**, told with the kitchen.
3. **A picture** (Mermaid diagrams, which render right here on GitHub).
4. **The tiniest possible code**, in TypeScript, using Effect 4.0 names.
5. **Check yourself**, three or four questions to talk about.
6. **Teacher notes**, including what to say when a sharp kid asks the hard question.

## Reference

`reference/effect` is a shallow git submodule of the Effect source ([Effect-TS/effect](https://github.com/Effect-TS/effect)),
pinned at the `effect@4.0.3` release, for checking API names. Fetch it with
`git submodule update --init --depth 1`. (Effect 4 was developed in `Effect-TS/effect-smol`; since the 4.0
release it lives in the main repository.)

## About the code

The snippets use the Effect 4.0 API. Every snippet in lessons 3 through 14 was type-checked and run
against `effect@4.0.3` (install with `npm install effect`) on 2026-10-11, and the lesson 14 tests were
run with `@effect/vitest@4.0.3` and `vitest@5`.

The code is deliberately tiny. The goal of these units is the *ideas*: a class that leaves knowing
"an Effect is a recipe card with three lines on it" has learned the thing that matters.
