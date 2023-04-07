---
slug: /sdk.nftcollection
title: NFTCollection class
hide_title: true
displayed_sidebar: solana
---

<!-- Do not edit this file. It is automatically generated by API Documenter. -->

# NFTCollection class

A collection of associated NFTs

**Signature:**

```typescript
export declare class NFTCollection
```

## Example

```jsx
import { ThirdwebSDK } from "@thirdweb-dev/sdk/solana";

const sdk = ThirdwebSDK.fromNetwork("devnet");
sdk.wallet.connect(signer);

// Get the interface for your NFT collection program
const program = await sdk.getProgram("{{program_address}}", "nft-collection");
```

## Constructors

| Constructor                                                                                 | Modifiers | Description                                                       |
| ------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------- |
| [(constructor)(collectionAddress, metaplex, storage)](./sdk.nftcollection._constructor_.md) |           | Constructs a new instance of the <code>NFTCollection</code> class |

## Properties

| Property                                          | Modifiers             | Type                                      | Description |
| ------------------------------------------------- | --------------------- | ----------------------------------------- | ----------- |
| [accountType](./sdk.nftcollection.accounttype.md) |                       | "nft-collection"                          |             |
| [network](./sdk.nftcollection.network.md)         | <code>readonly</code> | import("@metaplex-foundation/js").Cluster |             |
| [publicKey](./sdk.nftcollection.publickey.md)     |                       | PublicKey                                 |             |

## Methods

| Method                                                                                          | Modifiers | Description                                               |
| ----------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------- |
| [balance(nftAddress)](./sdk.nftcollection.balance.md)                                           |           | Get the NFT balance of the connected wallet               |
| [balanceOf(walletAddress, nftAddress)](./sdk.nftcollection.balanceof.md)                        |           | Get the NFT balance of the specified wallet               |
| [burn(nftAddress)](./sdk.nftcollection.burn.md)                                                 |           | Burn an NFT                                               |
| [burnBatch(nftAddresses)](./sdk.nftcollection.burnbatch.md)                                     |           | Burn multiple NFTs                                        |
| [get(nftAddress)](./sdk.nftcollection.get.md)                                                   |           | Get the metadata for a specific NFT                       |
| [getAll(queryParams)](./sdk.nftcollection.getall.md)                                            |           | Get the metadata for all NFTs on this collection          |
| [getCreators()](./sdk.nftcollection.getcreators.md)                                             |           | Get the creators of this program.                         |
| [getMetadata()](./sdk.nftcollection.getmetadata.md)                                             |           | Get the metadata for this program.                        |
| [getRoyalty()](./sdk.nftcollection.getroyalty.md)                                               |           | Get the royalty basis points for this collection          |
| [getTransactions(options)](./sdk.nftcollection.gettransactions.md)                              |           | **_(BETA)_** Get the all transactions for this program    |
| [mint(metadata)](./sdk.nftcollection.mint.md)                                                   |           | Mint NFTs to the connected wallet                         |
| [mintAdditionalSupply(nftAddress, amount)](./sdk.nftcollection.mintadditionalsupply.md)         |           | Mint additional supply of an NFT to the connected wallet  |
| [mintAdditionalSupplyTo(to, nftAddress, amount)](./sdk.nftcollection.mintadditionalsupplyto.md) |           | Mint additional supply of an NFT to the specified wallet  |
| [mintTo(to, metadata)](./sdk.nftcollection.mintto.md)                                           |           | Mint an NFT to the specified wallet                       |
| [ownerOf(nftAddress)](./sdk.nftcollection.ownerof.md)                                           |           | Get the current owner of the given NFT                    |
| [supplyOf(nftAddress)](./sdk.nftcollection.supplyof.md)                                         |           | Get the supply of NFT editions minted from a specific NFT |
| [totalSupply()](./sdk.nftcollection.totalsupply.md)                                             |           | Get the total number of nfts minted on this program       |
| [transfer(receiverAddress, nftAddress)](./sdk.nftcollection.transfer.md)                        |           | Transfer the specified NFTs to another wallet             |
| [updateCreators(creators, updateAll)](./sdk.nftcollection.updatecreators.md)                    |           | Update the creators of the collection                     |
| [updateRoyalty(sellerFeeBasisPoints, updateAll)](./sdk.nftcollection.updateroyalty.md)          |           | Update the royalty basis points of the collection         |