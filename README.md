# life

> *A Python repository that is also a journal. Deep inheritance hierarchies as existential cartography.*

## What is this?

This is an experiment in **code as medium**. Instead of writing about life in prose, I write it in Python - thoughts as classes, experiences as instances, existence as a type system.

```python

# entries/_260207_genesis.py

from agents.people import I
from mental.ideas import SoftwareProjectIdea

GENESIS_IDEA = SoftwareProjectIdea(
    content="journaling my life as a python repo...",
    is_meta=True  # This idea creates its own container
)

I.thought(about=GENESIS_IDEA)
```

## Philosophy

- **Thoughts exist independently** - they're not owned by thinkers, we merely relate to them through modalities (`about`, `that`, etc.)
- **Deep abstractions** - 5-7 levels of inheritance create semantic richness (e.g., `Entity → MentalConstruct → Thought → Idea → CreativeIdea → ProjectIdea → SoftwareProjectIdea`)
- **Organic evolution** - the system grows as journaling continues, discovering its own structure
- **Meta-circular** - the first entry journals the idea of creating the journal itself

## Structure

```
core/          Entity, categories, subjects
mental/        Thoughts and ideas
activities/    Things that are done
artifacts/     Things that are created
agents/        People (I = Person('Vova'))
entries/       Journal entries (_YYMMDD_description.py)
```

## Why?

*Let’s take the road, we’ll figure out the goal later, if ever.*

Some people meditate. Some go to therapy. I’m journaling my life in type-hinted Python with 7-level inheritance philosophies.

---

See [CLAUDE.md](CLAUDE.md) for technical details.
