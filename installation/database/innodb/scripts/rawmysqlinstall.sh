#!/bin/bash

# MySQL root password and cluster admin user details
mysqlrootpass="P@ssw0rd!"
clusterAdminUser="clusterAdmin"
clusterAdminPass="P@ssw0rd!"
mySqlVersion="8.0.32"  # Minimum MySQL Version that will be installed
buffer_size="$(free -k | awk '/^Mem:/{print int($2 * 0.7 / 1024 / 1024)}')"
max_connections="2001"

# Function to check if a line exists in the file
line_exists() {
  grep -q "^$1=" "$2"
}

# Function to replace or add a line in the file
replace_or_add_line() {
  if line_exists "$1" "$3"; then
    sudo sed -i "s/^$1=.*/$1=$2/" "$3"
  else
    echo "$1=$2" | sudo tee -a "$3"
  fi
}

# Function to ddddd the installed MySQL version
get_installed_mysql_version() {
  local mysql_version
  mysql_version=$(mysql --version | awk '{print $3}')
  echo "$mysql_version"
}

# Function to compare version numbers
version_compare() {
  local ver1="$1"
  local ver2="$2"

  if [[ "$ver1" == "$ver2" ]]; then
    return 0  # Versions are equal
  fi

  local IFS=.
  local ver1_parts=($ver1)
  local ver2_parts=($ver2)

  local max_len=$(( ${#ver1_parts[@]} > ${#ver2_parts[@]} ? ${#ver1_parts[@]} : ${#ver2_parts[@]} ))

  for ((i = 0; i < max_len; i++)); do
    local part1="${ver1_parts[i]:-0}"
    local part2="${ver2_parts[i]:-0}"

    if ((part1 > part2)); then
      return 0  # ver1 is greater
    elif ((part1 < part2)); then
      return 1  # ver1 is less
    fi
  done

  return 0  # Versions are equal (fallback)
}

# Function to start MySQL service and enable it on boot if it exists
start_mysql_service() {
  local mysql_service="mysql"
  local mysqld_service="mysqld"

  if [ "$(systemctl is-enabled "$mysql_service" 2>/dev/null)" == "disabled" ]; then
    sudo systemctl enable "$mysql_service" --quiet
    sudo systemctl restart "$mysql_service" --quiet
    echo "$mysql_service service started and enabled"
  elif [ "$(systemctl is-enabled "$mysql_service" 2>/dev/null)" == "enabled" ]; then
    sudo systemctl restart "$mysql_service" --quiet
    echo  "$mysql_service service started was already enabled"
  elif [ "$(systemctl is-enabled "$mysqld_service" 2>/dev/null)" == "disabled" ]; then
    sudo systemctl enable "$mysqld_service" --quiet
    sudo systemctl restart "$mysqld_service" --quiet
    echo "$mysqld_service service started and enabled"
  elif [ "$(systemctl is-enabled "$mysqld_service" 2>/dev/null)" == "enabled" ]; then
    sudo systemctl restart "$mysqld_service" --quiet
    echo "$mysqld_service service started was already enabled"
  fi
}

# Function to get the available MySQL version from the repositories
get_available_mysql_version() {
  local available_version

  if command -v apt-cache &>/dev/null; then
    available_version=$(apt-cache show mysql-server | grep -E "Version: [0-9]+\.[0-9]+\.[0-9]+" | awk '{match($2, /[0-9]+\.[0-9]+\.[0-9]+/); print substr($2, RSTART, RLENGTH)}' | head -n 1)
  elif command -v yum &>/dev/null; then
    available_version=$(yum list mysql-server --showduplicates | awk '/mysql-server/ {print $2}' | grep -oE '^[0-9]+\.[0-9]+\.[0-9]+' | sort -Vr | head -n 1)
  elif command -v dnf &>/dev/null; then
    available_version=$(dnf --showduplicates list mysql-server | grep -Eo "[0-9]+\.[0-9]+\.[0-9]+" | sort -r | head -n 1)
  else
    echo "Unsupported package manager. Manual installation required."
    exit 1
  fi

  echo "$available_version"
}

add_firewall_rules() {
  # Check if firewalld is installed and running
  if systemctl is-active --quiet firewalld; then
    # Add individual rules for each port for firewalld
    firewall-cmd --zone=public --add-port=3306/tcp --permanent --quiet
    firewall-cmd --zone=public --add-port=33060/tcp --permanent --quiet
    firewall-cmd --zone=public --add-port=33061/tcp --permanent --quiet
    firewall-cmd --zone=public --add-port=33062/tcp --permanent --quiet

    # Reload firewalld to apply the changes for firewalld
    firewall-cmd --reload --quiet

    echo "Firewalld rules added successfully."
  elif command -v ufw &>/dev/null && ufw status | grep -q "Status: active"; then
    # Add UFW rules for Ubuntu
    ufw allow 3306/tcp > /dev/null
    ufw allow 33060/tcp > /dev/null
    ufw allow 33061/tcp > /dev/null
    ufw allow 33062/tcp > /dev/null

    echo "UFW rules added successfully."
  else
    echo "Firewalld or UFW is not available on this system."
    return 1
  fi
}

# Function to install MySQL Server based on the package manager
check_mysql_installed() {
  if command -v mysql &>/dev/null; then
    MYSQL_VERSION=$(get_installed_mysql_version)
    echo $MYSQL_VERSION
  fi
}

install_mysql() {
  # Get the available MySQL version from the repositories
  AVAILABLE_VERSION=$(get_available_mysql_version)
  REQUIRED_VERSION="$mySqlVersion"

  # Check if the available version meets the minimum requirement
  version_compare "$AVAILABLE_VERSION" "$REQUIRED_VERSION"
  local compare_result=$?

  if [[ $compare_result -eq 0 ]]; then
    echo "MySQL version $AVAILABLE_VERSION will be installed."
    
    if [ "$NON_INTERACTIVE" = true ]; then
      echo "Proceeding with installation without user confirmation."
    else
      # Prompt for installation
      read -p "Do you want to continue with the installation? (y/n): " choice
      if [[ "$choice" != "y" ]]; then
        echo "Installation aborted."
        exit 0
      fi
    fi
  else
    echo "MySQL version $AVAILABLE_VERSION does not meet the minimum requirement of $REQUIRED_VERSION. Aborting installation."
    exit 0
  fi

  echo "Installing MySQL Server..."

  if command -v apt-get &>/dev/null; then  # Debian/Ubuntu
    sudo apt-get update
    sudo DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server
  elif command -v yum &>/dev/null; then  # CentOS/Red Hat
    sudo yum update -y
    sudo yum -y install mysql-server
  elif command -v dnf &>/dev/null; then  # Fedora
    sudo dnf -y install mysql-server
  else
    echo "Unsupported package manager. Manual installation required."
    exit 1
  fi

  # Start MySQL service and check if it's running
  start_mysql_service
  echo "MySQL installation and configuration complete."
}

################################################################################
################################################################################

# Parse arguments to check for --non-interactive
NON_INTERACTIVE=false
if [[ "$1" == "--non-interactive" ]]; then
  NON_INTERACTIVE=true
fi

# Main function

check_mysql_installed
add_firewall_rules
if [[ -z "$(check_mysql_installed)" ]]; then
  install_mysql
  mysql --user=root <<_EOF_
DELETE FROM mysql.user WHERE User='';
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
set persist sql_generate_invisible_primary_key=1;
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '${mysqlrootpass}';
CREATE USER '${clusterAdminUser}'@'%' IDENTIFIED BY '${clusterAdminPass}';
GRANT ALL PRIVILEGES ON *.* TO '${clusterAdminUser}'@'%' with grant option;
FLUSH PRIVILEGES;
_EOF_
else
  MYSQL_VERSION=$(get_installed_mysql_version)
  if [ "$NON_INTERACTIVE" = true ]; then
    echo "MySQL version $MYSQL_VERSION is already installed. Proceeding with configuration."
  else
    # Prompt the user to continue or abort
    read -p "MySQL version $MYSQL_VERSION is already installed. Do you want to continue with the configuration? (y/n): " choice
    if [[ "$choice" != "y" ]]; then
      echo "Configuration aborted."
      exit 0
    fi
  fi

  mysql -u root -p$mysqlrootpass <<_EOF_
DELETE FROM mysql.user WHERE User='';
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
set persist sql_generate_invisible_primary_key=1;
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '${mysqlrootpass}';
CREATE USER '${clusterAdminUser}'@'%' IDENTIFIED BY '${clusterAdminPass}';
GRANT ALL PRIVILEGES ON *.* TO '${clusterAdminUser}'@'%' with grant option;
FLUSH PRIVILEGES;
_EOF_
fi
