import React, { useState, useEffect } from 'react';
import { Line } from "react-chartjs-2"


const LineChartMulti = ({len}) => {


  const [tabTCP, setTabTCP] = useState([])
  const [tabUDP, setTabUDP] = useState([])
  const [tabDays, setTabDays] = useState([])

  useEffect(()=>{
    len && setTabTCP(len.map(element => element['protocol_agg']['buckets'][0]['doc_count']))
    len && setTabUDP(len.map(element => element['protocol_agg']['buckets'][1]['doc_count']))
    len && setTabDays(len.map(element => element['key_as_string'].split(" ")[0]))
  },[len])


  console.log("Valeur de len => ",len)



  let dataFirst = {
    label: "TCP",
    data: tabTCP,
    lineTension: 0,
    fill: false,
    borderColor: '#F7EC09'
  };

  let dataSecond = {
    label: "UDP",
    data: tabUDP,
    lineTension: 0,
    fill: false,
    borderColor: '#3EC70B'
  };


  let speedData = {
    labels: tabDays,
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