import React from 'react';
import axios from 'axios';
import Portfolio from './Portfolio';

export default class Requester extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      portfolioNames: [],
      selectedPortfolio: "test_portfolio32",
      selectedPortfolioData: null,
    }
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
    );
  }

  render() {
    return (
      <div>
        <select onChange={this.handleChange} >
          {this.state.portfolioNames.map(p =>
            <option value={p} key={p}>{p}</option>)
          }
        </select>
        <Portfolio portfolio={this.state.selectedPortfolio} />
      </div>
    )
  }
}
