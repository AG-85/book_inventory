# terraform/outputs.tf
output "container_image" {
  value = "ghcr.io/${var.github_owner}/hello-world:latest"
  description = "The URL of the container image in GitHub Container Registry"
}