# MVP Contract

## Purpose

This document defines the minimum contract between the backend, MQTT broker, gateway, and BLE tag.

The goal is to keep the MVP focused and avoid adding extra features before the core flow is stable.

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

## MQTT Topics

### Backend to Gateway

- esl/tag/write

Used when the backen sends a command to update a tag

### Gateway to Backend Architecture

- esl/tag/ack

Used when the gateway reports whether the tag update succeeded or failed


## Command Payload

```json
       ```
{
  "commandId": 1,
  "tagId": 1,
  "title": "Milk 1L",
  "finalPrice": 29.00
}

### Fields

commandId   Backend command identifier
tagId       Logical tag identifier
title       Product/title text displayed on tag
finalPrice  Price displayed on tag

## ACK Payload 

### Success

```json
       ```
{
  "commandId": 1,
  "tagId": 1,
  "ack": "true"
}

### Failure

```json
       ```
{
  "commandId": 1,
  "tagId": 1,
  "ack": "false",
  "reason": "tag_not_found"
}


## Backend API MVP

GET    /health

POST   /commands
GET    /commands
GET    /commands/{command_id}
PATCH  /commands/{command_id}
DELETE /commands/{command_id}

GET    /tags
GET    /tags/{tag_id}

## Command Lifecycle

created
↓
published
↓
ack_received

or

published
↓
failed

or

archived


## MVP Boundaries

- command creation
- command listing
- command lookup
- command status update
- command archiving
- tag listing
- tag lookup
- MQTT publish
- ACK handling
- SQLite persistence

#### Not include yet

- WebSockets
- authentication
- PostgreSQL
- ORM
- Alembic
- multi-gateway support
- advanced retry automation
- live dashboard updates


## Important Design Decisions

- The backend owns logical tag identity.

- The gateway owns BLE delivery details.

- The backend should not need to know the BLE address in the MVP.

- The gateway handles BLE retry attempts.

- The backend handles command history and ACK status tracking.

- The command monitor handles missing ACK timeout cases only.
