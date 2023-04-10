import React from "react";

export default function FeedbackFooter() {
  const [submissionState, setSubmissionState] = React.useState<
    "pending" | "open" | "answered"
  >("pending");

  const [feedback, setFeedback] = React.useState<string>("");

  async function handleSubmit(answer: boolean) {
    if (answer === true) {
      setSubmissionState("answered");
    }
    if (answer === false) {
      setSubmissionState("open");
    }
    sendPosthogEvent(answer);
  }

  async function sendPosthogEvent(value: boolean) {
    const posthog = window?.posthog;
    if (posthog) {
      posthog.capture("Portal Feedback", {
        response: value ? "yes" : "no",
      });
    }
  }

  async function handleSubmitText(text: string) {
    const posthog = window?.posthog;
    if (posthog && text?.length > 0) {
      posthog.capture("Portal Feedback", {
        feedback: text,
      });
      setSubmissionState("answered");
    }
  }

  // User hasn't clicked yes or no yet
  if (submissionState === "pending") {
    return (
      <div className="feedback card">
        <p className="feedback-title">这个页面对你有帮助吗?</p>
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
          }}
        >
          <button
            className="feedback-button"
            onClick={() => handleSubmit(true)}
            style={{
              marginRight: 8,
            }}
          >
            👍 有
          </button>
          <button
            className="feedback-button"
            onClick={() => handleSubmit(false)}
          >
            👎 没
          </button>
        </div>
      </div>
    );
  }

  // User clicked yes
  if (submissionState === "answered") {
    return (
      <div className="feedback card" style={{ justifyContent: "center" }}>
        <p className="feedback-title" style={{ width: "auto" }}>
        谢谢您的反馈 🙏
        </p>
      </div>
    );
  }

  // User clicked no (show feedback form)
  if (submissionState === "open") {
    return (
      <div
        className="feedback-form card"
        style={{
          alignItems: "flex-start",
          justifyContent: "flex-start",
        }}
      >
        <p className="feedback-form-title">很抱歉 😔</p>
        <p className="feedback-form-title">
        请描述您遇到的问题，以便我们改进页面。
        </p>
        <textarea
          className="feedback-form-input"
          style={{
            resize: "none",
          }}
          onChange={(e) => setFeedback(e.target.value)}
        />

        <button
          className="feedback-button"
          style={{
            width: "auto",
            marginTop: 16,
            cursor: "pointer",
          }}
          onClick={() => {
            handleSubmitText(feedback);
          }}
        >
          发送反馈
        </button>
      </div>
    );
  }
}
