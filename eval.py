import requests


def evaluation():
    # files = {
    # 'job_id': (None, '20181101-044714-679b'),
    # 'image_path': (None, '/data/datasets/imagenet/ilsvrc12/pet/Birman_/Birman_12.jpg'),
    # }

    #response = requests.post('http://localhost:8888/models/images/classification/classify_one.json', files=files)
    data = {'predictions': [['Birman', 100.0], [
        'Abyssinian', 0.0], ['Bengal', 0.0], ['Bombay', 0.0]]}

    return data