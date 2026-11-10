Issue:    crossbario/wamp-xbr#223
Title:    check-typing: follow ty 0.0.100's rule names, and ignore its two new rules for now
URL:      https://github.com/crossbario/wamp-xbr/issues/223
State:    OPEN at freeze
Author:   @oberstet
Updated:  2026-11-10T01:38:05Z
Comments: 0
Frozen:   2026-11-10T10:59:26Z by `just new-branch`
SHA-256:  aad74863ed92a020a9636a73e8cbe2a694fa78d3a45dcd8888ef48ba6bdd8844 (of everything below the line)

---

## Why

CI installs ty without a version (`uv tool install ty --prerelease=allow`). ty 0.0.100 (2026-11-09) fails `just check-typing cpy311` at master (`d44a673`) with 87 diagnostics. master's last CI run predates that release, so its next run, and any pull request's, will be red for this reason alone.

- **Two of the names the recipe ignores were renamed**, so they silence nothing:
  ```
  warning[renamed-rule]: Rule `invalid-method-override` has been renamed to `incompatible-method-override`
  warning[renamed-rule]: Rule `unresolved-attribute` has been renamed to `missing-attribute`
  ```
- **Two new rules report on code the old ones covered:**

  | rule | sites |
  | :-- | --: |
  | `missing-union-attribute` | 83 |
  | `lost-keyword-for-regular-parameter` | 2 |

The other names the recipe ignores are all current in 0.0.100. Run `uv tool install ty@latest` before trusting a local result.

The same change was made in crossbar (crossbar#2392) and autobahn-python (autobahn-python#2051). We follow ty rather than pinning it.

## The change

1. **Rename the two ignores** in `check-typing`:
   - `unresolved-attribute` becomes `missing-attribute`;
   - `invalid-method-override` becomes `incompatible-method-override`.
2. **Add `--ignore missing-union-attribute` and `--ignore lost-keyword-for-regular-parameter`**, with a follow-up issue to fix the 85 sites and drop both ignores.
3. **As in crossbar#2392,** the recipe prints ty's version, and after ty's output repeats any `unknown-rule`, `renamed-rule` or `renamed-rule-in-ignore-comment` warning and exits 1. The next rename then shows up as one named line, not as errors.

## Done when

- `just check-typing cpy311` passes with ty 0.0.100.
- With an old rule name put back, the recipe fails and names it.
- The follow-up issue exists.

---

## Comments at freeze (0)

