---
slug: /ProxyForUpgradeable
title: ProxyForUpgradeable
hide_title: true
displayed_sidebar: contracts
---

# ProxyForUpgradeable

_This contract implements an upgradeable proxy. It is upgradeable because calls are delegated to an implementation address that can be changed. This address is stored in storage in the location specified by [EIP1967](https://eips.ethereum.org/EIPS/eip-1967), so that it doesn&#39;t conflict with the storage layout of the implementation behind the proxy._

## Events

### AdminChanged

```solidity
event AdminChanged(address previousAdmin, address newAdmin)
```

#### Parameters

| Name          | Type    | Description |
| ------------- | ------- | ----------- |
| previousAdmin | address | undefined   |
| newAdmin      | address | undefined   |

### BeaconUpgraded

```solidity
event BeaconUpgraded(address indexed beacon)
```

#### Parameters

| Name             | Type    | Description |
| ---------------- | ------- | ----------- |
| beacon `indexed` | address | undefined   |

### Upgraded

```solidity
event Upgraded(address indexed implementation)
```

#### Parameters

| Name                     | Type    | Description |
| ------------------------ | ------- | ----------- |
| implementation `indexed` | address | undefined   |
