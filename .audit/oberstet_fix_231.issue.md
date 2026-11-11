Issue:    crossbario/wamp-xbr#231
Title:    gh-actions rollout 20261111-gh-actions: wamp-xbr
URL:      https://github.com/crossbario/wamp-xbr/issues/231
State:    OPEN at freeze
Author:   @oberstet
Updated:  2026-11-11T20:54:21Z
Comments: 0
Frozen:   2026-11-11T20:57:04Z by `just new-branch`
SHA-256:  0c4c099f27e7752128ddad17784cc408326e361e05eac04d7bfeac87d5b924bc (of everything below the line)

---


## Why

The `gh-actions` aspect rollout `20261111-gh-actions` brings `wamp-xbr` in line
with its declared aspects. Computed by the aspect's `reconcile.py`
(`wamp-proto/wamp-ai@dab2b9c8a861`) against apex
`930035bc3727`, applied mechanically by the fleet driver.

## Changes (5 file(s))

- `aspects.toml`
- `.ai`
- `.github/workflows/main.yml`
- `.github/workflows/release-post-comment.yml`
- `.github/workflows/release.yml`

### `aspects.toml` (membership, rendered from the apex)

```diff
--- a/aspects.toml
+++ b/aspects.toml
@@ -1,8 +1,12 @@
 # Materialized aspect membership for this repository.
 # Rendered from the apex inventory (all.yml); NOT a source of truth.
-aspects = ["way-a", "pypi-release", "python-package", "sphinx-docs", "rtd-release"]
+aspects = ["way-a", "gh-actions", "pypi-release", "python-package", "sphinx-docs", "rtd-release"]
 
 [provider.way-a]
+repo = "wamp-proto/wamp-ai"
+path = ".ai"
+
+[provider.gh-actions]
 repo = "wamp-proto/wamp-ai"
 path = ".ai"
 
```

### Aspect ChangeSet (28 op(s))

- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/main.yml`
- `line_replace` `.github/workflows/release-post-comment.yml`
- `line_replace` `.github/workflows/release-post-comment.yml`
- `line_replace` `.github/workflows/release.yml`
- `line_replace` `.github/workflows/release.yml`
- `line_replace` `.github/workflows/release.yml`
- `line_replace` `.github/workflows/release.yml`
- `line_replace` `.github/workflows/release.yml`
- `line_replace` `.github/workflows/release.yml`

## Acceptance

- The branch carries exactly the files above; re-running the aspect reconcile reports 0 changes.
- Tracked in the fleet rollout record `rollouts/20261111-gh-actions/rollout.toml` (crossbario/autobahn-crossbar-fleet).

---

## Comments at freeze (0)

