from inspect import signature



if __name__ == "__main__":
    def demo(x):
        return x
    
    print(signature(demo).parameters['x'])
