def unpack_styles(styles):
    """combine a dictionary of CSS property/value pairs into a string"""
    return "; ".join([": ".join(i) for i in styles.items()])
