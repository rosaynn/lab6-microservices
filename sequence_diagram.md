# Sequence Diagram

> Якщо діаграма не відображається, відкрий її у Markdown Preview з розширенням Mermaid.
> Для VS Code рекомендується встановити `Markdown Preview Mermaid Support` або `Markdown Preview Enhanced`.
> Або вставити нижче у https://mermaid.live

```mermaid
sequenceDiagram
    participant Client
    participant ManagementService as Management Service
    participant AuditService as Audit Service

    Client->>ManagementService: POST /action { action_name }
    ManagementService->>AuditService: POST /audit/log { action: "Management action: ..." }
    AuditService-->>ManagementService: 200 OK { audit record }
    ManagementService-->>Client: 200 OK { action completed }

    Client->>ManagementService: GET /actions
    ManagementService-->>Client: 200 OK { actions list }

    Client->>AuditService: GET /audit/{id}
    AuditService-->>Client: 200 OK { audit record }
```
