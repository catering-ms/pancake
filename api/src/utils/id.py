from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(42)


def get_product_id():
    val = next(gen)
    return str(val) 


def get_sub_product_id():
    the_id = uuid.uuid5(uuid.NAMESPACE_DNS, 'sub_product.id')
    return the_id