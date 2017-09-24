SCRIPT_DIR=$(cd $(dirname $0); pwd)

# パッケージを更新する
sudo yum update -y

# ツールのインストール  
sudo yum -y install epel-release
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install yum-utils \
                    emacs \
                    python36u python36u-pip python36u-devel \
                    httpd httpd-devel

# ネットワーク設定
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload

# Update configurations
cp --force $SCRIPT_DIR/../configurations/conf.d/django.conf /etc/httpd/conf.d/django.conf
cp --force $SCRIPT_DIR/../configurations/conf.modules.d/django-wsgi.conf /etc/httpd/conf.modules.d/django-wsgi.conf

# Setup develop environment
bash $SCRIPT_DIR/setup_dev_env.sh
bash $SCRIPT_DIR/setup_django.sh
chmod 777 -R .

# HTTP サーバーを起動
sudo systemctl start httpd

# ssh の鍵生成
# ssh-keygen -t rsa

echo "Setup Done!!"
