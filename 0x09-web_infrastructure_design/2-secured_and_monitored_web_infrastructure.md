# Simple Web Stack

<img src="2-secured_and_monitored_web_infrastructure.png">

<center>| <a href="">Visit the board</a> |</center>


## Explaining specifics about this infrastructure

+ Purpose of firewalls: <br>
It protects the network (web servers, anyway) from unwanted and unauthorized users by acting as an intermediary between the internal network and the external network and blocking the incoming traffic.

+ Purpose of SSL Certificate: <br>
The SSL certificate is for encrypting the traffic between the web servers and the external network to prevent man-in-the-middle attacks (MITM) and network sniffers from sniffing the traffic which could expose valuable information. The SSL certificate ensure privacy, integrity, and identification.

+ Purpuse of Monitoring Clients: <br>
They monitor the servers and the external network. They analyse the performance and operations of the servers, measure the overall health, and alert the administrators if the servers are not performing as expected.

## Issues With This Infrastructure

+ Terminating SSL at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted.

+ Having one MySQL server is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.

+ Having servers with all the same components would make the components contend for resources on the server like CPU, Memory, I/O, etc., which can lead to poor performance.
