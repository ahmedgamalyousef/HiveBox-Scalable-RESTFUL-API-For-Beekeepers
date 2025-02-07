# Terraform Configuration
provider "aws" {
  region = "us-west-2"
}

module "dev" {
  source = "./modules/k8s-cluster"
  environment = "dev"
}

module "stage" {
  source = "./modules/k8s-cluster"
  environment = "stage"
}

module "prod" {
  source = "./modules/k8s-cluster"
  environment = "prod"
}
