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
      holdingsValue: [],
      totalValue: [],
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
            data: this.state.totalValue,
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
        //console.log(portfolio);

        let cash = portfolio.map(day => parseFloat(day.cash));
        let date = portfolio.map(day => day.date);
        let holdingsValue = portfolio.map(day => Object.values(day.holdings)
              .map(stock => stock.adjusted_close)
              .reduce((a, b) => a + b, 0));

        let totalValue = holdingsValue
              .map(function (num, idx) {return num + cash[idx];});

        this.setState({
          date: date,
          cash: cash,
          holdingsValue: holdingsValue,
          totalValue: totalValue,
        });
      })
  }

  calculateChange(){
    const initValue = parseFloat(this.state.totalValue[0]);
    const lengthOfArray = this.state.totalValue.length-1;
    const currentValue = parseFloat(this.state.totalValue[lengthOfArray]);
    const delta = currentValue / initValue;
    const readableDelta = ((delta-1)*100).toFixed(1);
    const sign = delta >= 1 ? "+" : "";
    return sign + readableDelta + "%";
  }

  render() {
    return (
      <div className='portfolio-frame'>
        <h4>
        {this.props.portfolio}
        </h4>
        {this.calculateChange()}
        <Line data={this.getVectorDataAsPlot()} options={config.options} />
      </div>
    )
  }
}
