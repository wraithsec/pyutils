#!/usr/bin/env bash 
function gen_keys() {
    openssl genrsa -aes256 -passout pass:abcd -out server.pass.key 4096
    openssl rsa -passin pass:abcd -in server.pass.key -out server.key
    openssl req -new -key server.key -out server.csr
    openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt
}

if [[ $(ls -l *.{key,crt,csr}) ]]; then
while :; do
    printf "Detected old keys/certs. Do you wish to remove them and start fresh?: "
    read choice 
    choice="${choice,,}"
    case $choice in
        y|yes)  rm -f *{key,crt,csr} 
            gen_keys 
            echo "[+] Done, your keys are created! server.key and server.crt."
            break;;
        n|no) 
            break 
            ;;
        *) 
            echo "[!] Unknown choice!"
            continue
            ;;
    esac
done
else
    gen_keys
fi


echo "[ ] Use one of the following examples to exec the server:

python3 https_server.py 
python3 https_server.py -i 0.0.0.0 -p 8443 
python3 https_server.py -i 192.168.1.1 -p 4430 -c /etc/pki/server.crt -k /etc/pki/server.key"
