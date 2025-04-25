
#!/bin/bash
echo "[*] Installing CMS Scan Tools..."

# WordPress
if ! command -v wpscan &> /dev/null; then
  sudo gem install wpscan
fi

# Joomla
if [ ! -d /opt/joomscan ]; then
  git clone https://github.com/OWASP/joomscan.git /opt/joomscan
  ln -s /opt/joomscan/joomscan.pl /usr/bin/joomscan
fi

# Drupal
if ! command -v droopescan &> /dev/null; then
  pip install droopescan
fi

echo "[+] All CMS Tools Installed."
