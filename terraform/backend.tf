terraform {
  backend "s3" {
    bucket         = var.terraform_state_bucket
    key            = var.terraform_state_key
    region         = var.region
    dynamodb_table = var.terraform_lock_table
    encrypt        = var.terraform_state_encrypt
  }
}