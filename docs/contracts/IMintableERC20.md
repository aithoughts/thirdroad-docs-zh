---
slug: /IMintableERC20
title: IMintableERC20
hide_title: true
displayed_sidebar: contracts
---

# IMintableERC20

_thirdweb_

## Methods

### mintTo

```solidity
function mintTo(address to, uint256 amount) external nonpayable
```

_Creates `amount` new tokens for `to`. See {ERC20-\_mint}. Requirements: - the caller must have the `MINTER_ROLE`._

#### Parameters

| Name   | Type    | Description |
| ------ | ------- | ----------- |
| to     | address | undefined   |
| amount | uint256 | undefined   |

## Events

### TokensMinted

```solidity
event TokensMinted(address indexed mintedTo, uint256 quantityMinted)
```

_Emitted when tokens are minted with `mintTo`_

#### Parameters

| Name               | Type    | Description |
| ------------------ | ------- | ----------- |
| mintedTo `indexed` | address | undefined   |
| quantityMinted     | uint256 | undefined   |
