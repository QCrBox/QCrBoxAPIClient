from qcrboxapiclient.client import Client


def get_sync_client(base_url: str) -> Client:
    """Instantiate a synchronous API client object.

    Parameters
    ----------
    base_url : str
        The base URL of the API, e.g. http://127.0.0.1:11000

    Returns
    -------
    Client
        An instance of the API client.
    """
    return Client(base_url=base_url)
