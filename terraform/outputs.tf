
# To Show It => Run $ terraform output iam_user_access_key_ci_cd
output "iam_user_access_key_ci_cd" {
  value     = module.iam_user_ci_cd.iam_access_key_ci_cd
  sensitive = true
}

# To Show It => Run $ terraform output iam_user_secret_key_ci_cd
output "iam_user_secret_key_ci_cd" {
  value     = module.iam_user_ci_cd.iam_secret_key_ci_cd
  sensitive = true
}

output "ecr_repo_uri" {
  value = module.ecr_repo.repository_uri
}

output "ec2_public_ip" {
  value = module.ec2_instance.instance_public_ip
}

output "ec2_public_dns" {
  value = module.ec2_instance.instance_public_dns
}

