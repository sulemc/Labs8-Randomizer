// Libraries
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import styled from 'styled-components';
import axios from 'axios';

const Person = styled.div`
width: 200px;
height: 200px;`

class Newuser extends Component {
    constructor() {
      super();
      this.state={
          pictures: [],
      }
    }
    componentDidMount() {
        fetch('https://randomuser.me/api')
        .then(results => {
            return results.json();

        }) .then(data => {
            let pictures = data.results.map((pic) => {
                return (
                    <div key={pic.results}>
                    <img  src={pic.picture.large}/>
                    </div>
                )
            })
            this.setState({pictures: pictures});
            console.log("state", this.state.pictures);
        })
    }

    render() {
        return (
            
    <Person>
        
        {this.state.pictures}
        
    </Person>
            
        )
    }
}
export default Newuser;