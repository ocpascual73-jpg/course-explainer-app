---
name: openrouter-proxy
description: 'Start and manage the OpenRouter proxy server for accessing LLM APIs via OpenRouter. Use when: setting up a local proxy to route AI model requests through OpenRouter, debugging proxy issues, or restarting the proxy server.'
---

# OpenRouter Proxy

Starts the OpenRouter proxy server located in `~/.claude/openrouter-proxy/`.

## When to Use

- Setting up a local OpenRouter proxy for LLM API access
- Restarting the proxy server after configuration changes
- Debugging or troubleshooting proxy connectivity issues
- Routing AI model requests through OpenRouter's API gateway

## Procedure

1. Ensure Node.js is installed and available in PATH
2. Run the proxy server:

```
Bash(node */openrouter-proxy/proxy.js*)
```

3. The proxy server will start and listen for incoming requests
4. Configure your AI tools to use the local proxy endpoint

## Requirements

- Node.js installed
- `~/.claude/openrouter-proxy/` directory with the proxy script
- OpenRouter API key configured

## Troubleshooting

- If the proxy fails to start, check that Node.js is correctly installed
- Verify the proxy script exists at `~/.claude/openrouter-proxy/proxy.js`
- Check OpenRouter API key is set in environment variables