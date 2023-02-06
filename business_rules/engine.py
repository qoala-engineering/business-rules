from .fields import FIELD_NO_INPUT

class _BaseEngine():
    # private methods
    def __run(self, rule, defined_variables):
        conditions = rule['conditions']
        rule_triggered = self.__check_conditions_recursively(conditions, defined_variables)
        if rule_triggered:
            return True
        return False

    def __run_with_action(self, rule, defined_variables, defined_actions):
        conditions = rule['conditions']
        actions = rule['actions']
        rule_triggered = self.__check_conditions_recursively(conditions, defined_variables)
        if rule_triggered:
            self.__do_actions(actions, defined_actions)
            return True
        return False

    def __check_conditions_recursively(self, conditions, defined_variables):
        keys = list(conditions.keys())
        if keys == ['all']:
            assert len(conditions['all']) >= 1
            for condition in conditions['all']:
                if not self.__check_conditions_recursively(condition, defined_variables):
                    return False
            return True

        elif keys == ['any']:
            assert len(conditions['any']) >= 1
            for condition in conditions['any']:
                if self.__check_conditions_recursively(condition, defined_variables):
                    return True
            return False

        else:
            # help prevent errors - any and all can only be in the condition dict
            # if they're the only item
            assert not ('any' in keys or 'all' in keys)
            return self.__check_condition(conditions, defined_variables)

    def __check_condition(self, condition, defined_variables):
        """ Checks a single rule condition - the condition will be made up of
        variables, values, and the comparison operator. The defined_variables
        object must have a variable defined for any variables in this condition.
        """
        name, op, value = condition['name'], condition['operator'], condition['value']
        operator_type = self.__get_variable_value(defined_variables, name)
        return self.__do_operator_comparison(operator_type, op, value)

    def __get_variable_value(self, defined_variables, name):
        """ Call the function provided on the defined_variables object with the
        given name (raise exception if that doesn't exist) and casts it to the
        specified type.

        Returns an instance of operators.BaseType
        """
        def fallback(*args, **kwargs):
            raise AssertionError("Variable {0} is not defined in class {1}".format(
                    name, defined_variables.__class__.__name__))
        method = getattr(defined_variables, name, fallback)
        val = method()
        return method.field_type(val)

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

    def __do_actions(self, actions, defined_actions):
        for action in actions:
            method_name = action['name']
            def fallback(*args, **kwargs):
                raise AssertionError("Action {0} is not defined in class {1}"\
                        .format(method_name, defined_actions.__class__.__name__))
            params = action.get('params') or {}
            method = getattr(defined_actions, method_name, fallback)
            method(**params)


class Engine(_BaseEngine):
    def __init__ (self):
        pass

    def validate(self, rule, variable):
        res = self._BaseEngine__run(rule, variable)
        return {"validation_result": res }

    def validate_bulk(self, rule_map, variable):
        res = []
        valid_identifiers = []
        print(rule_map.keys())
        for ruleData in rule_map.keys():
            resData = self._BaseEngine__run(rule_map[ruleData], variable)
            res.append(resData)
            if resData:
                valid_identifiers.append(ruleData)
        return {"validation_results": res, "valid_identifiers": valid_identifiers }
