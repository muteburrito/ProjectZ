from utils import giphy

def search(prompt):
    giphy_client = giphy.Giphy('RyU7IKIGZQxKyDO0imHtZewjfFjAgNzh')
    giphy_client.construct_params(prompt)
    data = giphy_client.get_gifs()
    return data