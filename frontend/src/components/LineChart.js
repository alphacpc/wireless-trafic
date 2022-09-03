import React from 'react';
import { Line } from "react-chartjs-2"


const LineChart = ({length}) => {
  return (
    (length != null) ? <Line data={length} /> : "Chargement..."
  )
}

export default LineChart;