# Topic: how an internet message travels (self-study variation)

## SOURCE (give this to the assistant)

When a message is sent over the internet, it is first divided into packets —
small blocks of data, each carrying the destination address and a sequence
number. Routers pass each packet toward its destination hop by hop, choosing a
next step from routing tables; packets from the same message may take different
paths and arrive out of order. The receiving device uses the sequence numbers to
reassemble the message and requests retransmission of any packet that was lost.
This design, packet switching, lets many conversations share the same lines
efficiently and routes around failures, but it does not guarantee a fixed path
or arrival time; delays vary with congestion. Protocols such as TCP provide the
checking and reordering that make delivery reliable on top of this best-effort
network.

## SAMPLE OUTPUT (what a good result looks like)

### The main idea
The internet does not send your message in one piece. It cuts the message into
small pieces, sends each piece separately, and puts them back together at the
other end.

### The journey
Each piece is called a **packet** — a small block of data with the delivery
address and its place in line written on it. Machines called **routers** pass
each packet along, one hop at a time, each choosing the next step. Pieces of
the same message can travel different roads and arrive in the wrong order. The
receiving device uses the numbers to put them back in order — and asks for a
new copy of any piece that got lost.

### Why do it this way
Sharing the lines packet by packet lets millions of conversations use the same
wires, and traffic can steer around broken links. The cost: no piece is
promised a fixed road or arrival time — busy moments mean delays. A set of
rules called **TCP** does the checking and re-ordering that makes delivery
dependable anyway.

An analogy: it is like mailing a long letter as many postcards, each numbered,
possibly traveling by different routes. The analogy stops here: the post office
never notices a lost postcard, but the internet's rules detect a missing packet
and automatically ask the sender for it again.

### Check yourself
1. What two things are written on every packet? *(The destination address and
   its sequence number.)*
2. Why can pieces arrive out of order? *(They may take different paths.)*
3. What happens when a piece is lost? *(The receiver requests it again.)*

### Fidelity note (part of the check)
Preserved: best-effort delivery, variable delay under congestion, and TCP as
the reliability layer. Nothing promises speed or a fixed route — the source's
"no guarantee" condition survives in "no piece is promised a fixed road."
