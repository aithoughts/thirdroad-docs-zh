import React from "react";

import GettingStartedCard from "../GettingStartedCard";

type Resource = {
  name: string;
  description: string;
  link: string;
  image: string;
};

const resources: Resource[] = [
  {
    name: "指南",
    description:
      "了解更多，指导关于如何使用thirdweb来构建你的web3应用程序",
    link: "https://blog.thirdweb.com/guides/",
    image: "/assets/resources/guides.svg",
  },
  {
    name: "模板",
    description:
      "使用我们的模板，用一行命令启动你的项目",
    link: "/templates",
    image: "/assets/resources/sdk-reference.svg",
  },
  {
    name: "油管",
    description:
      "通过视频教程构建工作应用程序来学习web3开发",
    link: "https://www.youtube.com/thirdweb",
    image: "/assets/resources/youtube.svg",
  },
  {
    name: "活动",
    description: "参加现场研讨会和办公时间，亲身体验代码",
    link: 'https://thirdweb.com/events',
    image: "/assets/resources/calendar.svg",
  },
  {
    name: "社区",
    description: "加入我们的开发者社区，构建web3的未来",
    link: 'https://discord.gg/thirdweb',
    image: "/assets/resources/discord.svg",
  },
  {
    name: "支持",
    description: "故障排除类文章，来自客户支持团队的实时支持",
    link: 'https://support.thirdweb.com',
    image: "/assets/resources/support.svg",
  }
];

export default function ResourceCards() {
  return (
    <div className="explore-products-container">
      <h2 className="explore-products-heading" style={{ marginBottom: 12 }}>
        更多资源
      </h2>
      <div className="row" style={{ marginBottom: 64 }}>
        {resources.map((p, i) => (
          <div className="col col--4" key={i} style={{ padding: 8 }}>
            <GettingStartedCard
              name={p.name}
              description={p.description}
              link={p.link}
              image={p.image}
            />
          </div>
        ))}
      </div>
    </div>
  );
}
