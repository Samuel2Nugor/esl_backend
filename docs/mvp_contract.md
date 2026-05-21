# MVP Contract

## Purpose

This document defines the minimum contract between:

- Frontend
- Backend API
- MQTT broker
- Gateway
- BLE tags

The goal is to keep the MVP focused and avoid adding extra features before the core flow is stable.

---

## MVP System Flow

```text
        ```
Frontend / API client
        ↓
Backend API
        ↓
MQTT broker
        ↓
Gateway
        ↓
BLE tag
        ↓
Gateway ACK
        ↓
Backend ACK listener
        ↓
Backend database

----

## Backend API Routes

### Health

```text
GET /health
```

---

### Commands

```text
POST   /commands
GET    /commands
GET    /commands/{command_id}
PATCH  /commands/{command_id}
DELETE /commands/{command_id}
```

Request:

```json
{
    "tagId": 1,
    "title": "Milk 1L",
    "finalPrice": 29.0
}
```

---

### Products

```text
POST   /products
GET    /products
GET    /products/{product_id}
PATCH  /products/{product_id}
DELETE /products/{product_id}
```

Request:

```json
{
    "sku":"MILK001",
    "name":"Milk 1L",
    "price":29.0
}
```

---

### Tags

```text
POST   /tags
GET    /tags
GET    /tags/{tag_id}
PATCH  /tags/{tag_id}
DELETE /tags/{tag_id}
```

Request:

```json
{
    "name":"TG_01",
    "ble_address":"74:4D:BD:63:C2:C6",
    "status":"available"
}
```

---

### Shelf Locations

```text
POST   /shelf-locations
GET    /shelf-locations
GET    /shelf-locations/{location_id}
PATCH  /shelf-locations/{location_id}
DELETE /shelf-locations/{location_id}
```

Request:

```json
{
    "name":"Dairy A1",
    "description":"Milk shelf"
}
```

---

### Assignments

```text
POST   /assignments
GET    /assignments
GET    /assignments/{assignment_id}
PATCH  /assignments/{assignment_id}
DELETE /assignments/{assignment_id}
```

Request:

```json
{
    "product_id":1,
    "tag_id":1,
    "shelf_location_id":1
}
```

---

## MQTT Topics

Backend → Gateway

```text
esl/tag/write
```

Gateway → Backend

```text
esl/tag/ack
```

Command payload:

```json
{
    "commandId":1,
    "tagId":1,
    "title":"Milk 1L",
    "finalPrice":29.0
}
```

ACK:

```json
{
    "commandId":1,
    "tagId":1,
    "ack":"true"
}
```

Failure ACK:

```json
{
    "commandId":1,
    "tagId":1,
    "ack":"false",
    "reason":"tag_not_found"
}
```

---

## MVP Boundaries

Included:

- commands
- products
- tags
- shelf locations
- assignments
- MQTT
- SQLite
- ACK handling

Not included:

- authentication
- WebSockets
- PostgreSQL
- promotions
- campaigns
- stores
- multi-gateway

----

## Important Design Decisions

- The backend owns logical tag identity.

- The gateway owns BLE delivery details.

- The backend should not need to know the BLE address in the MVP.

- The gateway handles BLE retry attempts.

- The backend handles command history and ACK status tracking.

- The command monitor handles missing ACK timeout cases only.
