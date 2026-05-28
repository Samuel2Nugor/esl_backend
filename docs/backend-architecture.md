# Backend Architecture

The backend is responsible for application logic, validation and system coordination. It acts as the central decision-making
between the client interface, database, MQTT broker, and gateway.

The backend receives API requests from a frontend or another client, validates incoming payloads, applies business rules, and stores required
information for persistence and tracking. After processing the request, the backend publishes commands to the MQTT broker so the gateway
can deliver updates to the physical ESL tag through BLE communication.

The backend is also responsible for maintaining the desired system state. It should know what data is expected to be displayed on a tag,
whether a command was sent successfully, and later whether an acknowlodgement(ACK) was received from the gateway.

The business logic layer should remain separated from transport and infrstructure layers. MQTT is responsible only for transport, while
the backend logic decides what actions should happen and why.

### Why this matters

Separation responsiblities makes the system easier to understand, debug, test and scale.

A clear backend architecture helps prevent tight coupling between components such as the API, database, MQTT communication, and gateway logic.
Each component should focus on its own responsibilty:

- The backend owns business rules and desired state.
- The gateway owns BLE communication and delivery reliability.
- The tag owns displaying data and sending acknowledments.

----

## Purpose

The purpose of the backend architecture design is to define clear system responsabilties, data flow, and components boundaries before adding
more features to the system.

This design helps mantain a structured and understandable backend while preventing unnecessary complexity and overengineering
during early development stages.

The architecture is intended to evolve over time as the system grows and requirements become clearer. Even trough the design
may change later, having an initail structure helps visualize the system flow, improve ownership understanding,
and guide future implementation decisions.

A documented architecture also make debugging, testing, refractoring, and scaling easier beacuse each component has a more defined responsibility.

----

## Current scope

The current bakend scope focues on building a minimal but structured backend architecture that can coordinate request, validate
data, store state, and communicate with the gateway through MQTT.

### Business logic responsibilities

The buisiness logic layer should be able to:

- handle CRUD( Create, Read, Update and Delete) operations for payloads and tags
- validate incoming requests and payload data
- schedule or roganize future payload deliveries
- maintain awareness of the current system state
- received acknowledgement results from the gateway
- determine whether a delivery was succesful or failed 
- provide logging and traceability for easier debugging and monitoring

### Database responsiblities

The database layer should be able to:

- store every request received from frontend client or APIs
- store payload and tag information
- store delivery states and acknowledgment results
- persist system state between restarts or crashes
- provide historical tracking for debugging and future analysis

### MQTT communication responsiblities

The MQTT layer should be able to:

- publish commands to the broker
- receive acknowledgment from the gateway
- separate transport communication from business logic responsiblities

### Why this matters

Defining the current scope prevents the backend from becoming too large too early.

At this stage, the backend should focus on creating payloads, validating data, storing system state, publishing commands to
MQTT, and receiving delivery results from the gateway.

This mathers because the gateway already owns the BLE delivery, retries, offline handling, and ACK timeouts. Keeping those reponsabilities
on the gateway side prevents the backend from being tight coupled to BLE details.

A clear current scope makes the backend easier to build, test, and extend later without mising application logic with device communication logic.


----

## Future scope

- Promotions and campaign management
- Authentication and authorization( admin mode and user roles)
- Security layer for encrypted communications between the frontend, backend and gateway
- Maintain a registry of known ESL tags and their assigned products



## Components

## Design decisions
