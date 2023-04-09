import React from "react";

import ProductCard from "./ProductCard";

type Product = {
  image: string;
  name: string;
  description: string;
  link: string;
};

const products: Product[] = [
  {
    image: "/assets/product/extensions.png",
    name: "Solidity SDK",
    description:
      "基础合约，可以配置扩展以满足你的特定用例",
    link: "/solidity",
  },
  {
    image: "/assets/product/contracts.png",
    name: "探索",
    description:
      "一键发现和部署来自世界级协议和开发人员的合约",
    link: "/pre-built-contracts",
  },
  {
    image: "/assets/product/sdk.png",
    name: "SDK",
    description:
      "每个技术栈都有强大的SDK，支持Javascript, React, Python, Go, Node.js, Unity",
    link: "/sdk",
  },
  {
    image: "/assets/product/ui.png",
    name: "UI组件",
    description:
      "即插即用的UI组件可以轻松地将web3功能添加到应用程序中",
    link: "/react/react.web3button",
  },
  {
    image: "/assets/product/deploy.png",
    name: "部署",
    description:
      "通过为团队协作设计的简单部署工作流，在链上部署合同",
    link: "/deploy",
  },
  {
    image: "/assets/product/publish.png",
    name: "发布",
    description:
      "发布你的合同，让我们70k+的web3开发者社区发现你的合同",
    link: "/publish",
  },
  {
    image: "/assets/product/dashboard.png",
    name: "仪表板",
    description:
      "一站式方便地交互、管理、分析所有部署的合约",
    link: "/dashboard",
  },
  {
    image: "/assets/product/CLI.png",
    name: "CLI",
    description:
      "一套命令，允许你通过终端与thirdweb工具进行交互",
    link: "/cli",
  },
];

export default function ExploreProductsSection() {
  return (
    <div className="explore-products-container">
      <h2 className="explore-products-heading" style={{ marginBottom: 12 }}>
        全栈工具
      </h2>
      <div className="row" style={{ marginBottom: 64 }}>
        {products.map((p, i) => (
          <div className="col col--4" key={i} style={{ padding: 8 }}>
            <ProductCard
              image={p.image}
              name={p.name}
              description={p.description}
              link={p.link}
            />
          </div>
        ))}
      </div>
    </div>
  );
}
