---
slug: /sdk.nftcollection.getmetadata
title: NFTCollection.getMetadata() method
hide_title: true
displayed_sidebar: solana
---

<!-- Do not edit this file. It is automatically generated by API Documenter. -->

# NFTCollection.getMetadata() method

Get the metadata for this program.

**Signature:**

```typescript
getMetadata(): Promise<NFTMetadata>;
```

**Returns:**

Promise&lt;NFTMetadata&gt;

program metadata

## Example

```jsx
const metadata = await program.getMetadata();
console.log(metadata);
```