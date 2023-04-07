"""Generated wrapper for PaymentSplitterUpgradeable Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers.bases import ContractMethod, Validator
from zero_ex.contract_wrappers.tx_params import TxParams


# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for PaymentSplitterUpgradeable below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        PaymentSplitterUpgradeableValidator,
    )
except ImportError:

    class PaymentSplitterUpgradeableValidator(Validator):  # type: ignore
        """No-op input validator."""


try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class PayeeMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the payee method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, index: int):
        """Validate the inputs to the payee method."""
        self.validator.assert_valid(
            method_name="payee",
            parameter_name="index",
            argument_value=index,
        )
        # safeguard against fractional inputs
        index = int(index)
        return index

    def call(self, index: int, tx_params: Optional[TxParams] = None) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(index).call(tx_params.as_dict())
        return str(returned)

    def send_transaction(
        self, index: int, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).transact(tx_params.as_dict())

    def build_transaction(
        self, index: int, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, index: int, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (index) = self.validate_and_normalize_inputs(index)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index).estimateGas(tx_params.as_dict())


class PayeeCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the payeeCount method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class Releasable1Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the releasable method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the releasable method."""
        self.validator.assert_valid(
            method_name="releasable",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class Releasable2Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the releasable method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token: str, account: str):
        """Validate the inputs to the releasable method."""
        self.validator.assert_valid(
            method_name="releasable",
            parameter_name="token",
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        self.validator.assert_valid(
            method_name="releasable",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (token, account)

    def call(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token, account).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).estimateGas(
            tx_params.as_dict()
        )


class Release1Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the release method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the release method."""
        self.validator.assert_valid(
            method_name="release",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(account).call(tx_params.as_dict())

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class Release2Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the release method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token: str, account: str):
        """Validate the inputs to the release method."""
        self.validator.assert_valid(
            method_name="release",
            parameter_name="token",
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        self.validator.assert_valid(
            method_name="release",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (token, account)

    def call(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        self._underlying_method(token, account).call(tx_params.as_dict())

    def send_transaction(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).estimateGas(
            tx_params.as_dict()
        )


class Released2Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the released method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token: str, account: str):
        """Validate the inputs to the released method."""
        self.validator.assert_valid(
            method_name="released",
            parameter_name="token",
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        self.validator.assert_valid(
            method_name="released",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (token, account)

    def call(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token, account).call(
            tx_params.as_dict()
        )
        return int(returned)

    def send_transaction(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).transact(
            tx_params.as_dict()
        )

    def build_transaction(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token: str, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token, account) = self.validate_and_normalize_inputs(token, account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token, account).estimateGas(
            tx_params.as_dict()
        )


class Released1Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the released method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the released method."""
        self.validator.assert_valid(
            method_name="released",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class SharesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the shares method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, account: str):
        """Validate the inputs to the shares method."""
        self.validator.assert_valid(
            method_name="shares",
            parameter_name="account",
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return account

    def call(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(account).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, account: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(
            tx_params.as_dict()
        )


class TotalReleased2Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalReleased method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
        validator: Validator = None,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address, validator)
        self._underlying_method = contract_function

    def validate_and_normalize_inputs(self, token: str):
        """Validate the inputs to the totalReleased method."""
        self.validator.assert_valid(
            method_name="totalReleased",
            parameter_name="token",
            argument_value=token,
        )
        token = self.validate_and_checksum_address(token)
        return token

    def call(self, token: str, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        (token) = self.validate_and_normalize_inputs(token)
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method(token).call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, token: str, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (token) = self.validate_and_normalize_inputs(token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token).transact(tx_params.as_dict())

    def build_transaction(
        self, token: str, tx_params: Optional[TxParams] = None
    ) -> dict:
        """Construct calldata to be used as input to the method."""
        (token) = self.validate_and_normalize_inputs(token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token).buildTransaction(
            tx_params.as_dict()
        )

    def estimate_gas(
        self, token: str, tx_params: Optional[TxParams] = None
    ) -> int:
        """Estimate gas consumption of method call."""
        (token) = self.validate_and_normalize_inputs(token)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(token).estimateGas(tx_params.as_dict())


class TotalReleased1Method(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalReleased method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class TotalSharesMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the totalShares method."""

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        contract_function: ContractFunction,
    ):
        """Persist instance data."""
        super().__init__(web3_or_provider, contract_address)
        self._underlying_method = contract_function

    def call(self, tx_params: Optional[TxParams] = None) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        tx_params = super().normalize_tx_params(tx_params)
        returned = self._underlying_method().call(tx_params.as_dict())
        return int(returned)

    def send_transaction(
        self, tx_params: Optional[TxParams] = None
    ) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class PaymentSplitterUpgradeable:
    """Wrapper class for PaymentSplitterUpgradeable Solidity contract."""

    payee: PayeeMethod
    """Constructor-initialized instance of
    :class:`PayeeMethod`.
    """

    payee_count: PayeeCountMethod
    """Constructor-initialized instance of
    :class:`PayeeCountMethod`.
    """

    releasable1: Releasable1Method
    """Constructor-initialized instance of
    :class:`Releasable1Method`.
    """

    releasable2: Releasable2Method
    """Constructor-initialized instance of
    :class:`Releasable2Method`.
    """

    release1: Release1Method
    """Constructor-initialized instance of
    :class:`Release1Method`.
    """

    release2: Release2Method
    """Constructor-initialized instance of
    :class:`Release2Method`.
    """

    released2: Released2Method
    """Constructor-initialized instance of
    :class:`Released2Method`.
    """

    released1: Released1Method
    """Constructor-initialized instance of
    :class:`Released1Method`.
    """

    shares: SharesMethod
    """Constructor-initialized instance of
    :class:`SharesMethod`.
    """

    total_released2: TotalReleased2Method
    """Constructor-initialized instance of
    :class:`TotalReleased2Method`.
    """

    total_released1: TotalReleased1Method
    """Constructor-initialized instance of
    :class:`TotalReleased1Method`.
    """

    total_shares: TotalSharesMethod
    """Constructor-initialized instance of
    :class:`TotalSharesMethod`.
    """

    def __init__(
        self,
        web3_or_provider: Union[Web3, BaseProvider],
        contract_address: str,
        validator: PaymentSplitterUpgradeableValidator = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param web3_or_provider: Either an instance of `web3.Web3`:code: or
            `web3.providers.base.BaseProvider`:code:
        :param contract_address: where the contract has been deployed
        :param validator: for validation of method inputs.
        """
        # pylint: disable=too-many-statements

        self.contract_address = contract_address

        if not validator:
            validator = PaymentSplitterUpgradeableValidator(
                web3_or_provider, contract_address
            )

        web3 = None
        if isinstance(web3_or_provider, BaseProvider):
            web3 = Web3(web3_or_provider)
        elif isinstance(web3_or_provider, Web3):
            web3 = web3_or_provider
        else:
            raise TypeError(
                "Expected parameter 'web3_or_provider' to be an instance of either"
                + " Web3 or BaseProvider"
            )

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware["function"],
                        layer=middleware["layer"],
                    )
            except ValueError as value_error:
                if value_error.args == (
                    "You can't add the same un-named instance twice",
                ):
                    pass

        self._web3_eth = web3.eth

        functions = self._web3_eth.contract(
            address=to_checksum_address(contract_address),
            abi=PaymentSplitterUpgradeable.abi(),
        ).functions

        self.payee = PayeeMethod(
            web3_or_provider, contract_address, functions.payee, validator
        )

        self.payee_count = PayeeCountMethod(
            web3_or_provider, contract_address, functions.payeeCount
        )

        self.releasable1 = Releasable1Method(
            web3_or_provider, contract_address, functions.releasable, validator
        )

        self.releasable2 = Releasable2Method(
            web3_or_provider, contract_address, functions.releasable, validator
        )

        self.release1 = Release1Method(
            web3_or_provider, contract_address, functions.release, validator
        )

        self.release2 = Release2Method(
            web3_or_provider, contract_address, functions.release, validator
        )

        self.released2 = Released2Method(
            web3_or_provider, contract_address, functions.released, validator
        )

        self.released1 = Released1Method(
            web3_or_provider, contract_address, functions.released, validator
        )

        self.shares = SharesMethod(
            web3_or_provider, contract_address, functions.shares, validator
        )

        self.total_released2 = TotalReleased2Method(
            web3_or_provider,
            contract_address,
            functions.totalReleased,
            validator,
        )

        self.total_released1 = TotalReleased1Method(
            web3_or_provider, contract_address, functions.totalReleased
        )

        self.total_shares = TotalSharesMethod(
            web3_or_provider, contract_address, functions.totalShares
        )

    def get_erc20_payment_released_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for ERC20PaymentReleased event.

        :param tx_hash: hash of transaction emitting ERC20PaymentReleased event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=PaymentSplitterUpgradeable.abi(),
            )
            .events.ERC20PaymentReleased()
            .processReceipt(tx_receipt)
        )

    def get_initialized_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Initialized event.

        :param tx_hash: hash of transaction emitting Initialized event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=PaymentSplitterUpgradeable.abi(),
            )
            .events.Initialized()
            .processReceipt(tx_receipt)
        )

    def get_payee_added_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PayeeAdded event.

        :param tx_hash: hash of transaction emitting PayeeAdded event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=PaymentSplitterUpgradeable.abi(),
            )
            .events.PayeeAdded()
            .processReceipt(tx_receipt)
        )

    def get_payment_received_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PaymentReceived event.

        :param tx_hash: hash of transaction emitting PaymentReceived event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=PaymentSplitterUpgradeable.abi(),
            )
            .events.PaymentReceived()
            .processReceipt(tx_receipt)
        )

    def get_payment_released_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for PaymentReleased event.

        :param tx_hash: hash of transaction emitting PaymentReleased event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._web3_eth.contract(
                address=to_checksum_address(self.contract_address),
                abi=PaymentSplitterUpgradeable.abi(),
            )
            .events.PaymentReleased()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"contract IERC20Upgradeable","name":"token","type":"address"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ERC20PaymentReleased","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"shares","type":"uint256"}],"name":"PayeeAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"PaymentReceived","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"PaymentReleased","type":"event"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"payee","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"payeeCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"releasable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20Upgradeable","name":"token","type":"address"},{"internalType":"address","name":"account","type":"address"}],"name":"releasable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address payable","name":"account","type":"address"}],"name":"release","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20Upgradeable","name":"token","type":"address"},{"internalType":"address","name":"account","type":"address"}],"name":"release","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERC20Upgradeable","name":"token","type":"address"},{"internalType":"address","name":"account","type":"address"}],"name":"released","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"released","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"shares","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20Upgradeable","name":"token","type":"address"}],"name":"totalReleased","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalReleased","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalShares","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'  # noqa: E501 (line-too-long)
        )


# pylint: disable=too-many-lines
