from distributed import Client,LocalCluster


if __name__ == "__main__":

    cluster = LocalCluster()         
    client = cluster.get_client()

    print(cluster.get_client)