# terraform/variables.tf
variable "github_token" {
  description = "GitHub token for API access"
  type        = string
  sensitive   = true
}

variable "github_owner" {
  description = "GitHub repository owner/organization"
  type        = string
}

variable "github_repository" {
  description = "GitHub repository name"
  type        = string
}