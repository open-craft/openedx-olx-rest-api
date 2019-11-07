Open edX OLX REST API
=====================

This is a django app plugin for exporting OLX data from modulestore via a REST
API. In particular, it is useful for writing apps that read OLX out of
modulestore and then push it into Blockstore.


## Installation

```
make studio-shell
cd /edx/src
git clone https://github.com/open-craft/openedx-olx-rest-api.git
pip install -e /edx/src/openedx-olx-rest-api
```

## Usage

Access the API at `(Studio URL)/api/olx-export/v1/xblock/:block_id/`

Devstack Demo Course Example: http://localhost:18010/api/olx-export/v1/xblock/block-v1:edX+DemoX+Demo_Course+type@html+block@030e35c4756a4ddc8d40b95fbbfff4d4/

Output format:

```json
{
    "root_block_id": "block id",
    "blocks": {
        "block id": {
            "olx": "OLX string",
            "static_files": {
                "filename": {"url": "https://..."},
                ...
            }
        },
        ...
    }
}
```

The `static_files` map will be missing if that particular XBlock doesn't
reference any static assets.
