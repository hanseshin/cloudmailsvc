variable "slack_webhook_url" {
  description = "Slack Webhook URL"
  type        = string
  default     = "https://hooks.slack.com/services/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"
}

variable "vmware_api_url" {
  description = "VMware Webhook API URL"
  type        = string
  default     = "http://125.179.40.152:5000/webhook/restore"
}

variable "route53_healthcheck_id" {
  description = "Route53 HealthCheck ID"
  type        = string
  default     = "2fa3b506-4146-4b78-8bd4-4a5421aa8db9"
}
