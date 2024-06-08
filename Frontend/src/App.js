import Navbar from "./Navbar"
import { Route, Routes } from "react-router-dom"
import HomePage from "./components/Home"
import ChatApp from "./components/ChatApp"

function App() {
  return (
    <>
      <Navbar />
      <div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/chat_ai_app" element={<ChatApp />} />
        </Routes>
      </div>
    </>
  )
}

export default App