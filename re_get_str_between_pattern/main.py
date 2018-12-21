import re

if __name__ == '__main__':
    origin_str = '4854864apple5856486'
    target = 'apple'
    print("origin: {}\ntarge: {}".format(origin_str, target))
    result = re.search('[0-9]*([a-z]*)[0-9]*', origin_str).group(1)
    print("result: {}".format(result))
    
