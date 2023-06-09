---
slug: /IClaimableERC1155
title: IClaimableERC1155
hide_title: true
displayed_sidebar: contracts
---

# IClaimableERC1155

_thirdweb_

## Methods

### claim

```solidity
function claim(address _receiver, uint256 _tokenId, uint256 _quantity) external payable
```

Lets an address claim multiple lazy minted NFTs at once to a recipient. Contract creators should override this function to create custom logic for claiming, for e.g. price collection, allowlist, max quantity, etc.

_The logic in the `verifyClaim` function determines whether the caller is authorized to mint NFTs._

#### Parameters

| Name       | Type    | Description                                 |
| ---------- | ------- | ------------------------------------------- |
| \_receiver | address | The recipient of the tokens to mint.        |
| \_tokenId  | uint256 | The tokenId of the lazy minted NFT to mint. |
| \_quantity | uint256 | The number of tokens to mint.               |

### verifyClaim

```solidity
function verifyClaim(address _claimer, uint256 _tokenId, uint256 _quantity) external view
```

Override this function to add logic for claim verification, based on conditions such as allowlist, price, max quantity etc.

_Checks a request to claim NFTs against a custom condition._

#### Parameters

| Name       | Type    | Description                                 |
| ---------- | ------- | ------------------------------------------- |
| \_claimer  | address | Caller of the claim function.               |
| \_tokenId  | uint256 | The tokenId of the lazy minted NFT to mint. |
| \_quantity | uint256 | The number of NFTs being claimed.           |

## Events

### TokensClaimed

```solidity
event TokensClaimed(address indexed claimer, address indexed receiver, uint256 indexed tokenId, uint256 quantityClaimed)
```

_Emitted when tokens are claimed_

#### Parameters

| Name               | Type    | Description |
| ------------------ | ------- | ----------- |
| claimer `indexed`  | address | undefined   |
| receiver `indexed` | address | undefined   |
| tokenId `indexed`  | uint256 | undefined   |
| quantityClaimed    | uint256 | undefined   |
