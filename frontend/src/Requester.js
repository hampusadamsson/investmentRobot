import React from 'react';

import axios from 'axios';

export default class Requester extends React.Component {
  state = {
    portfolioNames: [],
    selectedPortfolio: null,
    selectedPortfolioData: null,
  }

  componentDidMount() {
    let uri = `http://localhost:5003/pnames`;
    axios.get(uri)
      .then(res => {
        const portfolioNames = res.data;
        this.setState({ portfolioNames });
        console.log(res);
      })
  }

  handleChange = (event) => {
    this.setState({
      selectedPortfolio: event.target.value,
    },
    this.requestPortfolio(),
    );
  }

  requestPortfolio(){
    let uri = `http://localhost:5003/p/` + this.state.selectedPortfolio;
    axios.get(uri)
      .then(res => {
        const selectedPortfolioData = res.data;
        this.setState({ selectedPortfolioData });
        console.log(res);
      })
  }

  render() {
    return (
      <div>
        <select onChange={this.handleChange} >
          {this.state.portfolioNames.map(p =>
            <option value={p} key={p}>{p}</option>)
          }
        </select>
        <i>
          {this.state.selectedPortfolioData}
        </i>
      </div>
    )
  }
}
