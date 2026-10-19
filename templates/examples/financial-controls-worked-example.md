# Synthetic financial-control walkthroughs

Use with the [procedure](../../docs/operations/financial-controls-draft.md) and [blank record](../financial-control-record.md). **Every value and event below is fictional test data.** These cases establish no real recipient, account, balance, approval, expense, donor, gift, credit entitlement or receipt. They remain outside the canonical opportunity and funding registers. Actual project role holders and administrative facts remain Unassigned or Unknown.

## FC-01 — separate support categories and reject unaccepted terms

Assume solely for this example that a fictional custodian statement records one restricted cash receipt of USD 120, a documented fee of USD 12 and a separate processor fee of USD 2. The fictional fund restriction permits only a specified accessibility study. A separate fictional unrestricted opening balance is USD 50. An unrelated notice offers 500 credit units; its terms are unaccepted and no entitlement is accessible. A loan document describes one device whose owner retains title, with a stated retail comparison of USD 900.

| Observation | Correct control record | Prohibited inference |
| --- | --- | --- |
| Restricted receipt and documented fees | Restricted cash: USD 120 gross − USD 12 − USD 2 = **USD 106 net**. | Treat gross as spendable net or transfer it to a different purpose. |
| Unrestricted opening balance | Separate unrestricted cash: **USD 50**, under its own fictional statement/custodian evidence. | Assume all actual organizational balances are known or that restricted funds are freely spendable. |
| Conditional credit notice | In-kind proposed award: **500 credit units**; available units Unknown; terms unaccepted; activation blocked. | Add 500 to cash, assert USD currency or treat an award as usable access. |
| Loaned device | In-kind custody/loan record; title retained by the fictional owner. | Add USD 900 to received cash or describe a donated ownership gift. |

Within this fictional same-currency example, total observed cash is **USD 156**, explicitly split USD 106 restricted / USD 50 unrestricted. The credit and loan figures are excluded. A proposed USD 24 study expense has no recorded independent approval or signed terms: it remains proposed and unpaid, with **no change** to either cash balance. The credit activation also remains blocked. A reviewer must state those two gates explicitly rather than infer permission from available cash or a notice.

The fee numbers are supplied facts of this fictional case, not a predicted charge for any actual host. A real statement with different amounts would require its actual fee calculation.

## FC-02 — prevent a second reimbursement and reconcile a refund

Assume an entirely fictional approved and reconciled eligible purchase of EUR 80. Its original invoice/receipt is `SYN-RECEIPT-02`; the fictional payment trail confirms EUR 60 already reimbursed and no earlier refunds. A second request uploads a renamed copy and asks for another EUR 80.

The semantic duplicate search links the same vendor, purchase, date, currency, line items and receipt despite the new upload name. At this point the maximum remaining supported amount is **EUR 20**, subject to the actual valid authorization and other checks. A new ID does not authorize EUR 80 again. Do not convert this amount using a guessed USD exchange rate.

Now add a fictional confirmed EUR 30 vendor refund **received by the original out-of-pocket purchaser/payee** for the same purchase before any further reimbursement. Preserve the original purchase and reimbursement, then add the linked refund and its recipient. Net eligible cost is **EUR 50**; EUR 60 has already been reimbursed, so the arithmetic exposes **EUR 10 over-reimbursement**. A refund paid directly to the custodian would require a different settlement reconciliation; that is not this scenario. Further payment is blocked and the case requires an authorized reconciliation/recovery decision. Do not erase the original history, silently reduce a statement balance or issue an unapproved debit to the payee.

Expected reviewer result: identify the duplicate and the changed net-cost calculation, keep the unmatched EUR 10 visible, retain the original restriction/currency and leave the actual resolution pending. No real recovery instruction or contact occurs.

## FC-03 — distinguish approval, uncertain payment and a retry

A fictional record has a supported payable and prior independent approval, but its payment attempt returns an ambiguous result. The case supplies no custodian confirmation of success or failure.

Correct result: **payment uncertain; do not submit another payment yet**. Keep the attempt ID, prior approval and payable; reconcile the actual custodian state before deciding whether another attempt is appropriate. Neither approval nor a missing response proves settlement. A later confirmed result must be linked to the same underlying obligation so it is counted once. The public record may say that reconciliation is pending without exposing a payee, account or private statement.

If the only potential approver is also the fictional payee, this proposal's independent-approval gate is separately unmet. A sole-admin platform exception does not supply the missing independent decision. No actual role is appointed to resolve the example.

## FC-04 — review an unsent acknowledgment with unknown return benefits

A fictional candidate record says “a gift of one used computer,” but supplies no verified recipient classification, issuer mandate, title-transfer evidence or statement about goods/services supplied to the contributor. No real donor or contact is named.

Correct result: **draft only; acknowledgment dispatch blocked**. Preserve the property description without inventing a donor-gift value. Do not replace the unknown return-benefit field with a no-benefit assertion. Determine whether ownership was donated or the computer was merely loaned. The actual recipient and qualified reviewer must establish which acknowledgment or disclosure is applicable before preparing an exact statement; this example does not select a donor's tax treatment.

If a later fictional branch explicitly establishes an applicable charitable cash gift of USD 300 and an actual return benefit valued at USD 40, the draft must preserve both values and their evidence; it cannot assert no goods or services. The full payment exceeds the distinct USD 75 disclosure threshold discussed in the procedure. The applicable draft disclosure states that the deductible portion is limited to the amount exceeding the return benefit's fair market value and supplies the supported good-faith USD 40 value. Its solicitation-or-receipt delivery remains unperformed and must be recorded separately from donor acknowledgment timing. This branch remains a synthetic applicability exercise, not a dispatched receipt or a decision about a real deduction.

## Independent walkthrough receipt

Record the actual reviewer, exact source revision and review URL when the manual walkthrough is performed. The expected outcomes above are authored scenario definitions until separately checked. The reviewer must recompute both ledger/refund examples and explicitly confirm blocked unaccepted-term activation, absent independent approval, uncertain-payment retry and unresolved acknowledgment. Repository schema/link checks cannot supply that source acceptance.
