class NumpyArrayEncoder(json.JSONEncoder):
    """Serialize numpy arrays"""

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


dataset = {'alice': 0,
           'bob': 1,
           'cynthia': np.array([1, 1, 2, 3, 5, 8])}

# save dictionary as *.json file
path_out = "./dataset.json"
with open(path_out, 'w') as f:
    json.dump(dataset, f, indent='\t', cls=NumpyArrayEncoder, sort_keys=True)
