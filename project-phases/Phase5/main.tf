# main.tf
provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "hivebox" {
  name     = "hivebox-cluster"
  role_arn = aws_iam_role.eks_cluster.arn
}