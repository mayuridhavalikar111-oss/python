def demo_function(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(key, ":", value)

# Example usage
demo_function(10, 20, 30, name="Mayuri", age=21, city="Pune")