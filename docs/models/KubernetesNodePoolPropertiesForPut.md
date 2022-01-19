# KubernetesNodePoolPropertiesForPut

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** | A Kubernetes node pool name. Valid Kubernetes node pool name must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. | [optional]  |
| **node_count** | **int** | The number of nodes that make up the node pool. |  |
| **k8s_version** | **str** | The Kubernetes version the nodepool is running. This imposes restrictions on what Kubernetes versions can be run in a cluster&#39;s nodepools. Additionally, not all Kubernetes versions are viable upgrade targets for all prior versions. | [optional]  |
| **maintenance_window** | [**KubernetesMaintenanceWindow**](KubernetesMaintenanceWindow.md) |  | [optional]  |
| **auto_scaling** | [**KubernetesAutoScaling**](KubernetesAutoScaling.md) |  | [optional]  |
| **lans** | [**list[KubernetesNodePoolLan]**](KubernetesNodePoolLan.md) | array of additional LANs attached to worker nodes | [optional]  |
| **labels** | **dict(str, str)** | map of labels attached to node pool. | [optional]  |
| **annotations** | **dict(str, str)** | map of annotations attached to node pool. | [optional]  |
| **public_ips** | **list[str]** | Optional array of reserved public IP addresses to be used by the nodes. IPs must be from same location as the data center used for the node pool. The array must contain one extra IP than maximum number of nodes could be. (nodeCount+1 if fixed node amount or maxNodeCount+1 if auto scaling is used) The extra provided IP Will be used during rebuilding of nodes. | [optional]  |

