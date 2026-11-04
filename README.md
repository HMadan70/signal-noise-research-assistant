# Signal & Noise newsroom research assistant

Signal & Noise builds research tools for newsrooms. The archive desk answers editors'
questions from decades of wire copy; today they use a prototype that greps the archive,
trusts whatever the model writes and numbers citations strangely. This repo is that
prototype, and you'll turn it into a research assistant the desk can rely on: it finds
evidence, runs tools within budgets, checks its citations and degrades gracefully when a
tool fails.

The client's rules: **only the Python standard library**, and everything **deterministic**
(the same input always gives the same output; no network, no real clock, seeded randomness).

Some parts exist already (the prototype and the code around it), some are stubs waiting for
you. You'll work on it task by task, all in this one repo. Read the existing code before you
change it: other modules and the desk's notebooks depend on it.

## Your tasks
**Your exact task is in Darbni.** Open the task there and read its description: it has the
rules for YOUR version. Every intern gets their own version of each task, so a solution
copied from someone else will fail the tests.

## Shared formats
`research_agent/formats.py` defines the structures modules pass to each other: the `Index`,
the `ParsedQuery` and the `ToolCall`. They are fixed. A function that takes an `Index` must
work with any index in that format, not only with one your own code built: Darbni's tests
build these inputs themselves.

## Where things are
| File | What it does |
|---|---|
| `research_agent/text.py` | the shared tokenizer (fixed) |
| `research_agent/formats.py` | the shared data formats (fixed) |
| `research_agent/hashing.py` | stable hashing with `hashlib`, never `hash()` (fixed) |
| `research_agent/prototype.py` | the desk's prototype: `answer(question, documents)` |
| `research_agent/chunking.py` | splits articles into chunks |
| `research_agent/query.py` | parses an editor's search query |
| `research_agent/citations.py` | turns `[@id]` markers into numbered citations |
| `research_agent/tool_schema.py` | one envelope for every tool call |
| `research_agent/index.py` | the positional inverted index |
| `research_agent/bm25.py` | BM25 ranking |
| `research_agent/phrases.py` | phrase search |
| `research_agent/fusion.py` | combines several rankings into one |
| `research_agent/tool_json.py` | reads tool calls out of a model's reply |
| `research_agent/tools.py` | the tools the assistant can call |
| `research_agent/retries.py` | retries with backoff, on a fake clock |
| `research_agent/cache.py` | an LRU cache with a time-to-live |
| `research_agent/agent.py` | the agent loop, within budgets |
| `research_agent/grounding.py` | checks that citations contain their claims |
| `research_agent/evaluation.py` | recall and nDCG against editors' judgments |
| `research_agent/dedupe.py` | near-duplicate stories (MinHash) |
| `research_agent/packing.py` | the best evidence for a token budget |
| `research_agent/feedback.py` | query expansion from the first results |
| `research_agent/incremental.py` | an index that updates in place |
| `research_agent/research.py` | the whole pipeline, with fallbacks |

## Run the tests
You need pytest:
```
pip install pytest
pytest tests/test_index.py        # the tests of the file your task is about
pytest                            # everything (tests for tasks you haven't done yet fail)
```
There is one example test per file. It works for every version, and it is far from enough:
write your own tests for the edge cases in your task. Darbni runs many more tests, made for
your version, when you submit.

## Submitting
Commit and push your work, then submit your repo URL and the full commit SHA in Darbni.
