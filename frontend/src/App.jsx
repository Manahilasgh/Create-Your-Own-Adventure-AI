import './App.css'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import StoryLoader from './components/StoryLoader'
import StoryGenerator from './components/StoryGenerator'
import SignUp from './auth/SignUp'
import Login from './auth/LogIn'
import ProtectedRoute from './auth/ProtectedRoute'

function App() {

   return (
    <Router>
      <div className="app-container">
        <header>
          <h1>Interactive Story Generator</h1>
        </header>
        <main>
          <Routes>
            <Route path={"/"} element={<SignUp />}/>
            <Route path={"/login"} element={<Login />}/>
            <Route path={"/story"} element={
              <ProtectedRoute> <StoryGenerator />
              </ProtectedRoute>}
              />
            <Route path={"/story/:id"} element={
              <ProtectedRoute> <StoryLoader />
              </ProtectedRoute>}
              />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App;
