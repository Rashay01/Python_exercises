# HTTP 3

### What was the problem with HTTP2?

In HTTP2 the major flaw was the TCP head of line blocking. This was due to HTTP2's reliance of the TCP protocol. Head-of-Line blocking occurs when a line or series of packets are held up in a queue by a first packet. Head of Line blocking occurred in HTTP2 when one single packet was lost/slow in transit, it blocked the delivery of all the further (subsequent) packets that followed in that single transmission connection. Network congestion generally causes packet loss.

### How HTTP3 addressed this issue
HTTP3 was able to fix this major flaw by introducing (QUIC) Quick UDP Internet Connections which is a transfer protocol. This protocol is known for features that improve performance, reduces latency, enhances security, and handles network fluctuations better compared to HTTP2. This allowed the packets to be sent without being worried about ordered constraints accompanied by TCP. This allowed http3 to perform better with packet loss and network congestion due to the reliance on UDP. UDP operates faster than TCP. UDP does not require the 3 way handshake to set up the communication channels.

HTTP3 utilized forward error correction and faster retransmission to achieve this improved packet loss recovery which in turn helps to improve the efficiency in recovering from packet loss compared to HTTP2. Forward error transmission is a method to recover lost packets by sending an extra parity packet for every four packets.

### What was fixed in HTTP3
- HTTP3 supports connection migration which allowed seamless switching between network paths in case of disruptions. This helped to fix the network errors that users experienced in HTTP2.

- HTTP3 has built in QUIC packet headers which removed the need to compress headers which occurred in HTTP2. HTTP2 used HPACK compression.

HTTP3 is designed to improve performance and reduced latency compared to HTTP1 and HTTP2. It improves on its security, speed, and reliability.
