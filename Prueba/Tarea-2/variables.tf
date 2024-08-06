variable "aws_region" {
  description = "Region de AWS donde se desplegaran las inctancias"
  default     = "us-east-1"
}

variable "instance_type_linux" {
  description = "Tipo de instancia"
  default     = "t2.micro"
}

variable "instance_type_windows" {
  description = "Tipo de instancia"
  default     = "t2.micro"
}

variable "linux_ami" {
  description = "ID de la AMI para utilizar en la instancia de linux"
  default     = "ami-0c55b159cbfafe1f0"
}

variable "windows_ami" {
  description = "ID de la AMI para utilizar en la instancia de windows"
  default     = "ami-0c2b8ca1dad447f8a" 
}

variable "allowed_cidr" {
  default = "172.0.1.0/24"  
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  default     = "172.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  default     = "172.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "CIDR block for the private subnet"
  default     = "172.0.2.0/24"
}

variable "key_name" {
  description = "llave para ingresar por SSM y SSH a las instancias"
  type        = string
}

# variable "access_key" {
#   description = "Llave de acceso a AWS"
#   type        = string
# }

# variable "secret_key" {
#   description = "Secreto de acceso a AWS"
#   type        = string
# }