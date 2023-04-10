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
    image: "/assets/product/auth.png",
    name: "Auth",
    description:
      "用钱包对用户进行身份验证。安全地验证用户的链上身份，而不依赖于集中式数据库",
    link: "/auth",
  },
  {
    image: "/assets/product/storage.png",
    name: "Storage",
    description:
      "快速访问存储在区块链上的数据。使用与你选择的存储提供商合作的统一API，进行便捷操作",
    link: "/storage",
  },
  {
    image: "/assets/product/wallet.png",
    name: "Wallet",
    description:
      "将钱包连接功能集成到web3应用程序中",
    link: "/wallet",
  },
];

export default function InfrastructureCards() {
  return (
    <div className="explore-products-container">
      <h2 className="explore-products-heading" style={{ marginBottom: 12 }}>
        基础设施
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
