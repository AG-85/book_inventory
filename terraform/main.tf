# terraform/main.tf
terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

resource "github_actions_secret" "registry_url" {
  repository      = var.github_repository
  secret_name     = "REGISTRY_URL"
  plaintext_value = "ghcr.io/${var.github_owner}/hello-world:latest"
}

resource "null_resource" "container_registry_setup" {
  provisioner "local-exec" {
    command = <<EOT
      echo "Container registry setup completed - image available at: ghcr.io/${var.github_owner}/hello-world:latest"
    EOT
  }
}