import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Pousadas from './pages/Pousadas';
import Sobre from './pages/Sobre';
export default function App(){
  return (
    <Routes>
      <Route path='/' element={<Home/>} />
      <Route path='/pousadas' element={<Pousadas/>} />
      <Route path='/sobre' element={<Sobre/>} />
    </Routes>
  )
}
