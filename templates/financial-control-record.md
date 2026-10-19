# Financial-control record

Use with the [financial-controls procedure](../docs/operations/financial-controls-draft.md). This blank form is not approval, a payment instruction, a donor receipt or an account-opening request. Complete a real record only in the actual authorized system. Copy only independently cleared public fields into GitHub; never fill the private section with real private information in this repository.

## Identity and current state

| Field | Value |
| --- | --- |
| Stable control-record ID and revision | Unknown |
| Existing opportunity / program / round | Unknown; Not applicable only with reason |
| Exact legal recipient or contracting party / operating route | Unknown |
| Actual host/custodian and governing agreement/version | Unknown |
| Public-benefit purpose and exact proposed output | Unknown |
| Record state and actual event/date | Draft; no actual transaction established |
| Prior version, related requests, invoices and payment attempts | Unknown |
| Current action gate and missing evidence | Blocked pending the concrete required authority and evidence |

Use separate facts for proposed, independently approved, obligated, delivered, submitted for payment, processing, failed, uncertain, confirmed settled, reconciled, refunded and closed. These control-record states do not replace the canonical opportunity lifecycle. Do not infer a payment from a submitted request, or a new payment entitlement from a revised ID.

## Amounts, custody and restrictions

| Field | Required content |
| --- | --- |
| Benefit / ledger class | Restricted cash, unrestricted cash, specific in-kind type, or commitment/payable; identify the actual classification evidence. |
| Fund ID, custodian and restriction | Exact permitted purpose and source clause; Unknown if unresolved. |
| Proposed maximum exposure | Amount/currency, term, taxes, fees, recurrence, overage and stop mechanism; Unknown inputs remain visible. |
| Available eligible funds and reservations | Reconciled statement period, balance, existing commitments and scope; never use zero for an unknown balance. |
| Actual cash settlement | Original amount/currency, gross, each actual fee, net, settlement date and safe transaction reference; Unknown until established. |
| Conversion | Original and settlement currencies, actual applied rate, source/date, fees and rounding; label any separate estimate. |
| In-kind benefit | Awarded versus available versus consumed units, rights, expiry and restrictions; owner/custodian/return conditions for property or loans. |
| Realized avoided cost | Counterfactual eligible purchase, same useful scope and actual avoided charge; Unknown until evidenced. Keep outside cash totals. |
| Refund / reversal / credit note | Link original entry, actual return or correction, affected fund/currency and restrictions; retain both histories. |

## Evidence and prior approval

| Check | Recorded finding / evidence / unresolved action |
| --- | --- |
| Current entity, host, applicant and account facts | Unknown |
| Actual requester/payee and any conflict | Unknown; retain private identity under authorized access |
| Quote or completed-work invoice; performance period | Unknown |
| Actual purchase/payment receipt if reimbursement | Unknown |
| Prior authorization before obligation | Unknown |
| Independent approver, actual capacity and scope | Unassigned / Unknown |
| Approved artifact revision, fund, amount/currency cap and term | Unknown |
| Distinct signer or host review where required | Unknown |
| Restriction, privacy, publication, branding and independence check | Unknown |
| Renewal, expiry, return/exit and reporting clauses | Unknown |
| Supported payee/payment prerequisites under custodian rules | Unknown; retain private details outside public copy |
| Current approval validity and changed-scope check | Unknown |

The requester/payee cannot supply the proposed independent approval for their own benefit. Record any permitted combination of other functions and its actual mandate. A platform's ability to approve a record does not establish the project's independent review.

## Duplicate, release and reconciliation trail

1. Record the systems/periods actually searched and compare payee/vendor, invoice/receipt identity, dates, amounts/currencies, line items, prior allocations, reimbursements and refunds. A file hash alone is insufficient. Missing search coverage remains explicit.
2. Reconcile the supported eligible amount with prior allocations and settlements; explain any remaining balance. Do not request the same cost again as both an invoice and a reimbursement.
3. Identify the actual authorized payment operator and release decision. Preserve the payment attempt reference and its observed state; an uncertain response remains unresolved until reconciled before retry.
4. Link confirmed settlement to the original payable and custodian evidence. Record the independent reconciler, period, equations, differences, result and actual review date.
5. Link remaining obligations, exact clause/deadline or trigger, owner/reviewer, reporting artifact/receipt, renewal decision and closeout. Unknown dates remain Unknown; accepted roles remain Unassigned until actually filled.

## Acknowledgment decision — draft only

| Field | Value |
| --- | --- |
| Actual recipient/issuer and authority for the statement | Unknown |
| Applicable gift classification, jurisdiction and review basis | Unknown |
| Cash amount/currency and actual gift date, if applicable | Unknown |
| Noncash property description, if applicable | Unknown; do not insert a donor-gift value into the charitable acknowledgment |
| Ownership gift versus loan, services or reimbursement | Unknown |
| Goods/services supplied in return and applicable supported value | Unknown; never replace Unknown with “none” |
| Applicable acknowledgment/disclosure basis and actual timing | Unknown; distinguish donor substantiation from recipient disclosure |
| Quid pro quo disclosure content and delivery, if applicable | Unknown; record the deductible-excess statement, good-faith return-benefit value and whether furnished with this solicitation or receipt; establish any applicable exception |
| Exact unsent statement, reviewer and intended private channel | Draft not prepared; reviewer Unassigned; channel Unknown |
| Actual dispatch / receipt evidence | None created by this template |

## Public and private separation

**Candidate public projection:** stable ID, permitted category/amount if independently cleared, project purpose/output, state, named unresolved gate and safe decision reference. Record who authorized each disclosure and what was actually reviewed. Omit confidential names, terms or amounts where disclosure is not established.

**Private system only:** actual payee/donor identity and contact, bank/payment details, credentials, tax records, unredacted invoice/receipt, sensitive agreement and authorization evidence. Record the actual custodian and access policy there, not an invented storage destination. Reference only an opaque safe ID publicly; do not publish an access-bearing link, private document or a hash of sensitive values.

## Review and disposition

- Exact reviewed revision and scope: Unknown.
- Actual independent reviewer and capacity: Unassigned.
- Findings, exceptions and missing evidence: Unknown.
- Decision: Draft / action blocked until required evidence and authority are accepted.
- Actual accepted-revision and review reference: Unknown.
- Next event or selected internal follow-up date and accepted owner: Unknown / Unassigned.

See the [synthetic worked examples](examples/financial-controls-worked-example.md) for the expected behavior. Their dates, values and case identities never populate a real ledger.
