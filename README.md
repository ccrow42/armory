# Portworx Armory Demo

This repository is designed to be cloned per environment. We are working to automate the setup steps.

## Prerequites

Ensure that you have the following utilities installed and up to date:
- eksctl
- aws - should have access to create clusters
- armory - should be logged in
- kubectl
- storkctl
- pxctl (best to use an alias for this one)

Details for utility installation coming soon.

It is important for the installation of portworx that the IAM role assigned to the EKS cluster has permissions to add disks. Details on creating an IAM policy can be found here: https://docs.portworx.com/portworx-enterprise/install-portworx/kubernetes/aws/aws-eks

Note that I have already created this policy and assigned it to the cluster using the eksctl file

## Manual Setup

Deploy EKS clusters:

'eksctl create cluster --kubeconfig ~/git/newstack/labv2/esk01 -f uswest2-eks01-prod.yaml'

'eksctl create cluster --kubeconfig ~/git/newstack/labv2/esk02 -f uswest2-eks02-stage.yaml'

Install the Armory Agents

NOTE: in order to avoid modifying config files, it is important that agents are install within tenants. There is a demo1 and demo2 tenant environment in armory. The source (prod) cluster is called cluster01 and the destination (stage) cluster is called cluster02

