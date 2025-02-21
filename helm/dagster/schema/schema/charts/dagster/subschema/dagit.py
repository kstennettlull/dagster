from typing import Dict, List, Optional

from pydantic import Extra  # pylint: disable=no-name-in-module

from ...utils import kubernetes
from ...utils.utils import BaseModel


class Server(BaseModel):
    host: str
    port: int
    name: Optional[str]


class Workspace(BaseModel):
    enabled: bool
    servers: List[Server]


class Dagit(BaseModel):
    replicaCount: int
    image: kubernetes.Image
    service: kubernetes.Service
    workspace: Workspace
    env: Dict[str, str]
    envConfigMaps: List[kubernetes.ConfigMapEnvSource]
    envSecrets: List[kubernetes.SecretEnvSource]
    deploymentLabels: Dict[str, str]
    labels: Dict[str, str]
    nodeSelector: kubernetes.NodeSelector
    affinity: kubernetes.Affinity
    tolerations: kubernetes.Tolerations
    podSecurityContext: kubernetes.PodSecurityContext
    securityContext: kubernetes.SecurityContext
    resources: kubernetes.Resources
    readinessProbe: kubernetes.ReadinessProbe
    livenessProbe: kubernetes.LivenessProbe
    startupProbe: kubernetes.StartupProbe
    annotations: kubernetes.Annotations
    enableReadOnly: bool
    dbStatementTimeout: Optional[int]

    class Config:
        extra = Extra.forbid
