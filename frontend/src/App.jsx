import {BrowserRouter, Routes, Route, Link} from 'react-router-dom'
import './App.css'
import ButtonsPage from './pages/ButtonsPage'
import ConfigPage from './pages/ConfigPage'
import { QueryClient, QueryClientProvider } from 'react-query';

const client = new QueryClient()

function App() {
  return (
    <QueryClientProvider client={client}>
      <BrowserRouter>
        <nav>
          <Link to="/">Buttons</Link>
          <Link to="/config">Config</Link>
        </nav>
        <Routes>
          <Route path="/" element={<ButtonsPage />}/>
          <Route path="/config" element={<ConfigPage />}/>
          <Route path="/*" element={<ButtonsPage />}/>
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  )
}

export default App
