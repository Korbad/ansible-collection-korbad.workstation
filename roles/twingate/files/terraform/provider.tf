terraform {
  cloud {
    organization = "korbad-test"

    workspaces {
      name = "test"
    }
  }
  required_providers {
    twingate = {
      source = "Twingate/twingate"
      version = "1.0.0"
    }
  }
}

provider "twingate" {
  api_token = var.twingate_token
  network   = "korbad"
}