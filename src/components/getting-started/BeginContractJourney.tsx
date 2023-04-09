import React, { useEffect, useState } from "react";

const items = [
  {
    id: "prebuilt-contract-section",
    title: "探索合约",
    description:
      "可以一键部署安全、gas费优化、经过审计的合约。",
    icon: "/product/contracts.png",
  },
  {
    id: "custom-contract-section",
    title: "构建合约",
    description:
      "使用Solidity SDK创建特定于你的用例的自定义合约。",
    icon: "/product/extensions.png",
  },
  {
    id: "deploy-contract-section",
    title: "源码部署",
    description:
      "已经有准备部署的合约了吗? 学习如何使用我们的交互式CLI来发布它。",
    icon: "/product/deploy.png",
  },
];

export default function BeginContractJourney() {
  const [activeTab, setActiveTab] = useState<number | undefined>(undefined);

  useEffect(() => {
    if (activeTab === undefined) return;
    // Grab the id of the items[activeTab]
    const id = items[activeTab]?.id;
    if (!id) return;
    // Grab the element with the id
    const element = document.getElementById(id);
    if (!element) return;

    // Update the other tabs visibility css
    items.forEach((item, index) => {
      const otherElement = document.getElementById(item.id);
      if (!otherElement) return;

      // Set height too
      otherElement.style.height = index === activeTab ? "auto" : "0px";
      // Overflow
      otherElement.style.overflow = index === activeTab ? "visible" : "hidden";

      // Set opacity too
      otherElement.style.opacity = index === activeTab ? "1" : "0";
    });

    // wait 0.1 seconds
    setTimeout(() => {
      // Scroll to the element
      // Scroll to the second h3 element
      const h3 = element.getElementsByTagName("h3")[0];

      // Get the offset of the h3 element
      const offset = h3.offsetTop;

      // Scroll to the offset
      window.scrollTo({
        top: offset - 72,
        behavior: "smooth",
      });
    }, 301);
  }, [activeTab]);

  return (
    <div className="contract-journey-container">
      {items.map((item, index) => (
        <div
          className={`tw-card contract-journey-card ${
            activeTab === index ? "active-journey-card" : ""
          }`}
          data-getting-started-deploy-pathway={item.title}
          key={index}
          onClick={() => setActiveTab(index)}
        >
          <div className="heading">
            <img
              className="logo"
              src={`/assets${item.icon}`}
              alt={item.title}
            />
            <p className="title">{item.title}</p>
          </div>

          <p className="description">{item.description}</p>
        </div>
      ))}
    </div>
  );
}
