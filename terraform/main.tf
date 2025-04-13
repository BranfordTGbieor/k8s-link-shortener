provider "aws" {
  region = var.region
}

data "aws_availability_zones" "available" {
  state = "available"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = var.vpc_name
  cidr = var.vpc_cidr

  azs             = slice(data.aws_availability_zones.available.names, 0, 2)
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets

  enable_nat_gateway   = var.enable_nat_gateway
  single_nat_gateway   = var.single_nat_gateway
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.3"

  cluster_name    = var.cluster_name
  cluster_version = var.eks_version

  vpc_id                         = module.vpc.vpc_id
  subnet_ids                     = module.vpc.private_subnets
  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    default = {
      min_size     = var.min_nodes
      max_size     = var.max_nodes
      desired_size = var.desired_nodes

      instance_types = [var.instance_type]
      capacity_type  = "ON_DEMAND"

      # Add IAM permissions for CNI plugin
      iam_role_additional_policies = {
        AmazonEKS_CNI_Policy = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
      }

      # Configure max pods per node
      max_pods = 17  # t2.micro has limited IP addresses

      # Configure kubelet parameters
      kubelet_extra_args = "--max-pods=17"
    }
  }

  # Add security group rules
  node_security_group_additional_rules = {
    egress_all = {
      description = "Allow all egress traffic"
      protocol    = "-1"
      from_port   = 0
      to_port     = 0
      type        = "egress"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  # Add lifecycle rule to ignore duplicate security group rules
  node_security_group_tags = {
    "kubernetes.io/cluster/${var.cluster_name}" = "owned"
  }
}

# Update kubeconfig after cluster creation
resource "null_resource" "update_kubeconfig" {
  depends_on = [module.eks]

  provisioner "local-exec" {
    command = "aws eks update-kubeconfig --name ${var.cluster_name} --region ${var.region}"
  }
} 