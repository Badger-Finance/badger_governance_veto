from brownie import accounts, TimelockController


def main(deployer_label=None):
    # initially all roles are given to the dev_msig
    dev_msig = "0xB65cef03b9B89f99517643226d76e286ee999e77"

    deployer = accounts.load(deployer_label)

    min_delay = 172800  # 2 days in seconds

    TimelockController.deploy(
        min_delay,
        [dev_msig],  # proposers
        [dev_msig],  # executors
        [dev_msig],  # vetoers
        [dev_msig],  # supremecourt
        [dev_msig],  # cancellors
        {"from": deployer},
        publish_source=True,
    )
