import React, { useEffect, useState } from "react";
import {
  Button,
  Card,
  Layout,
  List,
  Space,
  Spin,
  Tooltip,
  message,
  Input,
} from "antd";
import {
  CopyTwoTone,
  MessageOutlined,
  SendOutlined,
  UserOutlined,
} from "@ant-design/icons";
import axios from "axios";

const { Content, Footer } = Layout;
const { TextArea } = Input; // Import TextArea from Input

const ChatApp = () => {
  const [messageContent, setMessage] = useState(""); // State to manage the text input value
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState([]); // State to manage the list of messages

  // Function to save messages to localStorage
  const saveMessagesToLocalStorage = (messages) => {
    localStorage.setItem("chatMessages", JSON.stringify(messages));
  };

  useEffect(() => {
    // Load messages from localStorage when component mounts
    const storedMessages = localStorage.getItem("chatMessages");
    if (storedMessages) {
      setMessages(JSON.parse(storedMessages));
    }
  }, []);

  const handleMessageChange = (e) => {
    // Update the message state with the input value
    setMessage(e.target.value);
  };

  const handleKeyDown = (e) => {
    // Check if Shift key and Enter key are pressed together
    if (e.shiftKey && e.key === "Enter") {
      // Prevent default behavior (sending message) and add a newline
      e.preventDefault();
      setMessage(messageContent + "\n");
    }
  };

  const sendMessage = async () => {
    if (!messageContent.trim()) return; // Prevent sending empty messages
    setIsLoading(true);
    try {
      // Make the POST request to Watson API
      const response = await axios.post(
        "http://127.0.0.1:8000/watson/watson_api/",
        {
          message: messageContent.trim(), // Trim the message content
        }
      );

      // Add user message to the messages state
      const userMessage = { type: "user", text: messageContent };
      setMessages((prevMessages) => [...prevMessages, userMessage]);

      // Check if the response contains the expected structure
      if (response.data && response.status === 200) {
        // Add Watson's response to the messages state
        const watsonMessage = {
          type: "watson",
          text: response?.data?.data?.results[0]?.generated_text,
        };
        setMessages((prevMessages) => [...prevMessages, watsonMessage]);

        // Save messages to localStorage
        saveMessagesToLocalStorage([...messages, userMessage, watsonMessage]);
      } else {
        console.error("Invalid response structure:", response.data);
      }

      // Clear the input field
      setMessage("");
    } catch (error) {
      console.error("Error sending message:", error);
    } finally {
      setIsLoading(false);
    }
  };

  // Copy the message to clipboard
  const copyToClipboard = (text) => {
    navigator.clipboard
      .writeText(text)
      .then(() => {
        message.success("Text copied to clipboard", 2); // Specify the duration in seconds
        setTimeout(() => {
          message.destroy(); // Close the message after 2 seconds
        }, 2000);
      })
      .catch((error) => {
        message.error("Error copying text to clipboard");
      });
  };

  // useEffect to update messages when message or isLoading state changes
  useEffect(() => {
    // Scroll to the bottom of the chat window when new messages are added
    const chatWindow = document.getElementById("chat-window");
    if (chatWindow) {
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }
  }, [messages, isLoading]);

  return (
    <Layout>
      <Spin spinning={isLoading}>
        <div style={{ background: "#21272a" }}>
          <Content style={{ padding: "24px", background: "#21272a" }}>
            <div
              id="chat-window"
              style={{
                height: "80vh",
                overflow: "auto",
              }}
            >
              {messages.length > 0 ? (
                <List
                  style={{ maxHeight: "100%", overflow: "auto" }}
                  itemLayout="horizontal"
                  dataSource={messages}
                  renderItem={(item) => (
                    <List.Item
                      style={{
                        display: "flex",
                        justifyContent:
                          item.type === "user" ? "flex-start" : "flex-end",
                        textAlign: "left",
                      }}
                    >
                      <List.Item.Meta
                        title={
                          item.type === "user" ? (
                            <>
                              <UserOutlined /> User
                            </>
                          ) : (
                            <>
                              <MessageOutlined /> Watsonx
                            </>
                          )
                        }
                        style={{
                          background:
                            item.type === "user" ? "#00539a" : "#9ef0f0",
                          padding: "12px",
                          borderRadius: "6px",
                          boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
                          maxWidth: "80%",
                        }}
                        description={
                          <Card>
                            <div>
                              <span
                                dangerouslySetInnerHTML={{
                                  __html: item.text.replace(/\n/g, "<br />"),
                                }}
                              />
                              <div>
                                <span
                                  style={{
                                    fontWeight: 500,
                                    color: "#2a2a2a",
                                    textAlign:
                                      item.type === "user" ? "left" : "right",
                                  }}
                                >
                                  {item.type !== "user" && (
                                    <span
                                      onClick={() => copyToClipboard(item.text)}
                                    >
                                      <CopyTwoTone />
                                    </span>
                                  )}
                                </span>
                              </div>
                            </div>
                          </Card>
                        }
                      />
                    </List.Item>
                  )}
                />
              ) : (
                <div style={{ textAlign: "center", padding: "20px" }}>
                  <h2 style={{color:"white"}}>
                    Welcome to chatbot! Please enter your input below to start
                    the chat with Watsonx.
                  </h2>
                </div>
              )}
            </div>
          </Content>
        </div>
        <Footer
          style={{
            background: "#21272a",
          }}
        >
          <div style={{ display: "flex", width: "100%", alignItems: "center" }}>
            <TextArea
              size="large"
              value={messageContent}
              onChange={handleMessageChange}
              onKeyDown={handleKeyDown} // Handle Shift + Enter
              placeholder="Type your message here..."
              autoSize={{ minRows: 1, maxRows: 6 }}
              style={{
                flex: 9,
                marginRight: "8px",
                boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
              }}
            />
            <Tooltip title="Send message">
              <Button
                size="large"
                icon={<SendOutlined />}
                onClick={sendMessage}
                style={{ background: "#9ef0f0", flex: 1 }}
                disabled={!messageContent}
              />
            </Tooltip>
          </div>
        </Footer>
      </Spin>
    </Layout>
  );
};

export default ChatApp;
