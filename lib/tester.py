import gif_looper

args = {
        'seek': 120,
        'duration': "1",
        'input_filename': '../projects/aldous/youtube-dl-stuff/Aldous Harding - The Barrel (Official Video)-QyZeJr5ppm8.mp4',
        'output_prefix': 'tester',
        'output_format': 'gif',
        'options': {
                "palette": True,
                "scale": {
                         "x": 480,
                         "y": -1
                },
                # "rev_and_join": True
        }
}

gif_looper.gif_looper(**args)