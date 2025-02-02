provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "hivebox-scalable-restful-api-for-beekeepers_cluster" {
  ...
}
