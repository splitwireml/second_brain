---
title: sandbox-as-worker pattern
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [agent, architecture, composition, iii, sandbox, worker]
sources: [raw/articles/xarticle-why-agent-sandboxes-are-converging-on-libkrun-not--2055329887431393309.md]
---

# sandbox-as-worker pattern

## Definition
The architecture where a sandbox is treated as one worker among many in a system, rather than a separate product with its own API, identity model, and observability surface. Used in [iii](https://iii.dev/).

## Contrast with Traditional Sandbox Products
**Traditional sandbox-as-a-product:**
- Separate API key
- Separate identity model  
- Separate observability
- Different trust domain
- Must connect your systems to vendor's webhooks

**Sandbox-as-worker (iii pattern):**
- Same engine hosts HTTP routes, queue workers, and sandbox daemon
- Same trace ID propagates through agent → sandbox::create → sandbox::exec
- Same config system controls image allowlists and topic subscriptions
- Same lifecycle for cleanup across all workers

## Benefits
1. **Single observability view**: Agent worker's logs and sandbox worker's logs appear together in OpenTelemetry
2. **Composable**: An agent worker can register a function that boots a sandbox, runs code, captures output, and shuts down — and that whole composite is itself a function other workers can call
3. **No "correlate across systems" failure mode**: The failure mode that compounds quadratically with number of agents in the loop never gets a chance to exist

## Example Usage
```typescript
iii.registerFunction('agents::run-untrusted', async ({ code }) => {
  const { sandbox_id } = await iii.trigger({
    function_id: 'sandbox::create',
    payload: { image: 'python', cpus: 1, memory_mb: 512 },
  });
  try {
    return await iii.trigger({
      function_id: 'sandbox::exec',
      payload: { sandbox_id, cmd: 'python3', args: ['-c', code] },
    });
  } finally {
    await iii.trigger({ function_id: 'sandbox::stop', payload: { sandbox_id } });
  }
});
```

## Related Entities
- [[iii-sandbox]] — implements this pattern
- [[iii]] — the engine that enables this pattern