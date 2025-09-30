from diagrams import Cluster, Diagram
from diagrams.onprem.client import User
from diagrams.onprem.network import Nginx
from diagrams.k8s.infra import ETCD, Node
from diagrams.k8s.controlplane import API

with Diagram(
    "Vagrant Kubernetes Cluster",
    filename="vagrant_k8s_diagram",
    show=False,
    outformat="png",
    direction="TB",
    graph_attr={"dpi": "600"}
):
    user = User("local user")

    with Cluster("Virtual Box"):
        # Control plane + etcd nodes
        control_plane_nodes = []
        etcd_nodes = []
        for i, ip in enumerate(["192.168.56.10", "192.168.56.11", "192.168.56.12"]):
            with Cluster(f"hostname: server_{i}\nip: {ip}\nssh: 2001{i}"):
                api = API("port: 16443" if i == 0 else "")
                etcd = ETCD("")
                control_plane_nodes.append(api)
                etcd_nodes.append(etcd)

        # Worker nodes
        workers = []
        for i, ip in enumerate(["192.168.56.20", "192.168.56.21", "192.168.56.22"]):
            with Cluster(f"hostname: worker_{i}\nip: {ip}\nssh: 2002{i}"):
                worker = Node("")
                if i == 0:
                    with Cluster("pod"):
                        nginx = Nginx("port: 30080")
                        user >> nginx
                workers.append(worker)

    # User access to API
    user >> control_plane_nodes[0]

    # Connect control plane to workers
    for api, worker in zip(control_plane_nodes, workers):
        api >> worker

    # Connect etcd <-> control plane
    for api, etcd in zip(control_plane_nodes, etcd_nodes):
        api >> etcd
        etcd >> api
