import Home from "./components/Home";
import About from "./components/About";
import Navbar from "./components/Navbar";
import {Routes, Route} from 'react-router-dom';

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/About" element={<About/>} />
      </Routes>
      
     
     
    </div>
  );
}

export default App;  
