variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "aws_availability_zone" {
  description = "AWS availability zone"
  type        = string
  default     = "us-east-1a"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0069aa073aac75299" # Latest Ubuntu 20.04 LTS in us-east-1
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.medium"
}

variable "key_name" {
  description = "Name of the SSH key pair"
  type        = string
  default     = "k8s-url-shortener"
}

# Backend configuration variables
variable "terraform_state_bucket" {
  description = "S3 bucket for Terraform state"
  type        = string
  default     = "k8s-url-shortener-terraform-state"
}

variable "terraform_state_key" {
  description = "Key for Terraform state file in S3"
  type        = string
  default     = "terraform.tfstate"
}

variable "terraform_lock_table" {
  description = "DynamoDB table for Terraform state locking"
  type        = string
  default     = "k8s-url-shortener-terraform-locks"
}

variable "terraform_state_encrypt" {
  description = "Whether to encrypt the Terraform state"
  type        = bool
  default     = true
} 