# Design Document Issues Report

## 1. Logical and consistency issues

1. **The bike-rental invariant is incorrect or ambiguous.** The invariant section says that “every bike has exactly one renter.” A bike should be associated with one rental at a time, not one renter permanently. It may have many rentals over its lifetime, provided their active rental periods do not overlap.

2. **Rental status is used but is not modeled consistently.** The `createRental` and `completeRental` interface descriptions refer to an active/completed rental status, but the `RENTAL` entity and `Rental` class do not include a `rentalStatus` attribute. Add and define this status, or revise the interfaces so they do not depend on it.

3. **Payment status is referenced but missing from the data model.** `processPayment` says it updates payment status and that unsuccessful transactions are marked unpaid. However, neither the `PAYMENT` entity nor the `Payment` class has a `paymentStatus` attribute. Add a defined payment-status field and specify its possible values.

4. **The rental-to-payment relationship assumes exactly one payment per rental.** Both diagrams show a one-to-one relationship. This may be valid if the system permits only one payment record per rental, but it does not accommodate retries, partial payments, deposits, or refunds represented as separate payment records. The design should state the intended rule and make the diagrams and interface behavior agree.

5. **Bike availability is not fully defined for rentals with scheduled time periods.** `checkBikeAvailability` accepts a start and end time, while the bike also has a general `Status` field. The design should distinguish a bike's condition/operational status (for example, available for service or under maintenance) from whether it is already booked during a particular time interval.

6. **Rental time fields are ambiguous.** The ER diagram and class diagram use `EndTime`/`endTime`, while `completeRental` accepts a `returnTime`. It is unclear whether the end time is the planned rental end, the actual return time, or both. These should be separate fields if the system needs to track both.

7. **Rental pricing rules conflict or are underspecified.** The Bike entity stores an `HourlyRate`, but `calculateRentalCost` guarantees the “hourly daily weekly rate.” The design does not define daily or weekly rates, how rental duration is rounded, or how the rates interact. The pricing attributes and calculation rules should be made consistent.

8. **The payment amount is not tied clearly to the calculated rental cost.** `processPayment` accepts an amount supplied by the caller, but the requirements do not say whether that amount must equal the calculated rental cost, whether overpayment or underpayment is allowed, or how a mismatch is handled.

9. **The customer and bike references are not represented as attributes in the Rental class.** The class diagram shows relationships to `Customer` and `Bike`, which may be sufficient in an object-oriented model, but the relationship implementation should be clear and consistent with the `CustomerID` and `BikeID` foreign keys in the ER diagram.

10. **The invariants are too vague to verify.** “Payment status must always be correct” does not define correctness. State specific conditions, such as a `PAID` payment having a successful processor result and being associated with an existing rental. “Only available bikes can be rented” should also define how availability is determined for the requested rental period.

## 2. Interface specification issues

1. **The interface descriptions are incomplete relative to a full function contract.** They do not consistently include all of the requested contract sections, such as Purpose, Requires, Outcomes, Guarantees, and Notes. Several functions provide only a short requires/outcomes/guarantees description.

2. **Some parameter and return types are not fully specified.** `Customer`, `Rental`, and `Payment` are used as return types, and `DateTime` is used as a parameter type, but the document does not define these types or the values/fields they contain. Define these non-primitive types in the Interfaces introduction.

3. **The `registerCustomer` contract is unclear about invalid input.** It says the names and email must be valid and unique, but it does not define what happens if registration fails or whether the function returns an error, null value, or another result.

4. **`checkBikeAvailability` does not define behavior for an unknown bike ID.** The precondition says the bike ID must refer to an existing bike, but the interface should state whether invalid input is rejected, reported as an error, or treated as unavailable.

5. **`createRental` depends on an availability check but does not define an atomic operation.** Another request could reserve the bike after the check and before the rental is saved. The creation operation must recheck and reserve the bike as one protected transaction to prevent overlapping rentals.

6. **`createRental` does not specify the result when creation fails.** Its return type is `Rental`, but the contract does not say how failure is represented if the customer, bike, dates, or availability check is invalid.

7. **`calculateRentalCost` has an incomplete pricing contract.** It does not specify whether the rental must be active or completed, which time interval is used, how partial hours are rounded, or how currency precision is handled.

8. **`processPayment` does not define the relationship between payment failure and rental status.** It says payment status is updated, but does not specify whether a rental can be active before payment, whether it is held pending payment, or what happens if payment fails after a rental record is created.

9. **`completeRental` does not define how damage or failed inspection is handled.** The failure-mode table says a damaged bike should be placed under maintenance, but the interface contract only says the bike returns to the available pool. Include the inspection result or define a separate return-inspection operation.

10. **Error handling is not specified consistently.** The functions mix object, numeric, and Boolean return types without defining how validation errors, missing records, or external payment errors are communicated.

## 3. ER diagram and class diagram issues

1. **The two diagrams do not contain all the fields used by the interface descriptions.** In particular, rental status and payment status are missing, even though the interfaces rely on them.

2. **The class diagram omits method parameter and return types.** Methods such as `rentBike()`, `checkAvailability()`, `calculateCost()`, and `processPayment()` are shown without signatures detailed enough to compare with the Interfaces section.

3. **The class methods do not align clearly with the six interface functions.** For example, the interface includes `registerCustomer`, `createRental`, and `completeRental`, while the class diagram lists different or less specific method names. Identify which class owns each interface operation and use consistent names/signatures.

4. **The ER diagram uses `decimal` for money while the class diagram uses `double`.** These representations can behave differently for currency calculations. Choose a consistent monetary representation and document its precision.

5. **The diagrams use different date/time type names.** The ER diagram uses `datetime`, while the class diagram uses `Date`. The interfaces use `DateTime`. Use consistent terminology and define the chosen type.

6. **The diagrams do not document the allowed values for status and type fields.** Fields such as `Bike.Status` and `Bike.Type` are represented as unrestricted strings. Define their permitted values, preferably as enumerated types or constrained fields.

7. **The cardinality notation should be explained in the document.** The intended one-to-many relationships from Customer to Rental and Bike to Rental, and the one-to-one Rental to Payment relationship, should be stated in words and checked against the business rules.

## 4. Invariant issues

1. **The invariant list is not precise enough.** “Every bike has a unique identifier key” and “every customer must have a unique identifier” should explicitly say that identifiers are non-null and unique across their respective records.

2. **The availability invariant needs a time-period rule.** It should state that a bike cannot have two overlapping active or confirmed rentals, rather than relying only on a general `AVAILABLE` status.

3. **Important relationship invariants are missing.** Every rental should reference exactly one existing customer and one existing bike; every payment should reference an existing rental.

4. **The payment invariant needs explicit conditions.** Define the allowed payment states and what evidence is required for a payment to be considered paid, failed, or refunded.

## 5. Failure-mode section issues

1. **The failure modes are useful examples, but some recovery actions are not connected to a defined interface.** For example, the damaged-bike recovery action requires an inspection and a maintenance-status update, but no inspection function or detailed return procedure is specified.

2. **“Bike Return Failure” combines two different failure cases.** A damaged bike and a return that is not recorded have different causes, detection methods, and recovery steps. Consider separating them into distinct failure modes.

3. **The payment failure description does not cover uncertain payment outcomes.** An external processor may time out after receiving a request, leaving the system unsure whether the payment succeeded. The design should explain how it checks transaction status and prevents duplicate charges on retry.

4. **The failure-mode table does not state what happens to the rental record after each failure.** In particular, clarify whether an unpaid rental is cancelled, left pending, or held temporarily.

5. **The failure-mode examples do not cover all important interface failures.** Consider adding invalid or unknown rental IDs, overlapping rental requests, and failures when saving a rental or return record.

## 6. Structural, wording, and presentation issues

1. **The Interfaces section is formatted as a short bullet list rather than complete interface specifications.** Use a consistent subsection for each function, with its full signature and the same contract headings.

2. **The document does not introduce its non-primitive types.** Add a short type-definition paragraph before the interface list, covering `DateTime`, `Customer`, `Rental`, `Payment`, and any status enumerations used.

3. **Several spelling and grammar errors reduce clarity.** Examples include “availibility,” “gaurantees,” “retal,” “renal,” “requies,” “unsucessful,” and “reted.” Correct these throughout.

4. **Terminology and capitalization are inconsistent.** The document alternates between forms such as `CustomerID`/`customerID`, `Date`/`DateTime`, and “status”/“Status.” Use one naming convention in each diagram and ensure the same concepts have matching names across sections.

5. **Some statements are too broad to be testable.** Phrases such as “correct payment,” “valid time,” and “correct rate” should be replaced with specific, verifiable rules.

6. **The document is explicitly partial, but it does not identify which sections or decisions remain incomplete.** Add a short list of open design questions, particularly around payment retries, rental scheduling, pricing, return inspection, and error handling.

## 7. Recommended priorities

1. Resolve the business rules for rental time periods, bike availability, and the meaning of rental end/return time.
2. Add rental and payment status to the data model and define their allowed values.
3. Correct the “every bike has exactly one renter” invariant and make all invariants testable.
4. Align the ER diagram, class diagram, and six interface contracts so names, types, fields, and behavior agree.
5. Specify error handling and payment-processor timeout/retry behavior.
6. Complete the interface contracts and define all non-primitive types before treating the design as implementation-ready.
