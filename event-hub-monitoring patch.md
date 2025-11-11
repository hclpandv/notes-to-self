## In the main.tf

add below code in each `azurerm_monitor_diagnostic_setting` resource

```hcl
eventhub_authorization_rule_id  = var.monitoring_eventhub_authorization_rule_id != null ? var.monitoring_eventhub_authorization_rule_id : null
eventhub_name                   = var.monitoring_eventhub_name != null ? var.monitoring_eventhub_name : null
```

## In the variables.tf

```hcl
variable "monitoring_eventhub_authorization_rule_id" {
  description = "Event Hub authorization rule ID for diagnostic settings (if null, Event Hub logging is disabled)"
  type        = string
  default     = null
}

variable "monitoring_eventhub_name" {
  description = "Event Hub name for diagnostic settings (if null, Event Hub logging is disabled)"
  type        = string
  default     = null
}
```
