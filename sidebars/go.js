/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  // tutorialSidebar: [{type: 'autogenerated', dirName: '.'}],
  // But you can create a sidebar manually

  go: [
    {
      type: "doc",
      label: "Getting Started",
      id: "index",
    },
    {
      type: "doc",
      label: "ThirdwebSDK",
      id: "sdk",
    },
    {
      type: "doc",
      label: "IPFS Storage",
      id: "storage",
    },
    {
      type: "doc",
      label: "Deploying Contracts",
      id: "contract_deployer",
    },
    {
      type: "doc",
      label: "Custom Contracts",
      id: "custom",
    },
    {
      type: "doc",
      label: "Events",
      id: "contract_events",
    },
    {
      type: "doc",
      label: "Wallet Authentication",
      id: "wallet_authenticator",
    },
    {
      type: "category",
      label: "Contracts",
      collapsed: false,
      link: {
        type: "generated-index",
        title: "Contracts",
        description: "Interfaces for on-chain contracts.",
        keywords: ["contracts"],
      },
      items: [
        {
          type: "doc",
          label: "NFT Collection",
          id: "nft_collection",
        },
        {
          type: "doc",
          label: "Edition",
          id: "edition",
        },
        {
          type: "doc",
          label: "Token",
          id: "token",
        },
        {
          type: "doc",
          label: "NFT Drop",
          id: "nft_drop",
        },
        {
          type: "doc",
          label: "Edition Drop",
          id: "edition_drop",
        },
        {
          type: "doc",
          label: "Multiwrap",
          id: "multiwrap",
        },
        {
          type: "doc",
          label: "Marketplace",
          id: "marketplace",
        },
      ],
    },
    {
      type: "category",
      label: "Contract Interfaces",
      collapsed: true,
      link: {
        type: "generated-index",
        title: "Contract Interfaces",
        description:
          "Contract interfaces that extend the functionality of contracts.",
        keywords: ["contracts", "shared-interfaces"],
      },
      items: [
        {
          type: "category",
          label: "Contract Encoders",
          collapsed: true,
          link: {
            type: "generated-index",
            title: "Contract Encoders",
            description:
              "Contract encoders that return unsigned transaction data for contract calls.",
            keywords: ["contracts", "shared-interfaces"],
          },
          items: [
            {
              type: "doc",
              label: "Contract Encoder",
              id: "contract_encoder",
            },
            {
              type: "doc",
              label: "Marketplace Encoder",
              id: "marketplace_encoder",
            },
          ],
        },
        {
          type: "doc",
          label: "ERC 20",
          id: "erc20",
        },
        {
          type: "doc",
          label: "ERC 721",
          id: "erc721",
        },
        {
          type: "doc",
          label: "ERC 1155",
          id: "erc1155",
        },
        {
          type: "doc",
          label: "NFT Drop Claim Conditions",
          id: "nft_drop_claim_conditions",
        },
        {
          type: "doc",
          label: "Edition Drop Claim conditions",
          id: "edition_drop_claim_conditions",
        },
      ],
    },
    {
      type: "category",
      label: "Signature Minting",
      collapsed: true,
      link: {
        type: "generated-index",
        title: "Signature Minting",
        description: "Signature based minting for contracts.",
        keywords: ["contracts", "signature-minting"],
      },
      items: [
        {
          type: "doc",
          label: "ERC 721 Signature Minting",
          id: "erc721_signature_minting",
        },
        {
          type: "doc",
          label: "ERC 1155 Signature Minting",
          id: "erc1155_signature_minting",
        },
      ],
    },
  ],
};

module.exports = sidebars;
