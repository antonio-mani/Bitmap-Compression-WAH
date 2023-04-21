# Bitmap-Compression-WAH

## Description
Python script that takes text files in data, creates bit maps, and uses word aligned hybrid compression with 8, 16, 32, and 64 word sizes

compress_index(bitmap_index, output_path, compression_method, word_size):
        When calling compress bitmap_index should have the following format including txt suffix "./<somedir>/<somedir>/<bitmapFileName>.txt"
        output_path should just be a path to a directory without a slash following ex: "./<somedir>/<somedir>"
        compression_method is just a str and word_size is just an integer
def create_index(input_path, output_path, sorted):
        When making a call to create index, input_path should have the same format at bitmap_index from function above "./<somedir>/<somedir>/<bitmapFileName>"
        output_path just as the previous function should be the path to a directory without a trailing slash "./<somedir>/<somedir>"
        sorted should be a 1 or a 0 if you want both a sorted and unsorted bitmap set sorted to 1. If you want just an unsorted bitmap sorted should be 0
