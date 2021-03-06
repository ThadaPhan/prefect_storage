from prefect.run_configs import LocalRun, KubernetesRun, RunConfig
from prefect.storage.github import GitHub
from prefect.client.secrets import Secret


def set_run_config(local: bool = False) -> RunConfig:
    if local:
        return LocalRun(labels=["dev"])
    aws_account_id = Secret("AWS_ACCOUNT_ID").get()
    return KubernetesRun(
        labels=["prod"],
        image=f"{aws_account_id}.dkr.ecr.sa-east-1.amazonaws.com/docker:latest",
        image_pull_policy="IfNotPresent",
    )


def set_storage(flow_name: str) -> GitHub:
    return GitHub(
        repo="ThadaPhan/prefect_storage",
        path=f"flows/{flow_name}.py",
        access_token_secret="GITHUB_ACCESS_TOKEN",
    )
