import os
from .interface import (
    PluginInterface,
    Backend,
    Metadata,
    ResultType,
    QasmFilePath,
    check_backend,
    check_result_type,
    check_qasm_file,
    Results,
)


class Plugin(PluginInterface):
    """
    The Plugin class is the starting point for quantum-plugins.
    Using this, the server worker can interect directly with
    simulators.
    """

    def __init__(self):
        current_file_path = os.path.dirname(__file__)
        backends_relative_path = os.path.join(current_file_path, "backends.txt") 

        with open(backends_relative_path, 'r', encoding="UTF-8") as file:
            backends = list(map(lambda x: x.replace('\n', ''), file)) 
            super().__init__(backends)

    @check_backend
    @check_result_type
    @check_qasm_file
    def execute(
        self,
        target_backend: Backend,
        qasm_file_path: QasmFilePath,
        metadata: Metadata,
        result_type: ResultType,
    ) -> Results:
        """
        Do your execution logic here!!

        At the end, you must return either a dict(for counts or quasi dist) or a
        floating point number (for expectation values).

        Note: The decorators are used to ensure that the request backend,
            result_type and qasm file are correct.

        The client, sends 4 informations that are valuable to you:
            - target_backend: the choosen backend to run the job
            - qasm_file_path: the quantum algorithm in qasm format. You may handle
                IO errors while working with it.
            - metadata: the python client aggregates some data about the circuit like
                `depth`, `num_qubits`, `framework`, etc. This data might be insteresting
                for analysis and further checks.
            - result_type: the requested result type: `counts`, `quasi_dist` or `expval`.
        """

        raise NotImplementedError
