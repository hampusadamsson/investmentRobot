import React from 'react';
import axios from 'axios';
import {Line} from 'react-chartjs-2';
import config from './Config';
import './css/Portfolio.css';

export default class Portfolio extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      date: [],
      cash: [],
    };
    this.requestPortfolio();
  }

  getVectorDataAsPlot(){
    return (
      {
        labels: this.state.date,
        datasets: [
          {
            labels: "test",
            borderColor: 'rgba(75,202,72,.5)',
            pointRadius: 1,
            pointHitRadius: 1,
            data: this.state.cash,
          },
        ]
      }
    )
  }


  requestPortfolio(){
    let uri = `http://localhost:5003/p/` + this.props.portfolio;
    axios.get(uri)
      .then(res => {
        let portfolio = res.data.map(day => JSON.parse(day));
        this.setState({
          date : portfolio.map(day => day.date),
          cash : portfolio.map(day => parseFloat(day.cash)),
          holdings : portfolio.map(day => day.holdings),
        },
          console.log(this.state.cash),
        );
        console.log(res);
      })
  }

  render() {
    return (
      <div className='portfolio-frame'>
        <h4>
        {this.props.portfolio}
        </h4>
        <Line data={this.getVectorDataAsPlot()} options={config.options} />
      </div>
    )
  }
}
