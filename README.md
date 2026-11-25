# ple-engineer-harness

Autonomous engineering agent harness for **Google - Agent Harness on Physical-Engineering's Last Exam (PLE)**.

## Architecture

Built on the competition WebSocket protocol (`taskbridge.py`) with an OpenAI-compatible streaming client (`serve.py`), supporting all `google-cloud/*` foundation models:

- **Disciplined Engineering Workflow:** Enforces full workspace/MCP reconnaissance, explicit separation of hard constraints vs. design objectives, code-backed engineering calculations with unit verification, and real binary deliverable generation.
- **Independent QA/QC Verifier (`verify_once`):** After the engineer finishes, a fresh-context, read-only verifier inspects deliverables on disk, checks syntax/execution/archive integrity and hard constraints, and returns `VERDICT: PASS` or `VERDICT: FAIL` with concrete defects for up to `VERIFY_ROUNDS` fix iterations.
- **Long-Horizon Reliability:** Streaming with exponential backoff retries, Claude prompt-prefix caching (`cache_control`), Gemini thought-signature preservation, concurrent `read_file` batch execution, and constraint-preserving context compaction.

## Local Checks & Evaluation

From the `ple/` evaluation kit directory:

```bash
# Validate submission.yaml, build container, and run protocol checks
uv run python -m kit check ../ple-engineer-harness

# Run the 29-task public dev set and generate artifacts/
uv run python eval/run.py ../ple-engineer-harness --env-file local.env
```

Unit tests:

```bash
uv run --with-requirements requirements.txt python -m unittest -v tests/test_serve.py
```
