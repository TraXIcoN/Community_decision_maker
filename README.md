# Decentralized Voting System Utilizing Blockchain

This is a straightforward decentralized voting system leveraging blockchain technology with an emphasis on security. Each individual is granted a single voting right associated with their unique ID. The system guarantees the synchronization of node information, ensuring all nodes are updated. Nodes are multifunctional, serving either as a voting or mining system. The network is implemented using Flask framework.

## Primary Node

To connect all other nodes to the network, a primary node is employed. Upon startup, a new node transmits its details to the primary node.

## Block Structure

```json
{
    "index": 2,
    "previous_hash": "<hash value>",
    "proof": 35293,
    "timestamp": 1644346339.117375,
    "votes": [
        {
            "person_id": "<hash value>",
            "vote": "100"
        }
    ]
}
```

## Setup Instructions

Begin by ensuring that the following packages are installed:

```bash
pip3 install -r req.txt
```

Next, execute the application:

```bash
python3 main.py
```

Lastly, input your host address and port, for instance:

```bash
Host: 127.0.0.1
Port: 5050
```

## Node Registration with Blockchain

To register your device as a node with the blockchain, send a GET request to your device as follows:

```python
import requests
requests.get('http://<your-host>:<your-port>/init')
```

Alternatively, this can be done using Postman.

# Interacting with Nodes

You can interact with your node by sending HTTP requests to it.

### Retrieve List of All Nodes

```
Address: /nodes
Method: GET
Parameters: None
```

### Fetch Votes Not Yet Added to the Block

```
Address: /current-votes
Method: GET
Parameters: None
```

### Access Blockchain

```
Address: /chain
Method: GET
Parameters: None
```

### Update Node Data

```
Address: /update-block
Method: GET
Parameters: None
```

### Mine a New Block

```
Address: /mine
Method: GET
Parameters: None
```

### Tally Votes

```
Address: /count-votes
Method: GET
Parameters: None
```

### Add a New Vote

Each individual's ID is hashed and added to the blockchain. Votes are submitted in the following format:

```
'1001'
```

Signifying the first and last individuals who have cast their votes. To add a new vote:

```bash
Address: /new-vote
Method: POST
Parameters: {
    'person_id': id,
    'vote': vote,
}
```