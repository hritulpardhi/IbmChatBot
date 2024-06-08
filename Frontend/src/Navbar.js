// import { Link, useMatch, useResolvedPath } from "react-router-dom";

// export default function Navbar() {
//   return (
//     <nav className="nav">
//       <Link to="/" className="site-title">
//         Home
//       </Link>
//       <ul>
//         <CustomLink to="/weather_app">Weather app</CustomLink>
//         <CustomLink to="/youtube_statistics">YouTube statistics</CustomLink>
//         <CustomLink to="/chat_ai_app">Chat App</CustomLink>
//       </ul>
//     </nav>
//   );
// }

// function CustomLink({ to, children, ...props }) {
//   const resolvedPath = useResolvedPath(to);
//   const isActive = useMatch({ path: resolvedPath.pathname, end: true });

//   return (
//     <li className={isActive ? "active" : ""}>
//       <Link to={to} {...props}>
//         {children}
//       </Link>
//     </li>
//   );
// }

import { Menu } from 'antd';
import { Link } from 'react-router-dom';
import { CloudFilled, HomeFilled, HomeOutlined, WechatWorkOutlined, YoutubeFilled } from '@ant-design/icons';
import { useLocation } from 'react-router-dom';
export default function Navbar() {
  const location = useLocation();
  const { pathname } = location;

  return (
    <Menu theme="dark" mode="horizontal" selectedKeys={[pathname]}>
      <Menu.Item key="/" icon={<HomeFilled />}>
        <Link to="/">Home</Link>
      </Menu.Item>
      <Menu.Item key="/chat_ai_app" icon={<WechatWorkOutlined />}>
        <Link to="/chat_ai_app">Chat App</Link>
      </Menu.Item>
    </Menu>
  );
}
