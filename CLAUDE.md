# Life - A Python Journaling System

## What This Is

This repository is a creative coding experiment where life experiences, thoughts, and reflections are expressed through Python code. It's not a traditional software project - the code itself is the journal, the medium of expression.

## Philosophical Approach

### Thoughts Exist Independently

Thoughts are not "owned" by thinkers. They exist as independent entities, and people relate to them through different modalities:

```python
# Not this:
idea = Idea(thinker=I)

# But this:
IDEA = Idea(content="...")
I.thought(about=IDEA)
```

### Deep Inheritance Hierarchies

The system uses rich semantic layers (5-7 levels of abstraction):

- **Thoughts**: `Entity → MentalConstruct → Thought → Idea → CreativeIdea → ProjectIdea → SoftwareProjectIdea`
- **Activities**: `Entity → Activity → CreativeActivity → Writing → Journaling`
- **Artifacts**: `Entity → Artifact → DigitalArtifact → Codebase → Repository → PythonRepository`
- **Agents**: `Entity → Agent → Person`

Each layer adds semantic meaning - this creates poetic depth in the code.

### Modalities of Engagement

People engage with thoughts via kwargs that express different relationships:

```python
I.thought(about=something)           # contemplation
I.thought(that="something")          # belief/assertion
I.thought(about=LIFE, that="it sucks")  # mixing modalities
```

New modalities can emerge organically as journaling continues.

## Key Patterns

### UPPERCASE Constants

- People: `I = Person('Vova')`
- Global instances: `CODE_JOURNALING = Journaling(medium="code")`
- Important thoughts: `GENESIS_IDEA = SoftwareProjectIdea(...)`

### Type Hints

Everything is rigorously type-hinted using Python type annotations.

### No Re-exports

Import directly from specific files for clarity:

```python
from agents.people import I
from mental.ideas import SoftwareProjectIdea
```

### Minimalism

No database-like features (`id`, `created_at`, etc.) - keep it simple and poetic.

## Directory Structure

```
core/          - Foundation: Entity, categories, subjects
mental/        - Thoughts and ideas
activities/    - Things that are done
artifacts/     - Things that are created
agents/        - People and other agents
entries/       - Journal entries (dated files)
```

## How to Add New Entries

Create a new file in `entries/` with the pattern `_YYMMDD_description.py` (underscore prefix + YYMMDD for sortable dates):

```python
from agents.people import I
from mental.ideas import Idea

TODAYS_IDEA = Idea(content="...")
I.thought(about=TODAYS_IDEA, that="it's interesting")
```

Execute entries as modules:
```bash
python -m entries._260207_genesis
```

## Meta-Circularity

This system is special - it was born from the act of journaling its own creation. The first entry ([entries/_260207_genesis.py](entries/_260207_genesis.py)) records the idea that created the system, within the system itself:

```python
GENESIS_IDEA = SoftwareProjectIdea(
    content="journaling my life as a python repo...",
    is_meta=True  # Self-referential
)
I.thought(about=GENESIS_IDEA)
```

## Let It Evolve

The system is meant to grow organically:
- Add new thought types as they emerge
- Create new activity hierarchies when patterns appear
- Build temporal structures (Day, Week, Month) when needed
- Let the abstractions guide the journaling, and let the journaling shape the abstractions

"Let's take the road, we'll figure out the goal later, if ever."
