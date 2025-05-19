from robot.api.deco import keyword


@keyword
def should_not_be_none(value, name="Value"):
    if value is None:
        raise AssertionError(f"{name} should not be None.")


@keyword
def check_object_has_attributes(object, *attributes):
    missing = [attribute for attribute in attributes if not hasattr(object, attribute)]
    if missing:
        raise AssertionError(f"Object is missing attributes: {missing}")
