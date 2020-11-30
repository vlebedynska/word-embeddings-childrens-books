class Utils:

    @staticmethod
    def filter_list(list, filter):
        found_items = []
        not_found_items = []
        for item in filter:
            if item in list:
                found_items.append(item)
            else:
                not_found_items.append(item)
        return found_items, not_found_items


    @staticmethod
    def one_is_empty(a_attrs, b_attrs, x_targets, y_targets):
        list_of_length = []
        list_of_length.append(len(a_attrs))
        list_of_length.append(len(b_attrs))
        list_of_length.append(len(x_targets))
        list_of_length.append(len(y_targets))
        for item in list_of_length:
            if item != 0:
                continue
            else:
                return True
        return False
