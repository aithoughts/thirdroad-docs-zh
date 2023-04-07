---
slug: /sdk.nftcollection.transfer
title: NFTCollection.transfer() method
hide_title: true
displayed_sidebar: solana
---

<!-- Do not edit this file. It is automatically generated by API Documenter. -->

# NFTCollection.transfer() method

Transfer the specified NFTs to another wallet

**Signature:**

```typescript
transfer(receiverAddress: string, nftAddress: string): Promise<TransactionResult>;
```

## Parameters

| Parameter       | Type   | Description                             |
| --------------- | ------ | --------------------------------------- |
| receiverAddress | string | The address to send the tokens to       |
| nftAddress      | string | The mint address of the NFT to transfer |

**Returns:**

Promise&lt;TransactionResult&gt;

the transaction result of the transfer

## Example

```jsx
// The wallet address to transfer the NFTs to
const to = "...";
// The mint address of the NFT to transfer
const nftAddress = "...";
const tx = await program.transfer(to, nftAddress);
```