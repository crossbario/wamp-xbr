Issue:    crossbario/wamp-xbr#220
Title:    CI: compile the contracts on Node 22 (not 20), and stop `npm install` from rewriting the committed package-lock.json
URL:      https://github.com/crossbario/wamp-xbr/issues/220
State:    OPEN at freeze
Author:   @oberstet
Updated:  2026-11-09T04:35:01Z
Comments: 0
Frozen:   2026-11-09T04:50:00Z by `just new-branch`
SHA-256:  eb4affbc768f11b80b082b9921682e816f1b51c327a4a9516708e0edc5d0e90f (of everything below the line)

---

## What happens

A replay of `.github/workflows/main.yml` at `a344329`, job by job, on a fresh x86_64 Linux machine, found two things. Every job passed.

1. **The contracts are compiled on Node 20.**
   - `check`, `test` (all five legs), `docs` and `build` each run `actions/setup-node@v4` with `node-version: '20'` before `just compile-contracts`.
   - Node 20 reached its end of life in April 2026.
   - autobahn-js, the other WAMP repo with a Node toolchain, tests on Node 22, 24 and 25, and declares `"engines": {"node": ">= 22.0.0"}`.
   - The replay ran the whole chain on Node 22.23.4 with npm 10.9.9, and it passed in all eight jobs and legs. The chain is `npm install`, then Truffle's download of solc 0.6.12, then `truffle compile`, and the editable install and the tests after it.
2. **Every job leaves `package-lock.json` modified.**
   - At `a344329`, `package.json` says `"version": "25.12.2"`, while the committed `package-lock.json` still says `"version": "25.12.1"`.
   - `install-node-tools` runs plain `npm install`, and that reconciles the lockfile with `package.json` and re-resolves the tree with the npm in use. The rewrite is about 400 lines, including new platform entries such as `node_modules/@typescript/typescript-aix-ppc64`.
   - On a GitHub runner nobody sees this, because the runner is thrown away. But it means CI does not install the tree the lockfile records, and any local `just compile-contracts` leaves the working tree dirty.

A third thing, for context rather than to fix here: `npm install` fetches two dependencies of the Truffle/web3 1.x stack as GitHub tarballs (`web3-js/WebSocket-Node`, `web3-js/scrypt-shim`, from `codeload.github.com`), and the install logs are full of `npm warn deprecated` for `@truffle/*`, `apollo-server*`, `uuid@2.0.1` and others. Where `codeload.github.com` is not reachable, npm falls back to `git` over `github.com`.

## The change

1. **Node:** `node-version: '22'` in every `actions/setup-node` step of `main.yml`, and in any other workflow that sets one.
   - Add `"engines": {"node": ">= 22.0.0"}` to `package.json`, as autobahn-js has.
2. **The lockfile:**
   - Regenerate `package-lock.json` with `npm install` on Node 22 and commit it, so that it says `25.12.2` and matches the tree.
   - Change `install-node-tools` to run `npm ci` when `package-lock.json` exists, so that CI installs exactly the locked tree and fails when the two files disagree, instead of rewriting one of them.
   - Bumping the version (`package.json`'s `version`) then has to update the lockfile in the same commit. `npm version` does that.

## Done when

- `main.yml` uses Node 22, and a GitHub run of `main.yml` passes.
- After `just compile-contracts` in a fresh clone, `git status --porcelain` is empty.

---

## Comments at freeze (0)

