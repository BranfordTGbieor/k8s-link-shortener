terraform {
  backend "s3" {
    bucket         = "k8s-url-shortener-terraform-state"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "k8s-url-shortener-terraform-locks"
    encrypt        = true
  }
} 