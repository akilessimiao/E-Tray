import React, { useEffect, useState } from 'react';
import api from '../services/api';
export default function Home(){
  const [pousadas, setPousadas] = useState([]);
  useEffect(()=>{ api.get('/pousadas/?tem_cafe=false').then(r=>setPousadas(r.data)).catch(()=>setPousadas([])) },[]);
  return (
    <div className='container'>
      <header className='header'><img src='/assets/logo_estay.png' className='logo' alt='E-Stay'/><div><h1 style={{color:'#4CC9F0'}}>E-Stay</h1><p>Hospedagem inteligente com tecnologia LinkUp</p></div></header>
      <section>
        {pousadas.length===0 ? <div className='card'>Nenhuma pousada encontrada (mock)</div> : pousadas.map(p=> <div className='card' key={p.id}><h3>{p.nome}</h3><p>{p.endereco}</p><p>⭐ {p.avaliacao}</p><a href={p.link} target='_blank' rel='noreferrer'>Ver no Google Maps</a></div>)}
      </section>
    </div>
  )
}
