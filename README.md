# Effect, Explained to 7th and 8th Graders

A month-long unit that teaches the ideas behind **Effect for TypeScript (version 4.0 release candidate)**
to middle-school computer science students, without drowning them in jargon.

The unit is built on one running story: **a kitchen**. JavaScript is a kitchen with one cook.
Promises are order receipts. Effects are recipe cards. Services are the appliances a recipe needs.
Fibers are bookmarks in half-finished recipes. Every lesson adds one thing to that picture,
so students never have to hold more than one new idea at a time.

## The illustrated version

The same seven lessons as an interactive web page, with SVG comic panels (Sam the cook, Maya the customer,
Ty the type checker), mechanism diagrams, and a small hands-on demo per lesson:
**https://claude.ai/artifact/8xbKVQ6zzg9G5WXUJepXxD**

Its source lives in `site/src` (one file per lesson, plus `sprites.svg` for the cast and props).
Run `python3 site/build.py` to rebuild `site/dist/index.html`.

## The lessons

| # | Lesson | The one big idea | Kitchen picture |
|---|--------|------------------|-----------------|
| 1 | [Waiting Is Normal](lessons/01-waiting-is-normal.md) | JavaScript has one cook. Waiting must not freeze the kitchen. | One cook, a timer, and a ticket rail |
| 2 | [Promises: The Receipt](lessons/02-promises.md) | A Promise is a receipt for a value that isn't ready yet. | The smoothie counter |
| 3 | [Effects: The Recipe Card](lessons/03-effects-the-recipe-card.md) | An Effect is a plan, not an action. Nothing happens until you run it. | Recipe card vs. the meal |
| 4 | [Errors You Can See](lessons/04-errors-you-can-see.md) | The card says what can go wrong, so the compiler makes you deal with it. | "Out of bananas" written on the card |
| 5 | [Asking for Help: Services](lessons/05-services-and-layers.md) | A recipe says what it needs. The kitchen supplies it. | "Needs: blender" and the pretend blender |
| 6 | [Many Things at Once: Fibers](lessons/06-fibers-and-concurrency.md) | One cook can keep many recipes going, and can stop one cleanly. | Bookmarks in several recipes |
| 7 | [Cleaning Up](lessons/07-cleaning-up.md) | Whatever you borrow, you give back, even when things go wrong. | The library book |

Extras:

- [Promise vs. Effect cheat sheet](lessons/cheat-sheet.md), one page, side by side
- [Glossary](lessons/glossary.md), every word we use, in kid language
- [Teacher's guide](lessons/00-teacher-guide.md), pacing, misconceptions, and how to run the demos

## How the lessons are written

Every lesson has the same shape so students know what to expect:

1. **The big idea** in one sentence.
2. **The story**, told with the kitchen.
3. **A picture** (Mermaid diagrams, which render right here on GitHub).
4. **The tiniest possible code**, in TypeScript, using Effect 4.0 names.
5. **Check yourself**, three or four questions to talk about.
6. **Teacher notes**, including what to say when a sharp kid asks the hard question.

## Reference

`reference/effect-smol` is a shallow git submodule of the Effect 4 source, for checking API names.
Fetch it with `git submodule update --init --depth 1`.

## About the code

The snippets use the Effect 4.0 release-candidate API. Every snippet in lessons 3 through 7 was
type-checked and run against `effect@4.0.0-rc.118` (install with `npm install effect@rc`) on 2026-09-29.
A release candidate can still move, so if a name doesn't compile in class, check the current docs
before assuming the kid typed it wrong.

The code is deliberately tiny. The goal of this unit is the *ideas*: a class that leaves knowing
"an Effect is a recipe card with three lines on it" has learned the thing that matters.
