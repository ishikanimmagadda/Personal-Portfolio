Deployment Documentation

How do two computers communicate data with each other wirelessly? 
    Wifi
      - each computer has its own ip address and both computers are connected to the same wifi router --> data is transmitted with TCP protocols over network 
    Bluetooth 
      - One computer needs to be discoverable, data transmitted directly between devices through Bluetooth 
    Cellular 
      - carrier assigns a IP to each device, data transmits over cellular network 
    Adhoc Network 
      - one computer creates the adhoc network, the other joins it 

Seven Layers of Open Systems Interconnection Network Stack 

Physical Layer: transmitting bitstreams of data from one computer to another 
DataLink Layer: packs bitstreams into collection of frames 
Network Layer: frames are packaged into IP packets, that IP determines the destination of computer, which recieves the data 
Transport Layer: streaming data from one location to another location, TCP: Transmission Control Protocol
Session Layer: Manages connections between applications 
Presentation Layer: Structred way of representing information thats going through the sessions 
Application Layer: network services to end user 

Ip Address: unique ID assigned to each device connected to network. Internet Protocol Address, IPv4: 32 bits, IPv6: 128 bits. Computer uses IP address to connect to websites. a

Port: Allow multiple communication sessions to occur simultaneously on a single device. 
    - When a device sends data over the network, the transport layer protocol (TCP/UDP) attaches the source and destination port numbers to the data packet.
    - The receiving device uses the port number to forward the packet to the correct application or service.
    - Together, an IP address and a port number form a socket, which uniquely identifies a network connection endpoint.

EC2: virtual server in AWS Cloud 

SSH: Secure Shell, provides a secure way to access a remote computer over an unsecured network.
    - It enables secure communication between two networked devices by encrypting the data transmitted between them.

    - Connecting to a Remote Server: ssh username@hostname

SCP: Secure Copy Protocol, network protocol used for securely transferring files between a local machine and a remote servers, encrypted 

    - Copying Files to a Remote Server (SCP): scp localfile username@hostname:/path/to/remote/file
    - Copying Files from a Remote Server (SCP): scp username@hostname:/path/to/remote/file localfile





