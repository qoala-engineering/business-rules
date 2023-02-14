from .fields import FIELD_NO_INPUT
from .operators import (NumericType,
                        StringType,
                        BooleanType,
                        SelectMultipleType)


class _BaseEngine():
    # private methods
    def __run(self, rule, rule_maps):
        conditions = rule['conditions']
        rule_triggered = self.__check_conditions_recursively(conditions, rule_maps)
        if rule_triggered:
            return True
        return False

    def __check_conditions_recursively(self, conditions, rule_maps):
        keys = list(conditions.keys())
        if keys == ['all']:
            assert len(conditions['all']) >= 1
            for condition in conditions['all']:
                if not self.__check_conditions_recursively(condition, rule_maps):
                    return False
            return True

        elif keys == ['any']:
            assert len(conditions['any']) >= 1
            for condition in conditions['any']:
                if self.__check_conditions_recursively(condition, rule_maps):
                    return True
            return False

        else:
            # help prevent errors - any and all can only be in the condition dict
            # if they're the only item
            assert not ('any' in keys or 'all' in keys)
            return self.__check_condition(conditions, rule_maps)

    def __check_condition(self, condition, rule_maps):
        """ Checks a single rule condition - the condition will be made up of
        variables, values, and the comparison operator. The rule_maps
        object must have a variable defined for any variables in this condition.
        """
        name, op, value = condition['name'], condition['operator'], condition['value']
        operator_type = self.__get_variable_value(rule_maps, name)
        return self.__do_operator_comparison(operator_type, op, value)

    def __get_variable_value(self, rule_maps, name):
        var_map = {}
        for rule_map in rule_maps:
            if rule_map["name"] == name:
                var_map = rule_map
        if var_map["type"] == "numeric":
            return NumericType(var_map["value"])
        elif var_map["type"] == "string":
            return StringType(var_map["value"])
        elif var_map["type"] == "boolean":
            return BooleanType(var_map["value"])
        elif var_map["type"] == "select_multiple":
            return SelectMultipleType([var_map["value"]])

    def __do_operator_comparison(self, operator_type, operator_name, comparison_value):
        """ Finds the method on the given operator_type and compares it to the
        given comparison_value.

        operator_type should be an instance of operators.BaseType
        comparison_value is whatever python type to compare to
        returns a bool
        """
        def fallback(*args, **kwargs):
            raise AssertionError("Operator {0} does not exist for type {1}".format(
                operator_name, operator_type.__class__.__name__))
        method = getattr(operator_type, operator_name, fallback)
        if getattr(method, 'input_type', '') == FIELD_NO_INPUT:
            return method()
        return method(comparison_value)

class Engine(_BaseEngine):
    def __init__ (self):
        pass

    def validate(self, rule_variables, rule_data, input_data):
        #create a dict in python
        rule_variable_type_map = dict()
        for rule_variable in rule_variables:
            rule_variable_type_map[rule_variable["name"]] = rule_variable["type"]
        rule_maps = []
        for input_rule in input_data:
            rule_map = {
                "name": input_rule["name"],
                "type": rule_variable_type_map[input_rule["name"]],
                "value": input_rule["value"],
            }
            rule_maps.append(rule_map)
        res = self._BaseEngine__run(rule_data, rule_maps)
        return {"validation_result": res }    