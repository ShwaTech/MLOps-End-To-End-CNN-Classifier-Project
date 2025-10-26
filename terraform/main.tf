
module "iam_user_ci_cd" {
  source    = "./modules/iam"
  user_name = var.iam_user_name_ci_cd
}

module "ecr_repo" {
  source    = "./modules/ecr"
  repo_name = var.ecr_repo_name
}

data "aws_vpc" "default" {
  default = true
}

module "ec2_instance" {
  source        = "./modules/ec2"
  vpc_id        = data.aws_vpc.default.id
  instance_name = var.ec2_instance_name
  ami_id        = var.ec2_ami
  instance_type = var.ec2_instance_type
  key_name      = var.ec2_key_name
  disk_size     = var.ec2_disk_size
}
