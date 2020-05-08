# Pingtool

Basic tool for pinging hostnames and IP addresses with ports.

### Installing

`git clone https://github.com/xNPx3/Pingtool.git`

`pip install -r requirements.txt`

### Usage

`python3 main.py <args>`

### Help
|   Argument   | Alternative | Parameter type |                    Info                    |  Default  |
|--------------|-------------|----------------|--------------------------------------------|-----------|
|    --help    |      -h     |      None      |               Displays help                |    None   |
|  --verbose   |      -v     |      None      |            Enables verbose mode            |   False   |
|    --port    |      -p     |    Integer     |             Sets port to scan              |     80    |
|  --timeout   |      -t     |     Float      |        Sets scan timeout (seconds)         |     1     |
|   --range    |      -r     |    Integer     |      Sets the amount of times to scan      |     10    |
| --r-address  |      -a     |      None      |        Enables random address mode         |   False   |
|   --r-port   |      -b     |      None      |          Enables random port mode          |   False   |
| --ip-address |      -i     |      Str       |          Sets IP address to scan           | localhost |
|  --database  |      -d     |      None      | Saves online addresses to a MySQL database |    None   |
|  --portscan  |      -s     |      None      |           Enables portscan mode            |   False   |
