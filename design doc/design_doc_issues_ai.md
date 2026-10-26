# Design Document Issues Report

## Scope of this review

This review focuses on logical, structural, and clarity issues in the current partial design document. Since this is explicitly **Part 1**, missing detail is not automatically treated as a defect; the points below identify ambiguities, inconsistencies, and decisions that may need clarification in later sections.

## 1. Logical and requirements issues

### Overview

- The overview says users can "update and maintain" the bike catalog and availability. It is unclear whether **customers** can edit inventory or whether this is a staff-only capability. The goals suggest inventory management belongs to employees or management.
- The overview should distinguish customer-facing activities (browse bikes, check availability, reserve, pay) from staff-facing activities (manage inventory, schedule maintenance, report problems).
- The spelling and wording need editing, including "retal buissness," "catologue," "availibility," and "maintance." These do not change the design, but they reduce professionalism and can make requirements harder to interpret.

### Actors

- "Users" is broad and may overlap with employees and management. Consider defining whether "users" means customers, or use explicit actor names such as **Customer**, **Employee**, and **Manager**.
- The third-party payment platform is an external system rather than a human actor. It can still appear in an actor/external-system list, but labeling the section **Actors and External Systems** would be clearer.
- The email service appears in the component diagram but is missing from the actors/external-systems list. If it is an external dependency, it should be listed or explained in a later section.
- The diagram does not show what employees and management are allowed to do differently. Role permissions may need to be specified later.

### Goals and non-goals

- "Email confirm" is vague. A clearer goal would be "send customers an email confirmation after a successful reservation."
- "Update orders" is ambiguous: it could mean customers changing or canceling their reservations, or staff modifying orders. Define which actions and roles are intended.
- "Investigate different bike options" is unclear phrasing. "Browse bike types and details" would better describe the customer goal.
- "Manage bike inventory" is broad. Later requirements should clarify whether this includes adding, editing, retiring, or marking bikes unavailable.
- The non-goals appropriately limit the scope, but "other equipment rentals" could be more precise (for example, helmets or accessories) if those items are likely to cause confusion.
- The goals mention paying for rentals, but do not specify whether payment occurs when booking, at pickup, or after the rental. This is an important workflow decision to resolve.

### Constraints

- "The application must work on mobile" is not very testable. Clarify whether this means a responsive website in mobile browsers, a native mobile app, or both. The React constraint alone does not settle that question.
- The $10,000 budget and end-of-term deadline are useful project constraints, but the document should eventually identify the currency and the exact deadline or milestone.
- Requiring a third-party payment platform is clear at a high level, but the chosen provider and its supported payment flow are not identified. That can remain undecided in a partial document if it is recorded as an open decision.
- The document does not identify any constraints for hosting, programming language on the backend, or database technology. These are not necessarily missing requirements at this stage, but should be considered if the project has restrictions in those areas.

### Assumptions

- "The server must support multiple users" is phrased as a requirement, not an assumption. It would fit better as a system requirement, potentially connected to the concurrent-user target.
- "The user can navigate a normal site" is subjective. Consider stating an assumption about basic web-browser familiarity, while ensuring the interface still has usable and accessible navigation.
- "APIs are maintained" is vague. Specify which external APIs this refers to and whether the team assumes the providers will maintain availability and backward compatibility.
- "No private data is stored" conflicts with likely system behavior. Accounts and reservations may require names, email addresses, contact details, and booking information; the payment provider may also return transaction identifiers or payment status. Clarify what data the application stores and what the payment provider stores.
- "Users have internet" is a reasonable assumption for an online rental website, but it means offline use is outside the expected operating environment. This should be understood as an assumption, not a guarantee.

### Non-functional requirements

- **Uptime greater than 90% is low for a customer-facing rental service.** At 90% uptime, downtime could exceed 72 hours in a 30-day month. Confirm whether this target is intentional. Define how uptime is measured and over what period.
- "The server can have at least 100 concurrent users" is understandable but imprecise. Define whether 100 users must be actively making requests at once, and under what workload or response-time target.
- "The average time to checkout is less than 5 mins" measures user behavior as much as system quality. Define the start and end points, and whether the target applies to a representative usability test or to all/some percentage of sessions.
- "Creating an account takes 2 mins or less" also needs a measurement method and test conditions. It may be better framed as a usability target for a first-time user.
- "Reservations must be able to be made 1 yr in advance" is a functional/business rule more than a conventional non-functional requirement. Move it to the functional requirements or rental rules section, while retaining it here if the assignment expects all quality-related constraints in one list.
- The performance requirements do not specify a response time for key actions such as checking availability or loading the bike catalog.
- No accessibility, security, backup/recovery, or privacy target is listed. These may be added in a later iteration if they are in scope; their absence is not necessarily a defect in this partial draft.

## 2. Component diagram issues

- The diagram uses `flowchart TD`, which is a Mermaid flowchart rather than Mermaid's dedicated `C4Component` or UML component notation. It is still a reasonable simple component-style diagram, but the document should be consistent with what the assignment means by "component diagram."
- The arrows from the actors to the React website and from the website to the backend are clear at a high level.
- The backend is shown calling Inventory, Rental Management, and Maintenance Management, but the diagram does not show whether those components communicate with one another. For example, rental availability may need to account for maintenance status.
- The diagram shows Inventory, Rentals, and Maintenance connected to the database, but does not show the Backend API's relationship to the database. This may be intentional if the feature components access it through the backend, but the architecture should make the access pattern clear and avoid implying direct database access from the browser.
- The payment platform is shown as an external component, but the diagram only shows Rentals connecting to it. Consider indicating that payment status/results return to the rental workflow, since a booking may need to be confirmed only after payment succeeds.
- The email flow is split into "Email Notifications" and "Email Service." This separation can make sense if the first component prepares notification content and the second is an external provider, but their responsibilities and boundary should be stated clearly.
- The email service is not identified as an external system in the actor list.
- The diagram does not show authentication or authorization. Those components may be unnecessary for a very simple draft, but accounts and distinct customer/employee/management permissions may require them in a later design.
- The diagram does not show how the database is hosted or whether it is a managed external service. This can remain unspecified until infrastructure choices are made.
- The component names are mostly consistent between the diagram and table. However, the table describes Email Notifications as generating messages, while the diagram does not define exactly where that message-generation responsibility sits.

## 3. Component table issues

- The table is valid Markdown and gives each listed component a short description.
- The descriptions are understandable but broad. Later versions could identify each component's main responsibility and avoid overlap.
- The table lists the Third-Party Payment Platform and Email Service as components alongside internal application components. This is acceptable, but consider labeling them as **external systems** so the system boundary is clear.
- The table does not list the human actors (Users, Employees, Management), which is fine if it is intended to document software components only. Keep actors in a separate section/table.

## 4. Structural and presentation issues

- The section headings are readable, but a consistent Markdown heading structure would be easier to maintain (for example, `# Design Document — Part 1`, followed by `## Overview`, `## Actors`, and so on).
- The document uses a mix of bold labels and indented asterisk lists. Standard Markdown headings and `-` bullet lists would be more consistent.
- The phrase "Goals/nogoals" could be renamed **Goals and Non-Goals**.
- Consider adding an **Open Questions** section for unresolved decisions rather than forcing every decision into the current partial draft.
- The design document should distinguish confirmed requirements from assumptions and tentative design choices. For example, React is a stated constraint, while the exact backend, database, and email provider are not yet specified.
- The document should consistently use terms such as "reservation," "rental," and "order." If these mean different things, define them; otherwise, choose one term where possible.

## 5. Suggested open questions for a later revision

1. Can customers make reservations without creating an account, or is an account required?
2. When is payment collected: at booking, at pickup, or at another point?
3. What happens if payment fails or the payment provider is temporarily unavailable?
4. Can customers modify or cancel reservations? If so, what are the rules?
5. How is bike availability calculated for a requested date range, including bikes under maintenance?
6. Which roles can add, edit, or remove bikes and manage reservations?
7. What customer and transaction data is stored by the application, and for how long?
8. Which email provider will be used, and what should happen if a confirmation email fails to send?
9. What exact uptime, performance, and load-test criteria will be used to verify the non-functional requirements?
10. Does "mobile support" mean a responsive website, and which browsers/devices must be supported?

## Overall assessment

The draft establishes a useful initial scope, identifies the main actors and project constraints, and includes a simple component diagram and component table. The most important issues to clarify are the contradiction around private data, the distinction between assumptions and requirements, the low and underspecified uptime target, the definition of mobile support, and the rental/payment/availability workflow. These are appropriate issues to track in a partial design document; they do not mean the entire document needs to be completed before the next design step.
