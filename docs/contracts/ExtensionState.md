---
slug: /ExtensionState
title: ExtensionState
hide_title: true
displayed_sidebar: contracts
---

# ExtensionState

## Events

### ExtensionAdded

```solidity
event ExtensionAdded(address indexed extensionAddress, bytes4 indexed functionSelector, string functionSignature)
```

#### Parameters

| Name                       | Type    | Description |
| -------------------------- | ------- | ----------- |
| extensionAddress `indexed` | address | undefined   |
| functionSelector `indexed` | bytes4  | undefined   |
| functionSignature          | string  | undefined   |

### ExtensionRemoved

```solidity
event ExtensionRemoved(address indexed extensionAddress, bytes4 indexed functionSelector, string functionSignature)
```

#### Parameters

| Name                       | Type    | Description |
| -------------------------- | ------- | ----------- |
| extensionAddress `indexed` | address | undefined   |
| functionSelector `indexed` | bytes4  | undefined   |
| functionSignature          | string  | undefined   |

### ExtensionUpdated

```solidity
event ExtensionUpdated(address indexed oldExtensionAddress, address indexed newExtensionAddress, bytes4 indexed functionSelector, string functionSignature)
```

#### Parameters

| Name                          | Type    | Description |
| ----------------------------- | ------- | ----------- |
| oldExtensionAddress `indexed` | address | undefined   |
| newExtensionAddress `indexed` | address | undefined   |
| functionSelector `indexed`    | bytes4  | undefined   |
| functionSignature             | string  | undefined   |
