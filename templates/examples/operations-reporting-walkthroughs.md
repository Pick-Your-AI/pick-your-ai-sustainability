# Four synthetic operations and reporting walkthroughs

Use the [operating procedure](../../docs/operations-and-reporting.md), [benefit record](../benefit-obligation-record.md) and [award report](../award-report.md). These four cases are **entirely synthetic**. Every `SYN-*` identifier, amount, unit, date, offer, receipt and decision below is an invented test premise, never an actual provider, applicant, financial event, appointment or agreement. None is inserted in live JSON or sent anywhere.

The author walks the stated input through the procedure and records the expected result below. Independent review must repeat that reasoning against the exact frozen revision; the presence of this document is not its acceptance. Actual project people, accounts, terms and benefit events remain Unknown / Unassigned.

## Case 1 — Awarded credits with unaccepted terms

### Synthetic input

- `SYN-01` has a confirmed synthetic provider decision offering 10,000 compute units. Its simulated lifecycle is Awarded; no receipt or usable entitlement is established.
- The exact offer requires confidentiality, a reporting clause and expiry conditions. Those terms are available as a synthetic offer, but **not accepted**. The offer's nominal currency equivalent is not evidence of actual cash.
- Existing synthetic preparation/submission authority covers only those actions. Acceptance, activation and spending are not included.
- The actual applicant/custodian and mandated operating roles are unresolved within this test. No effective overage stop has been demonstrated.
- The operator is asked to mark Activated merely because the award email exists.

### Manual application

1. Record the provider decision and its conditions under Awarded. Keep terms reviewed and terms accepted as different fields.
2. Check the #68 action scope: preparation/submission authority cannot cover acceptance or activation.
3. Apply the common activation sequence: actual terms acceptance, required recipient/role evidence, covered operating authority, bounded exposure and usable readback are missing.
4. Create a Pending/Blocked obligation row for the reported clause, without inventing its accepted terms or actual due trigger. The operation record is **Blocked**.
5. Leave actual cash receipt and usable units **Unknown**. Do not convert the 10,000 offered units into a cash amount, spending balance or realized avoided cost.

**Expected result: Awarded retained; activation Blocked.** There is no valid route from this input to Activated. Research and engineering preparation still have their existing scope.

### Discriminating changes

| Changed synthetic input | Required result |
| --- | --- |
| Mark the terms “read” instead of “accepted” | Still Blocked; source review is not acceptance. |
| Add accepted terms but leave actual role, activation authority and overage control unresolved | Still Blocked for those exact missing prerequisites. |
| Add a nominal credit balance without verified account/recipient identity | Still Blocked; a balance alone is not usable covered entitlement. |
| Supply every applicable identity, accepted agreement, exact mandate, effective control and independently reviewed usable readback as explicit synthetic evidence | The procedure permits recording only that verified covered activation; it does not retrospectively change earlier blocked attempts. This conditional control is a reasoning input, not an executed activation. |

**Author walkthrough result:** the award-only proposal and all three incomplete variants remain blocked; the final complete-evidence control has a defined route. Independent reviewer, exact reviewed revision and actual acceptance: **Pending / Unassigned**.

## Case 2 — Cash, unused credits and a loan cannot form one income total

### Synthetic input and ledger

The test defines one USD restricted fund with an **explicitly known opening balance of USD 0**. It has one synthetic gross cash receipt of USD 1,000, a separately evidenced USD 50 settlement fee, and USD 250 of independently approved eligible payments. The fee is a fixture fact, not a real host rate. No other cash or liability event is in this fixture.

Two separate synthetic records contain 10,000 available credits and one loaned device. The credits have a quoted face value of USD 5,000; 2,000 eligible units have actually been consumed, 8,000 remain available. The loaned device has a quoted list price of USD 600, is in custody and must be returned; title was not donated.

| Record | Actual synthetic measure | Permitted total |
| --- | --- | --- |
| `SYN-02-CASH` | USD 1,000 gross − USD 50 fee = USD 950 net receipt | Restricted USD receipt and fee ledger |
| Same restricted fund | USD 0 opening + USD 950 net − USD 250 payments = **USD 700 closing** | Restricted cash only; gross-style equivalent is 0 + 1,000 − 50 − 250 = 700 |
| `SYN-02-CREDIT` | 10,000 available − 2,000 used = **8,000 unused units** | Credit units; quoted USD 5,000 remains face value |
| Same credit use | A documented synthetic alternative purchase for this same useful 2,000-unit scope would cost USD 0.02/unit; actual incremental cash charges are explicitly USD 0 in this fixture | **USD 40 realized avoided cost** = 2,000 × 0.02 − 0, in a separate value column |
| `SYN-02-LOAN` | One unit received in custody; zero donated units by the explicit fixture's loan terms | Custody/return ledger; no USD 600 cash or owned-gift value |

### Manual application and negative controls

1. Reconcile the cash by its single defined fund/currency/custodian. Do not add the gross USD 1,000 a second time after booking net USD 950.
2. Keep USD 700 closing restricted cash separate from USD 40 avoided cost and 8,000 unused credit units. The fixture's unrestricted cash and loan proceeds are explicitly absent, not inferred from an unknown real account.
3. Reject `700 + 5,000 + 600 = 6,300` as “cash available” or “realized unrestricted income.” It combines cash, unused entitlement face value and someone else's loaned property.
4. Reject adding the USD 40 avoided-cost measure into the restricted cash balance. It describes a counterfactual purchase, not money paid into the fund.
5. Remove the counterfactual purchase/need evidence: the avoided-cost field becomes **Unknown**, even though consumption and face value are still known. A list price alone cannot restore it.
6. Present the same USD 250 purchase again under a new reimbursement record: the #24 duplicate check links it to the paid expense and blocks a second settlement. A new record name cannot create a new eligible cost.
7. Change the loan status to “donation” without title-transfer evidence: reject the reclassification and retain the loan obligation. A delivery receipt proves custody, not ownership.

**Author walkthrough result:** the two cash equations agree at USD 700; credit conservation gives 8,000 units; separately supported avoided cost is USD 40. All mixed-total, missing-counterfactual, duplicate and title-change variants fail their stated control. No real cash balance, valuation, tax acknowledgment or payment is asserted. Independent review: **Pending**.

## Case 3 — Partial output and unknown trigger remain open in a report

### Synthetic input

`SYN-03` assumes a valid covered activation and a reporting activity solely for this simulation. Its agreement has three original deliverables A, B and C, and two obligations:

- `SYN-03-O1`: report the whole agreed 200-check evaluation and attach all three deliverables.
- `SYN-03-O2`: a final narrative is due **30 calendar days after accepted delivery**. The trigger's accepted-delivery event has not occurred; no actual due instant can be calculated.

Observed synthetic output: deliverable A is complete, B is partial and C was not run. Of the planned 200 checks, 120 pass, 10 fail and 70 are not run. No amendment reducing scope has been accepted. The report exists as a draft; no actual dispatch is part of the fixture.

### Filled report snapshot

| Planned requirement | Actual synthetic evidence | Report disposition |
| --- | --- | --- |
| All 200 checks | 120 Pass + 10 Fail + 70 Not run = 200 | **Partial**; do not call the 120 passing subset the complete plan |
| Deliverable A | Exact synthetic artifact revision and covered technical review exist | Delivered for its stated scope |
| Deliverable B | Original failure evidence and unfinished scope retained | Partial; remaining action explicit |
| Deliverable C | No execution or artifact | Not run; no fabricated placeholder result |
| `O1` full report/attachments | Draft accurately includes the partial/failure/not-run rows | Draft may be reviewed; full required delivery remains incomplete |
| `O2` accepted-delivery + 30 days | Trigger event absent | Due instant **Unknown**, reason and trigger recorded |
| Provider response | No confirmed dispatch | Submission, acknowledgment and acceptance **Unperformed/Unknown**, separately recorded |

### Manual application and negative controls

1. Confirm planned and observed scope match the same period and 200-check denominator; preserve original failing and unexecuted rows.
2. Review the actual draft and exact artifacts. A reviewer may accept its accurate account of incomplete work without certifying that all deliverables are satisfied.
3. Treat a proposed reduction to 120 checks as a proposed deviation only. Without actual amendment authority and provider acceptance where required, the original 200-check obligation remains.
4. Reject a due date calculated from the award date, draft-report date or an arbitrary midnight: the governing trigger is accepted delivery, which is absent. Even after a real trigger exists, its recorded date/time precision and applicable rule must support the calculation.
5. Add a synthetic “received” acknowledgment after a separately authorized confirmed report dispatch: only the Submitted/Acknowledged fields advance; provider output acceptance and remaining obligations remain open.
6. Add an actual synthetic waiver only for deliverable C: close only that waived scope, preserving the original C Not run history. B and any remaining report/financial duties stay open.

**Author walkthrough result:** the draft can faithfully report partial work; it cannot erase 10 failures, invent 70 executions, close the whole obligation or fabricate a deadline. An acknowledgment and a scoped waiver cannot establish whole-project acceptance. Independent review: **Pending**.

## Case 4 — Changed renewal and partial return prevent blanket closeout

### Synthetic input

`SYN-04-LICENSE` is usable under an accepted synthetic license through **2026-11-30 23:59:59 UTC**, an explicit fixture term. Its current authority covers the existing period only. A proposed renewal introduces new data-use and recurring-charge conditions; their cost, permitted data use and exact renewed authority remain unresolved. The fixture does not claim an automatic renewal setting.

A separate `SYN-04-LOAN` is due for return under its own fixture terms. A shipping receipt exists, but no recipient confirmation or accepted title transfer exists. A draft final report and export request are present, but final report acceptance and successful export verification are missing.

### Manual application

1. Preserve the current license's actual permitted use and historical activation. Suspend only the uncovered renewal action while its changed terms, cost, actual control settings and authority are reviewed.
2. Do not infer auto-renewal is disabled from an internal reminder. The operation record must obtain actual configuration/term evidence and a covered stop/exit action before the relevant boundary.
3. Record the loan as **Return in progress**, not Closed. Shipment and recipient acceptance are different facts.
4. Record export as requested but unverified; keep final report acceptance and settlement review unresolved.
5. Leave overall closeout **Partial/Blocked**, explicitly listing each missing item. Do not set a new canonical lifecycle value “Closed.”
6. In a positive control, add synthetic recipient-confirmed return, verified required export, required revocation/settlement and accepted final report, each with covered authority and independent review. Close exactly those evidenced items.
7. If retention or confidentiality duties survive, retain their actual clause, period/trigger, owner and follow-up separately. Unknown retention duration cannot be replaced by a universal deletion date or silently discharged by closing the return record.

### Discriminating changes

| Proposed shortcut | Expected response |
| --- | --- |
| Reuse old license approval for materially different renewal | Block the changed renewal; preserve the old covered period |
| Treat a calendar reminder as proof of disabled paid renewal | Reject; actual setting/terms remain unverified |
| Treat tracking/shipment as accepted return | Keep return open |
| Treat an export request as verified recoverability | Keep that obligation open |
| Use a successful return to mark every obligation Closed | Reject while report, finance, retention or other required evidence remains |
| Supply complete evidence for one covered item | Close that item, retaining open residual duties and all historical events |

**Author walkthrough result:** the incomplete case cannot renew or reach blanket closeout. The positive control closes only the actually covered items. No license, account, loan, export, termination, report or contract action was performed. Independent review: **Pending**.

## Manual review receipt fields

The independent reviewer records the exact five-path revision, actual read scope and each case's result:

| Case | Required review conclusion | Actual reviewer / decision |
| --- | --- | --- |
| 1 | Awarded-with-unaccepted-terms and other incomplete variants stay blocked; the complete-evidence control has a defined route | Unassigned / Pending |
| 2 | Separate cash/unit/custody totals and counterfactual evidence prevent inflation, duplicate payment and false ownership | Unassigned / Pending |
| 3 | Partial results, missing trigger, acknowledgment and scoped waiver preserve remaining obligations | Unassigned / Pending |
| 4 | Changed renewal and incomplete return/export/report cannot yield blanket closure | Unassigned / Pending |

Record real findings and corrections without rewriting their original result. A local schema/link validator does not execute these operating decisions or supply independent findings acceptance.
