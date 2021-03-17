#!/usr/bin/env bash
echo ""
echo "> Placing environments in nginx config..."
echo "----------------------------------------"

upstream="s/!SERVER/$UPSTREAM_APP_URL/g"
http_port="s/!HTTPPORT/$HTTP_SERVER_PORT/g"
https_port="s/!HTTPSPORT/$HTTPS_SERVER_PORT/g"
server_name="s/!SERVERNAME/$SERVER_NAME/g"
proxy_pass="s/!PROXYPASS/$PROXY_PASS/g"


sed -i "$upstream" /etc/nginx/nginx.conf
sed -i "$http_port" /etc/nginx/nginx.conf
sed -i "$https_port" /etc/nginx/nginx.conf
sed -i "$server_name" /etc/nginx/nginx.conf
sed -i "$proxy_pass" /etc/nginx/nginx.conf

echo ""
echo "> Launching nginx services..."
echo "----------------------------------------"
nginx -g "daemon off;"