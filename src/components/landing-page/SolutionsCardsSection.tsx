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
    image: "/assets/product/sdk.png",
    name: "CommerceKit",
    description:
      "构建web3商务应用程序的一体化工具包。为Shopify店面添加强大的web3功能，支持代币化商务、NFT忠诚计划、数字收藏品销售等等。",
    link: "https://thirdweb.com/solutions/commerce",
  },
  {
    image: "/assets/product/sdk.png",
    name: "GamingKit",
    description:
      "构建web3游戏所需的一切。通过给予玩家游戏内资产的所有权，围绕游戏构建更强大的社区",
    link: "https://thirdweb.com/solutions/gaming",
  },
  {
    image: "/assets/product/sdk.png",
    name: "Minting",
    description:
      "强大的工具集，允许创建者和开发人员以可配置、安全和可扩展的方式启动新的NFT合集，而无需创建者承担任何成本。",
    link: "https://thirdweb.com/solutions/minting",
  },
];

export default function SolutionsSection() {
  return (
    <div className="explore-products-container">
      <h2 className="explore-products-heading" style={{ marginBottom: 12 }}>
        解决方案
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
