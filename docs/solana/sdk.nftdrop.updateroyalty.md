---
slug: /sdk.nftdrop.updateroyalty
title: NFTDrop.updateRoyalty() method
hide_title: true
displayed_sidebar: solana
---

<!-- Do not edit this file. It is automatically generated by API Documenter. -->

# NFTDrop.updateRoyalty() method

Update the royalty basis points of the collection

**Signature:**

```typescript
updateRoyalty(sellerFeeBasisPoints: number, updateAll?: boolean): Promise<TransactionResult[] | {
        signature: string;
    }>;
```

## Parameters

| Parameter            | Type    | Description                                                                                   |
| -------------------- | ------- | --------------------------------------------------------------------------------------------- |
| sellerFeeBasisPoints | number  | the royalty basis points of the collection                                                    |
| updateAll            | boolean | _(Optional)_ whether or not to retroactively update the royalty basis points of all past NFTs |

**Returns:**

Promise&lt;TransactionResult\[\] \| { signature: string; }&gt;