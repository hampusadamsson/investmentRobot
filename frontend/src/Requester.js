import React from 'react';
import axios from 'axios';
import Portfolio from './Portfolio';
import './css/Requester.css';

export default class Requester extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      portfolioNames: [],
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
        <h2>Portfolios</h2>
        <div className='portfolio-holders'>
          {this.state.portfolioNames.map(p =>
            <Portfolio portfolio={p} key={p}/>
          )}
        </div>
      </div>
    )
  }
}
