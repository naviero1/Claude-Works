# Topic: inventory replenishment (live demonstration)

## SOURCE (give this to the assistant)

Inventory replenishment is the process of reordering stock before it runs out.
A reorder point is the inventory level that triggers a new order; it is set by
multiplying expected daily demand by the supplier lead time in days, then adding
safety stock. Safety stock is extra inventory held to absorb demand spikes and
late deliveries; more variability in demand or lead time requires more safety
stock. Ordering too late causes stockouts and lost sales; ordering too early or
too much increases holding costs (storage, capital tied up, spoilage or
obsolescence risk). The reorder quantity is a separate decision from the reorder
point and is often set to balance ordering costs against holding costs. These
formulas assume demand history predicts future demand; a promotion, a new
customer, or a supply disruption can invalidate that assumption, so reorder
parameters should be reviewed periodically rather than set once.

## SAMPLE OUTPUT (what a good result looks like)

### The main idea
Reordering works best when you order **before** you run out — at a planned
stock level called the reorder point — not when the shelf is already empty.

### When to reorder
The reorder point is the stock level that tells you "order now." It has three
parts: how much you use each day, how many days a new order takes to arrive,
and a safety cushion on top. Example: if a bakery uses 10 bags of flour a day
and delivery takes 4 days, it needs to reorder no later than 40 bags — plus
that cushion, which the next section explains.

### The extra cushion
That extra is called **safety stock**: spare inventory that protects you when
you suddenly need more than usual, or when a delivery is late. The less
predictable your needs or your supplier, the bigger the cushion should be.

### The trade-off
Ordering too late means running out and losing sales. Ordering too much means
paying to store things — and some stock can spoil or go out of date. How MUCH
to order each time is a separate decision from WHEN to order.

An analogy: the reorder point is like your car's fuel light. It comes on early
enough to reach a gas station. But the analogy stops there — a fuel light is set
once by the carmaker, while a reorder point must be **reviewed regularly**,
because it relies on the past predicting the future. A promotion, a new
customer, or a supply problem can make yesterday's numbers wrong.

### Check yourself
1. What sets the reorder point? *(Daily use multiplied by delivery days, plus
   safety stock — all three parts, per the source formula.)*
2. What is safety stock for? *(Demand spikes and late deliveries.)*
3. Why review reorder points regularly? *(They assume the past predicts the
   future; promotions, new customers, or disruptions break that assumption.)*

### Fidelity note (part of the check)
Preserved: the point/quantity distinction, the variability rule, both failure
costs, and the review caveat. No fixed numbers were invented; the bakery example
illustrates the formula in the source.
