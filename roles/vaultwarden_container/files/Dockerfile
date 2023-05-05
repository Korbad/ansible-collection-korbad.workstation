FROM docker.io/manjarolinux/base

RUN pacman -Sy vaultwarden vaultwarden-web systemd systemd-sysvcompat --noconfirm && \
    echo "WEB_VAULT_FOLDER=/usr/share/webapps/vaultwarden-web" >> /etc/vaultwarden.env && \ 
    echo "WEB_VAULT_ENABLED=true" >> /etc/vaultwarden.env
    
RUN systemctl start vaultwarden && \
    systemctl enable vaultwarden 
