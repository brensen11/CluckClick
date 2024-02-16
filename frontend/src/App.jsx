import {BrowserRouter, Routes, Route, Link} from 'react-router-dom'
import './App.css'
import ButtonsPage from './pages/ButtonsPage'
import ConfigPage from './pages/ConfigPage'

function App() {
  return (
    <>
      <h1>Click Cluck</h1>
      <BrowserRouter>
        <nav>
          <Link to="/">Home</Link>
          <Link to="/buttons">Buttons</Link>
          <Link to="/config">Config</Link>
        </nav>
        <Routes>
          <Route path="/buttons" element={<ButtonsPage />}/>
          <Route path="/config" element={<ConfigPage />}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
