import React from "react";

import ViewRepoButton from "./ViewRepoButton";

type Props = {
  repoName: string;
  repoUrl: string;
  isLibrary?: boolean;
};

export default function OpenSourceInfo({
  repoName,
  repoUrl,
  isLibrary = true,
}: Props) {
  return (
    <div className="open-source-info-container">
      <h2>
        开源 Open Source
        {isLibrary && " Library"}
      </h2>
      <p>
        {repoName} {isLibrary && "library"} 是开源项目。 你可以在{" "}
        <a href={repoUrl} target="_blank" rel="noopener noreferrer">
          GitHub
        </a>
        {" "}上查看源代码并对其进行贡献。
      </p>

      <ViewRepoButton name={repoName} text="View on GitHub" link={repoUrl} />
    </div>
  );
}
