# Pingtool

Basic tool for pinging hostnames and IP addresses with ports.

### Installing

`git clone https://github.com/xNPx3/Pingtool.git`

`pip install -r requirements.txt`

### Usage

`python3 main.py <args>`

### Help
|   Argument   | Alternative | Parameter type |                    Info                    |
|--------------|-------------|----------------|--------------------------------------------|
|    --help    |      -h     |      None      |               Displays help                |
|  --verbose   |      -v     |      None      |            Enables verbose mode            |
|    --port    |      -p     |    Integer     |             Sets port to scan              |
|  --timeout   |      -t     |     Float      |             Sets scan timeout              |
|   --range    |      -r     |    Integer     |      Sets the amount of times to scan      |
| --r-address  |      -a     |      None      |        Enables random address mode         |
|   --r-port   |      -b     |      None      |          Enables random port mode          |
| --ip-address |      -i     |      Str       |          Sets IP address to scan           |
|  --database  |      -d     |      None      | Saves online addresses to a MySQL database |
|  --portscan  |      -s     |      None      |           Enables portscan mode            |
