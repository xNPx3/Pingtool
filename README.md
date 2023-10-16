# Pingtool

Basic tool for pinging hostnames and IP addresses with ports.

*The software is provided "as is" and I am not responsible for any of actions made using this tool.*

### Installing

`git clone https://github.com/xNPx3/Pingtool.git`

`pip install -r requirements.txt`

### Usage

`python3 main.py <args>`

### Help
|   Argument   | Alternative | Parameter type |                    Info                    |  Default  |
|--------------|-------------|----------------|--------------------------------------------|-----------|
|    --help    |      -h     |      None      |               Displays help                |    None   |
| --r-address  |      -a     |      None      |        Enables random address mode         |   False   |
|   --r-port   |      -b     |      None      |          Enables random port mode          |   False   |
|  --database  |      -d     |      None      | Saves online addresses to a MySQL database |    None   |
| --ip-address |      -i     |     String     |          Sets IP address to scan           | localhost |
|    --port    |      -p     |     Integer    |             Sets port to scan              |     80    |
|   --range    |      -r     |     Integer    |      Sets the amount of times to scan      |     10    |
|  --portscan  |      -s     |      None      |           Enables portscan mode            |   False   |
|  --timeout   |      -t     |     Float      |        Sets scan timeout (seconds)         |     1     |
|  --verbose   |      -v     |      None      |            Enables verbose mode            |   False   |
