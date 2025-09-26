Vagrant.configure("2") do |config|
    # Servers
    config.vm.define "server_0" do |app|
      app.vm.box = "bento/debian-12"
      app.vm.network "private_network", ip: "192.168.56.10"
      app.vm.network "forwarded_port", guest: 22, host: 20010, id: "server-0-ssh", auto_correct: false
      app.vm.network "forwarded_port", guest: 16443, host: 16443, id: "kubernetes-api", auto_correct: false
      app.vm.provider "virtualbox" do |vb|
        vb.memory = 1024
        vb.cpus = 1
      end
    end
  
    config.vm.define "server_1" do |app|
      app.vm.box = "bento/debian-12"
      app.vm.network "private_network", ip: "192.168.56.11"
      app.vm.network "forwarded_port", guest: 22, host: 20011, id: "server-1-ssh", auto_correct: false
      app.vm.provider "virtualbox" do |vb|
        vb.memory = 1024
        vb.cpus = 1
      end
    end
  
    config.vm.define "server_2" do |app|
      app.vm.box = "bento/debian-12"
      app.vm.network "private_network", ip: "192.168.56.12"
      app.vm.network "forwarded_port", guest: 22, host: 20012, id: "server-2-ssh", auto_correct: false
      app.vm.provider "virtualbox" do |vb|
        vb.memory = 1024
        vb.cpus = 1
      end
    end
  
    # Workers
    config.vm.define "worker_0" do |app|
      app.vm.box = "bento/debian-12"
      app.vm.network "private_network", ip: "192.168.56.20"
      app.vm.network "forwarded_port", guest: 22, host: 20020, id: "worker-0-ssh", auto_correct: false
      app.vm.network "forwarded_port", guest: 30443, host: 8443, id: "worker-0-https", auto_correct: false
      app.vm.network "forwarded_port", guest: 30080, host: 8080, id: "worker-0-http", auto_correct: false
      app.vm.provider "virtualbox" do |vb|
        vb.memory = 2048
        vb.cpus = 1
      end
    end
  
    config.vm.define "worker_1" do |app|
      app.vm.box = "bento/debian-12"
      app.vm.network "private_network", ip: "192.168.56.21"
      app.vm.network "forwarded_port", guest: 22, host: 20021, id: "worker-1-ssh", auto_correct: false
      app.vm.provider "virtualbox" do |vb|
        vb.memory = 2048
        vb.cpus = 1
      end
    end
  
    config.vm.define "worker_2" do |app|
      app.vm.box = "bento/debian-12"
      app.vm.network "private_network", ip: "192.168.56.22"
      app.vm.network "forwarded_port", guest: 22, host: 20022, id: "worker-2-ssh", auto_correct: false
      app.vm.provider "virtualbox" do |vb|
        vb.memory = 2048
        vb.cpus = 1
      end
    end
  
  end
  