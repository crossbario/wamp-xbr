Issue:    crossbario/wamp-xbr#224
Title:    check-typing: fix the 83 missing-union-attribute and 2 lost-keyword-for-regular-parameter sites, then stop ignoring both rules
URL:      https://github.com/crossbario/wamp-xbr/issues/224
State:    OPEN at freeze
Author:   @oberstet
Updated:  2026-11-10T01:38:14Z
Comments: 0
Frozen:   2026-11-11T01:19:52Z by `just new-branch`
SHA-256:  d8f340fb85b36caf78470983ff21632da28d2f30aa7b92ddaa5060ac5dcfdca4 (of everything below the line)

---

## Why

ty 0.0.100 added two rules. `check-typing` ignores both since the rule-name change, so CI could follow ty. Under `src/xbr/` they report:

| rule | file | sites |
| :-- | :-- | --: |
| `missing-union-attribute` | `_seller.py` | 26 |
| | `test/` | 20 |
| | `_buyer.py` | 15 |
| | `_blockchain.py` | 10 |
| | `_cli.py` | 7 |
| | `_schema.py` | 3 |
| | `_secmod.py` | 2 |
| `lost-keyword-for-regular-parameter` | `_eip712_authority_certificate.py:312` | 1 |
| | `_eip712_delegate_certificate.py:289` | 1 |

The unions behind `missing-union-attribute`:

| union | sites |
| :-- | --: |
| `None \| Unknown` / `Unknown \| None` | 43 |
| `EIP712DelegateCertificate \| EIP712AuthorityCertificate` | 18 |
| `None \| (Unknown & ApplicationSession)` | 6 |
| `None \| (Unknown & CallDetails)` | 4 |
| others | 12 |

Most are a value that may be `None`. The 18 certificate sites are not: an attribute that one of the two certificate classes has and the other does not, used on a value that may be either. Each of those is either a missing type check or a missing attribute.

## The change

1. For the 18 certificate sites, check the type before using a class's own attribute, or give both classes the attribute.
2. Fix each `None` site by what it means:
   - `assert x is not None`, or a narrowed local, where the value is set by then;
   - a real `None` check, where it may not be;
   - a declared type without `None`, where the attribute is always set before use.
3. Fix the two overrides so that they keep the base class's keyword parameters.
4. Remove both ignores from `check-typing`.

## Done when

- `just check-typing cpy311` passes with the newest ty, without the two ignores.
- The test suites pass.

---

## Comments at freeze (0)

