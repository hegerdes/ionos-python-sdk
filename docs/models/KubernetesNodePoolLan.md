# KubernetesNodePoolLan

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **id** | **int** | The LAN ID of an existing LAN at the related datacenter |  |
| **dhcp** | **bool** | Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. | [optional]  |
| **routes** | [**list[KubernetesNodePoolLanRoutes]**](KubernetesNodePoolLanRoutes.md) | array of additional LANs attached to worker nodes | [optional]  |

