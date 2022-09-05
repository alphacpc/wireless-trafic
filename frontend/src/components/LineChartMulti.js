import React from 'react';
import { Line } from "react-chartjs-2"


const LineChartMulti = ({len}) => {


  let dataFirst = {
    label: "Lorem ipsum",
    data: [0, 59, 75, 20, 20, 55, 40],
    lineTension: 0,
    fill: false,
    borderColor: '#F7EC09'
  };

  let dataSecond = {
    label: "Lorem impsum",
    data: [20, 15, 60, 60, 65, 30, 70],
    lineTension: 0,
    fill: false,
    borderColor: '#3EC70B'
  };


  let speedData = {
    labels: ["0s", "10s", "20s", "30s", "40s", "50s", "60s"],
    datasets: [dataFirst, dataSecond]
  };

let chartOptions = {
  legend: {
    display: true,
    position: 'top',
    labels: {
      boxWidth: 80,
      fontColor: 'black'
    }
  }
};


  return (
    (len != null) ? <Line data={speedData} options={chartOptions} /> : <p className='p-loader'>Chargement en cours !</p>
  )
}

export default LineChartMulti;