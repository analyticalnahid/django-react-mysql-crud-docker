import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import Home from "./component/Home";
import Department from "./component/Department";
import Employee from "./component/Employee";

function App() {
  return (
    <BrowserRouter>
    <div className="App container">
      <h2 >React JS Frontend</h2>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <ul className="navbar-nav">
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary " to="/home">
              Home
            </NavLink>
          </li>
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary " to="/department">
              Department
            </NavLink>
          </li>
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary " to="/employee">
              Employee
            </NavLink>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/department" element={<Department />} />
        <Route path="/employee" element={<Employee />} />
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
