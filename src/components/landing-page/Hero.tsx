import React from "react";
import ThemedImage from "@theme/ThemedImage";

export default function Hero() {
  return (
    <>
      <div className="hero-container">
        <div className="hero-left">
          <h1 className="hero-left-title">
            thirdroad 文档 <br /> 翻译自 thirdweb documentation
          </h1>
          <p className="hero-left-description">
            thirdweb是一个完整的web3开发框架，提供了将你的应用程序和游戏连接到去中心化网络所需的一切。
          </p>
        </div>

        <div className="hero-right">
          <div className="hero-right-image-container">
            <ThemedImage
              sources={{
                light: "/assets/docs-hero-light-2.png",
                dark: "/assets/docs-hero.png",
              }}
              className="hero-right-image"
              alt="thirdweb documentation hero image"
            />
          </div>
        </div>
      </div>

      <hr className="hero-divider" />
    </>
  );
}
