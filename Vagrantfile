# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "django-rest-git"
  config.vm.network "forwarded_port", guest: 8000, host: 8080, auto_correct: true
  # To facilitate the NFS share
  config.vm.network "private_network", type: "dhcp"
  config.vm.synced_folder ".", "/vagrant", type: "nfs"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "768"
  end


  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    # Install some prereqs
    sudo apt-get update --fix-missing
    sudo apt-get install -y make build-essential git emacs graphviz libgraphviz-dev pkg-config python-dev curl libjpeg-dev libfreetype6-dev zlib1g-dev pkg-config python-virtualenv nginx redis-server libxml2-dev libxslt1-dev

    # Add apt file for PostgreSQL (obtained from postgresql.org)
    echo  "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
    sudo apt-key add -
    sudo apt-get update --fix-missing
    sudo apt-get install -y --force-yes postgresql postgresql-server-dev-9.4 postgresql-9.4-postgis postgis postgresql-contrib

    # update the postgres user psw
    sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'password';"
    sudo -u postgres psql -U postgres -d postgres -c "CREATE USER bamboo WITH password 'password';"
    sudo -u postgres psql -U postgres -d postgres -c "ALTER USER bamboo WITH SUPERUSER;"
    sudo apt-get install git

    # Install virtualenv
    wget -O - https://gist.githubusercontent.com/jaywhy13/3ce4bed7b46c83892351/raw/0236675a39084e3c50978cfba2bdcabf2405d84d/install_virtualenv.sh | sh

    # Configure Byobu
    wget -O - https://gist.githubusercontent.com/jaywhy13/b3b3fb1add6a98c89b3a/raw/c418d91e5025f9fd8d51c978981330a1b30639ad/customize_byobu_keybindings.sh | sh
  SHELL

end

