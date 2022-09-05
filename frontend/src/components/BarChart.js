import React from 'react';
import { Bar } from "react-chartjs-2";

const BarChart = ({protocol}) => {
  return (
    (protocol != null) ? <Bar data={ protocol } /> : <p className='p-loader'>Chargement en cours !</p>
  )
}

export default BarChart;