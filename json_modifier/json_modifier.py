import json
from typing import List, Dict


class JsonModifier:

    def __init__(
            self,
            input_file: str = 'input.json',
            modifier_file: str = 'modify.json',
            output_file: str = 'output.json',
            id_field: str = 'name'
    ):
        self._input_file = input_file
        self._modifier_file = modifier_file
        self._output_file = output_file
        self._id_field = id_field

    def modify(self) -> None:
        input_data = self._load_data(self._input_file)
        update_data = self._load_data(self._modifier_file)
        result_data = []

        for input_item in input_data:
            for update_item in update_data:
                if input_item[self._id_field] == update_item[self._id_field]:  # modify by first attribute in a record
                    input_item.update(update_item)
            result_data.append(input_item)

        self._dump_data(self._output_file, result_data)

    def print_output(self) -> None:
        self._print_file(self._output_file)

    @staticmethod
    def _load_data(file: str) -> List[Dict[str, str]]:
        with open(file, "r") as f:
            return json.load(f)

    @staticmethod
    def _dump_data(file: str, data: List[Dict[str, str]]) -> None:
        with open(file, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def _print_file(cls, file: str) -> None:
        print(cls._load_data(file))


if __name__ == '__main__':
    json_modifier = JsonModifier()
    json_modifier.modify()
    json_modifier.print_output()
