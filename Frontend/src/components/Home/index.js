import React from "react";
import { Layout, Row, Col, Typography, Card } from "antd";
import { Link } from "react-router-dom";
import {
  MessageOutlined,
} from "@ant-design/icons";

const { Header, Content } = Layout;
const { Title, Text } = Typography;

const HomePage = () => {
  return (
    <Layout style={{ minHeight: "90vh" }}>
      <Header>
        <Title level={3} style={{ color: "white" }}>
          Welcome to IBM Watson Chatbot!
        </Title>
      </Header>

      <Content style={{ padding: "50px" }}>
        <Text style={{ color: "black" }}>
          This chatbot works with IBM Watson API with llama3 as the chat service provider.
        </Text>
        <Row justify="center">
          <Col span={24} style={{ textAlign: "center" }}>
            <Title level={3}>Start chatting now : </Title>
          </Col>
        </Row>
        <Row gutter={[16, 16]} justify="center">
          <Col xs={24} sm={12} lg={8}>
            <Link to="/chat_ai_app">
              <Card
                hoverable
                style={{ minHeight: "200px" }}
                cover={
                  <MessageOutlined
                    style={{
                      fontSize: "64px",
                      textAlign: "center",
                      margin: "20px 0",
                    }}
                  />
                }
              >
                <Card.Meta
                  title="Chat App"
                  description="Have any question? Get it resolved right away with Watsonx!"
                />
              </Card>
            </Link>
          </Col>
        </Row>
      </Content>
    </Layout>
  );
};

export default HomePage;
